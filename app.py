import streamlit as st
from dotenv import load_dotenv
import arxiv_lookup
import os
import ingest_and_embed
import agent

load_dotenv()

st.set_page_config(page_title="Document Q&A Agent", layout="wide")
st.title("📄 Document Q&A Agent ")

uploaded_files = st.file_uploader("Upload pdfs to ingest", type=["pdf"], accept_multiple_files=True)
if uploaded_files:
    pdf_paths = []
    os.makedirs("uploaded_files", exist_ok=True)
    for uploaded_file in uploaded_files:
        pdf_path = os.path.join("uploaded_files", uploaded_file.name)
        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())  # Save file correctly
        pdf_paths.append(pdf_path)
    st.success(f"Uploaded {len(uploaded_files)} PDFs! Processing...")
    ingest_and_embed.ingest_pdfs_to_vectorstore(pdf_paths)  
    st.success("Ingestion completed! You can now ask questions.")

query = st.text_input("Ask your question here:")
if query:
    with st.spinner("Getting answer..."):
        answer = agent.query_agent(query)
    st.markdown(f"**Answer:** {answer}")

st.markdown("---")
st.subheader("Search arXiv papers")
search_query = st.text_input("Search query for arXiv:", key="arxiv")
use_ai_refinement = st.checkbox("Use AI-powered query refinement")

if search_query:
    with st.spinner("Searching arXiv..."):
        if use_ai_refinement:
           st.markdown(arxiv_lookup.functional_lookup(search_query)) 
        else:
            st.markdown(arxiv_lookup.search_arxiv(search_query))