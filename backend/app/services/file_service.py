import os
import uuid
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "data/uploads"
ALLOWED_EXTENSIONS = {".pdf", ".txt", ".docx"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


def validate_file(file: UploadFile):
    filename = file.filename
    ext = os.path.splitext(filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Invalid file type")

    return ext


async def save_file(file: UploadFile, user_id: str = "default"):
    ext = validate_file(file)

    user_dir = os.path.join(UPLOAD_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)

    file_id = str(uuid.uuid4())
    file_path = os.path.join(user_dir, f"{file_id}{ext}")

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="File too large")

    with open(file_path, "wb") as f:
        f.write(content)

    return {
        "file_id": file_id,
        "file_path": file_path,
        "filename": file.filename
    }