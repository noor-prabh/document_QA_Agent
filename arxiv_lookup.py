import arxiv
from langchain_together import Together

def search_arxiv(query):
    search = arxiv.Search(query=query, max_results=1)
    results = list(search.results())
    if results:
        paper = results[0]
        return f"{paper.title}\n\n{paper.summary}\n\nPDF: {paper.pdf_url}"
    return "No paper found."

def functional_lookup(query):
    llm_parser = Together(model="mistralai/Mixtral-8x7B-Instruct-v0.1")
    
    prompt = f"Convert this description into a search query: {query}"
    refined_query = llm_parser.invoke({"question": prompt}) 

    return search_arxiv(refined_query)