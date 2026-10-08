# Resume upload

from fastapi import APIRouter, UploadFile, File
import os
import shutil


router = APIRouter()


# API Router
@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "uploaded": "File uploaded successfully"
    }