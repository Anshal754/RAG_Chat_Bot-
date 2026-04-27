from fastapi import APIRouter, UploadFile, File
import shutil

from backend.app.services.rag.query_service import query_rag
from backend.app.services.rag.chunking import extract_text, chunk_text
from backend.app.services.rag.embedding_service import vector_store

router = APIRouter()


# ==============================
# 🔹 UPLOAD
# ==============================
@router.post("/upload")
def upload(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)
    chunks = chunk_text(text)

    vector_store.add(chunks)

    return {"message": "File processed successfully"}


# ==============================
# 🔹 QUERY
# ==============================
@router.post("/query")
def query(question: str, mode: str = "fast"):
    answer = query_rag(vector_store, question, mode)
    return {"answer": answer}