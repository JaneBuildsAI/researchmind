import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool

load_dotenv()

# LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"), temperature=0
)

# Search tool
search = DuckDuckGoSearchRun()
search_tool = Tool(
    name="web_search",
    func=search.run,
    description="Search the web for current information on a topic.",
)

# Wikipedia tool
wikipedia = WikipediaAPIWrapper()
wiki_tool = Tool(
    name="wikipedia",
    func=wikipedia.run,
    description="Get background information on a topic from Wikipedia.",
)

tools = [search_tool, wiki_tool]

if __name__ == "__main__":
    # Test both tools
    print("Testing search...")
    print(search_tool.run("AI agent frameworks 2024"))
    print("\nTesting Wikipedia...")
    print(wiki_tool.run("Artificial Intelligence"))
