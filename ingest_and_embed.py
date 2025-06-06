import os
os.environ["USE_TF"] = "0"
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from ingestion.pdf_parser import extract_text_from_pdf
from dotenv import load_dotenv

load_dotenv()

def ingest_pdfs_to_vectorstore(pdf_paths, persist_directory="chroma_db"):
    all_chunks = []
    for pdf_path in pdf_paths:
        doc = extract_text_from_pdf(pdf_path)
        text = doc["text"]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = text_splitter.split_text(text)
        all_chunks.extend(chunks)  

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_texts(all_chunks, embeddings, persist_directory=persist_directory)

    print(f"Ingested {len(all_chunks)} chunks across {len(pdf_paths)} PDFs into vectorstore.")

    



