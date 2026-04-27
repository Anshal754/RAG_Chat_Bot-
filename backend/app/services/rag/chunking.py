from pypdf import PdfReader
import docx


# ==============================
# 🔹 EXTRACT TEXT
# ==============================
def extract_text(file_path: str) -> str:
    if file_path.endswith(".pdf"):
        reader = PdfReader(file_path)
        return "\n".join([page.extract_text() or "" for page in reader.pages])

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file format")


# ==============================
# 🔹 SMART CHUNKING (FAST + BETTER)
# ==============================
def chunk_text(text: str, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size

        chunk = text[start:end]

        # try to end at sentence boundary (cleaner chunks)
        last_period = chunk.rfind(".")
        if last_period != -1 and last_period > chunk_size * 0.5:
            chunk = chunk[:last_period + 1]

        chunks.append(chunk.strip())

        start += chunk_size - overlap

    return chunks