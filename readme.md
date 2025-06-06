Document Q&A AI Agent
This project is an enterprise-ready AI agent that provides document-based question answering and academic research retrieval. It leverages open LLM APIs for intelligent query handling while optimizing response accuracy.
Features
- Multi-PDF ingestion – Allows users to upload multiple documents for processing.
- Structured extraction – Preserves tables, equations, and metadata for better content analysis.
- Optimized retrieval – Uses advanced ranking techniques to provide the most relevant answers.
- ArXiv research integration – Searches and summarizes academic papers using AI-powered query refinement


Setup Instructions
1. Install Dependencies
Run the following command to install required libraries:
pip install -r requirements.txt

Ensure API keys are stored in a .env file:
TOGETHER_API_KEY="your-api-key"

2. Run the Application
Launch the Document Q&A Agent interface with:
streamlit run app.py

3. Upload PDFs and Ask Questions
- Click "Upload PDFs" and select multiple documents.
- Enter a question related to the uploaded content.
- Receive precise answers with enhanced retrieval techniques.

4. Search for ArXiv Papers
- Enter a search term or description.
- Use AI-powered query refinement to improve search accuracy.
- Retrieve relevant academic research papers.

Project Structure
/docqna-agent
├── ingestion.py         # Multi-PDF ingestion and vector embedding
├── pdf_parser.py        # Structured document extraction
├── retrieval.py         # Optimized query handling
├── arxiv_lookup.py      # ArXiv search and AI-powered query refinement
├── app.py               # Streamlit-based user interface
├── requirements.txt     # Dependencies for installation
├── README.md            # Documentation

Demonstration
A video demonstration showcasing the functionality of the AI agent is available. [Provide link to recorded walkthrough]


Enterprise-Grade Enhancements
- Advanced embedding models ensure high retrieval accuracy.
- Multi-document processing improves scalability.
- Context-aware response generation enhances relevance.
- API security through environment variable management.


Next Steps
- Test multi-document retrieval with large datasets.
- Improve structured extraction for tables and figures.
- Enhance retrieval ranking based on custom user queries.
- Implement additional error-handling mechanisms.
