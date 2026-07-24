# AI Partners RAG Knowledge Bot 🤖
Link : https://rag-interview-wiyao-984449208354.europe-west9.run.app/

A production-ready, containerized **Advanced RAG (Retrieval-Augmented Generation)** application built with **Streamlit**, **LangChain**, and Google's state-of-the-art **Gemini 3.6-flash** and **Gemini Embedding 2** models.

Designed for high performance, zero-latency vector retrieval, and enterprise reliability, this application allows users to query internal documentation safely with strict anti-hallucination guardrails and dynamic source transparency.

---

## Key Architecture & Features

- **Semantic Ingestion & Chunking:** Processes markdown knowledge bases using structural header splitting (`MarkdownHeaderTextSplitter`) combined with recursive character segmentation to preserve contextual integrity.
- **Dense Vector Search:** Leverages Google's `gemini-embedding-2` model mapped to an in-memory `FAISS` index for lightning-fast similarity lookups.
- **State-of-the-Art Generation:** Powered by `gemini-3.6-flash` running at a low temperature (`0.1`) for deterministic, factual data extraction.
- **Robust Streaming Parser:** Dynamically parses streaming API output to handle both string and structured multi-modal list payloads seamlessly.
- **Smart UI Gating & Source Transparency:** Queries the top 3 contextual chunks to feed the LLM, but intelligently displays **only the primary source (Chunk 1)** inside a conditional expander. If a fallback is triggered, source rendering is automatically suppressed to prevent user confusion.


---

## Local Installation & Run

- Clone the repository and set up a virtual environment : 
   * python -m venv venv
   * source venv/bin/activate
- Install dependencies:
   * pip install -r requirements.txt
- Create a .env file at the root of the project and update with GOOGLE_API_KEY=your_actual_api_key_here
- Run the Streamlit application:
   * streamlit run app.py
- Docker Local Testing :
   * docker build -t ai-partners-rag .
   * docker run -p 8501:8501 -e GOOGLE_API_KEY=your_actual_api_key_here ai-partners-rag





