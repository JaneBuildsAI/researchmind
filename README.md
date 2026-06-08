# 🧠 ResearchMind

An AI research agent that searches the web, synthesises sources, and delivers structured reports — with full reasoning transparency.

**Live demo:** https://mindresearch.streamlit.app

## What it does
- Takes any research topic as input
- Searches the web using DuckDuckGo
- Pulls background context from Wikipedia
- Synthesises findings into a structured report
- Shows a full reasoning trace of every step the agent took

## Tech stack
- **LLM:** Llama 3.3 70B via Groq API
- **Search:** DuckDuckGo Search
- **Knowledge:** Wikipedia API
- **UI:** Streamlit
- **Deployment:** Streamlit Community Cloud

## Run locally

1. Clone the repo
   git clone https://github.com/JaneBuildsAI/researchmind.git
   cd researchmind

2. Create a virtual environment and activate it
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Add your Groq API key to a .env file
   GROQ_API_KEY=your_key_here

5. Run the app
   streamlit run app.py

## Built by
Janet Eluwole — AI Engineer
https://github.com/JaneBuildsAI