import os
from dotenv import load_dotenv
from groq import Groq
from ddgs import DDGS
import wikipediaapi

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


# --- Tools ---
def web_search(query: str) -> str:
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
        if not results:
            return "No results found."
        return "\n".join([f"- {r['title']}: {r['body']}" for r in results])
    except Exception as e:
        return f"Search error: {str(e)}"


def wiki_search(query: str) -> str:
    try:
        wiki = wikipediaapi.Wikipedia(language="en", user_agent="researchmind/1.0")
        page = wiki.page(query)
        if not page.exists():
            return "No Wikipedia page found."
        return page.summary[:1000]
    except Exception as e:
        return f"Wikipedia error: {str(e)}"


# --- Agent loop ---
def research(topic: str):
    steps = []

    # Step 1: Web search
    print("  → Searching the web...")
    search_result = web_search(topic)
    steps.append(
        {"role": "web_search", "content": f"Query: {topic}\n\n{search_result[:500]}"}
    )

    # Step 2: Wikipedia
    print("  → Searching Wikipedia...")
    wiki_result = wiki_search(topic)
    steps.append(
        {"role": "wikipedia", "content": f"Query: {topic}\n\n{wiki_result[:500]}"}
    )

    # Step 3: Synthesise with LLM
    print("  → Synthesising report...")
    synthesis_prompt = f"""You are a research assistant. Based on the following sources, write a clear, structured research report on: {topic}

--- WEB SEARCH RESULTS ---
{search_result}

--- WIKIPEDIA ---
{wiki_result}

Write a structured report with:
1. Overview
2. Key Findings
3. Current Trends
4. Conclusion

Be detailed and informative."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": synthesis_prompt}],
    )

    report = response.choices[0].message.content
    steps.append({"role": "assistant", "content": report[:300]})

    return {"steps": steps, "report": report}


if __name__ == "__main__":
    topic = "AI agents in 2025"
    print(f"Researching: {topic}\n")
    result = research(topic)

    print("\n=== REASONING TRACE ===")
    for step in result["steps"]:
        print(f"\n[{step['role'].upper()}]")
        print(step["content"][:300])

    print("\n=== FINAL REPORT ===")
    print(result["report"])
