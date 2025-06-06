import os
from dotenv import load_dotenv

from langchain_core.runnables import RunnableSequence
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_together import Together
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

load_dotenv()
llm = Together(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    api_key=os.getenv("TOGETHER_API_KEY"), max_tokens=512
)

template = """Use the following context to answer the user's question.
If the answer is not in the context, just say you don't know.

Context:
{context}

Question:
{question}

Answer:"""

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)

chain = prompt | llm

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

def query_agent(query):
    context_docs_with_scores = db.similarity_search_with_score(query, k=5)
    context_docs_with_scores = sorted(context_docs_with_scores, key=lambda x: x[1], reverse=True)
    context = "\n\n".join(doc.page_content for doc, score in context_docs_with_scores)
    return chain.invoke({"context": context, "question": query})



