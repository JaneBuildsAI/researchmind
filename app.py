import streamlit as st
from agent.researcher import research

st.set_page_config(page_title="ResearchMind", page_icon="🧠", layout="wide")

# Header
st.title("🧠 ResearchMind")
st.caption(
    "AI research agent — searches the web, synthesises sources, delivers structured reports."
)

st.divider()

# Input
topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Large language models, Climate change 2025, Quantum computing",
)

run = st.button("Research", type="primary")

if run and topic:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📄 Report")
        with st.spinner("Researching..."):
            result = research(topic)
        st.markdown(result["report"])

    with col2:
        st.subheader("🔍 Reasoning Trace")
        for step in result["steps"]:
            role = step["role"].replace("_", " ").title()
            with st.expander(f"[{role}]"):
                st.write(step["content"][:500])

elif run and not topic:
    st.warning("Please enter a topic first.")
