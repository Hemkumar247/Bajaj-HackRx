# HackRx 6.0 - Intelligent Document Q&A Bot

This project is a submission for the HackRx 6.0 hackathon. It is an intelligent system that uses Large Language Models (LLMs) to answer natural language questions based on a large unstructured document, in simple it user RAG to process the query.

## 🚀 Features
- **Natural Language Understanding:** Ask questions in plain English.
- **Justified Answers:** The system can provide the source from the document for its answers.
- **Structured Output:** Delivers clean, machine-readable JSON responses.
- **API-Ready:** Built with FastAPI for easy integration.

## 🛠️ Tech Stack
- **Core Logic:** LangFlow
- **LLM:** Google Gemini
- **API:** FastAPI, Uvicorn
- **Embeddings & Vector Store:** (e.g., HuggingFace Embeddings, FAISS)

## 📦 Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [your-github-repo-link]
    cd HackRx_Submission
    ```
2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set Up Environment Variables:**
    -   Copy the `.env.example` file to a new file named `.env`.
    -   Open the `.env` file and add your `GOOGLE_API_KEY`.

## ▶️ How to Run
1.  **Start the API Server:**
    ```bash
    uvicorn main:app --reload
    ```
2.  **Access the API:**
    -   Open your browser and go to **http://127.0.0.1:8000/docs**.
    -   Use the interactive Swagger UI to test the `/ask` endpoint.

