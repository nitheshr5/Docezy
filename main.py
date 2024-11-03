from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import file_storage  # for S3 uploads
import models
import nlp_processing  # for document querying
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload/")
async def upload_document(file: UploadFile, db: Session = Depends(get_db)):
    # Read file content and upload to S3
    content = await file.read()
    file_url = file_storage.upload_to_s3(content, file.filename)
    
    # Store file metadata in the database
    doc = models.Document(file_url=file_url)
    db.add(doc)
    db.commit()
    
    return {"file_url": file_url}

@app.post("/query/")
def query_document(query: str, db: Session = Depends(get_db)):
    documents = db.query(models.Document).all()
    # Perform NLP query on documents
    answer = nlp_processing.query_with_rag(query, documents)
    return {"answer": answer}

@app.get("/documents/", response_model=List[models.Document])
def get_documents(db: Session = Depends(get_db)):
    documents = db.query(models.Document).all()
    return documents
