import fitz
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    full_text = ""
    tables = []
    for page in doc:
        full_text += page.get_text("text")+"\n"

        for block in page.get_text("blocks"):
            if "table" in block:
                tables.append(block)
    
    return{
        "text": full_text,
        "tables": tables
    }

