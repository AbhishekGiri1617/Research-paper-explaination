# 📄 Research Paper Summarizer using LangChain + Gemini AI

This is a **Streamlit** web app that helps you **summarize research papers** in various styles and lengths, powered by **LangChain** and **Gemini AI**!  
It fetches **top 10 research papers** from **Google Scholar** based on your chosen topic, and generates a smart, customized summary with optional technical depth, analogies, and mathematical details.

---

## 🚀 Features

- 🔍 **Search Papers:** Enter any research topic and instantly fetch top 10 related papers from Google Scholar.
- 📑 **Select Paper:** Choose a paper title from the search results.
- 🛠️ **Customize Summary Style:** 
  - Concise
  - Detailed
  - Technical
  - Layman's Terms
  - Comparative
- 📏 **Choose Summary Length:**
  - Short (1-2 sentences)
  - Medium (3-5 sentences)
  - Long (1 paragraph)
  - Very Long (2 paragraphs)
- 🤖 **Powered by LangChain + Gemini AI:** Generates high-quality, factual, and customized summaries.
- 📈 **Mathematical Details:** Includes equations/code snippets where applicable.
- 🎯 **Relatable Analogies:** Explains complex concepts in an easy-to-understand way.
- 🛡️ **No Guessing:** If information is missing, the model says "INSUFFICIENT INFORMATION AVAILABLE."

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.dev/)
- [Google Gemini AI](https://deepmind.google/technologies/gemini/)
- [scholarly (Google Scholar search)](https://pypi.org/project/scholarly/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone (https://github.com/AbhishekGiri1617/Research-paper-explaination.git)
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup environment variables:**
   Create a `.env` file and add your Gemini API key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run researchpapersummary.py
   ```

---

## ✍️ Usage

- Enter a **research topic** (example: "Transformer models").
- Choose a **paper** from the dropdown.
- Select your preferred **summary style** and **length**.
- Click **"Summarize"** and get a high-quality AI-generated summary!

---
