# 📄 Document Q&A AI Agent

This project is an enterprise-ready AI agent that provides intelligent document-based question answering and academic research retrieval. It leverages open LLM APIs for accurate and context-aware query resolution.

---

## 🚀 Features

- **Multi-PDF Ingestion**  
  Upload and process multiple documents simultaneously for comprehensive analysis.

- **Structured Extraction**  
  Accurately preserves tables, equations, and metadata for deep document understanding.

- **Optimized Retrieval**  
  Uses advanced embedding models and ranking algorithms to deliver the most relevant answers.

- **ArXiv Research Integration**  
  Searches and summarizes academic papers using AI-enhanced query refinement techniques.

---

## 🛠️ Setup Instructions

### 1. Install Dependencies
Run the following command to install required libraries:
```bash
pip install -r requirements.txt
Ensure your API key is stored securely in a .env file:
TOGETHER_API_KEY="your-api-key"

2. Launch the Application
Start the Streamlit interface using:
streamlit run app.py

3. Use the Document Q&A Interface
Click Upload PDFs to upload one or more documents.
Ask questions based on the uploaded content.
Get accurate, AI-generated answers using optimized retrieval.

4. Search ArXiv Academic Papers
Enter a research topic or description.
The system refines the query using AI.
View and explore relevant academic papers.

🧠 Project Structure
/docqna-agent
├── app.py               # Streamlit-based UI
├── ingestion.py         # Multi-PDF ingestion and vector embedding
├── pdf_parser.py        # Structured document content extraction
├── retrieval.py         # Intelligent question-answer retrieval
├── arxiv_lookup.py      # ArXiv search and query refinement
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation


📺 Demonstration
A walkthrough video showcasing the full functionality of the Document Q&A Agent is available:
👉 Demo Video Link (https://drive.google.com/file/d/1dpg8nDWsNT0IkvNRxsyeT00VewiYCVE-/view?usp=drive_link)

🏢 Enterprise-Grade Capabilities
High-precision embeddings for context-aware responses
Scalable multi-document processing
Integration with scientific literature databases (ArXiv)
API key security using .env environment variables
