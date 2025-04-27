from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate
from scholarly import scholarly
import time

# Load environment variables (for API keys etc.)
load_dotenv()

# Initialize the Gemini model
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-001')

st.title("Research Paper Summarizer 📄✨")

# User input for the research topic
topic_input = st.text_input("Enter a research topic to search for papers:")

# Variables to store papers
paper_titles = []
papers_data = []

# If topic is entered
if topic_input:
    with st.spinner("Searching for papers..."):
        search_query = scholarly.search_pubs(topic_input)
        for i in range(10):  # Get top 10 papers
            try:
                paper = next(search_query)
                paper_titles.append(paper['bib']['title'])
                papers_data.append(paper)
                time.sleep(1)  # Be polite to Google Scholar
            except StopIteration:
                break

    if paper_titles:
        paper_input = st.selectbox(
            "Select a research paper to summarize:",
            options=paper_titles
        )

        style_input = st.selectbox(
            "Select a style for the summary:",
            options=[
                "Concise",
                "Detailed",
                "Technical",
                "Layman's Terms",
                "Comparative",
            ],
        )

        length_input = st.selectbox(
            "Select the length of the summary:",
            options=[
                "Short (1-2 sentences)",
                "Medium (3-5 sentences)",
                "Long (1 paragraph)",
                "Very Long (2 paragraphs)",
            ],
        )

        template = PromptTemplate(
            template="""
            Please summarize the research paper titled "{paper_input}" with the following specifications:
            - Explanation Style: {style_input}
            - Explanation Length: {length_input}

            Additional Instructions:
            1. Mathematical Details:
                - Include relevant mathematical details and equations if present in the paper.
                - Explain mathematical concepts clearly, using simple intuitive code snippets if applicable.
            2. Analogies:
                - Use relatable analogies to explain complex concepts.

            If certain information is missing from the paper, respond with "INSUFFICIENT INFORMATION AVAILABLE" instead of guessing.

            Ensure the summary is clear, accurate, and aligned with the provided style and length.
            """,
            input_variables=["paper_input", "style_input", "length_input"]
        )

        prompt = template.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

        if st.button("Summarize"):
            with st.spinner("Generating summary..."):
                result = model.invoke(prompt)
                st.subheader("Summary:")
                st.write(result.content)
    else:
        st.warning("No papers found for this topic. Try a different keyword.")
else:
    st.info("Please enter a topic above to search papers.")

