from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Insurance RAG API")

class AskRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(req: AskRequest):
    # Skeleton — implement retrieval + Grok later
    return {
        "answer": "Skeleton response. Implement retrieval and Grok call.",
        "sources": []
    }

@app.get("/health")
def health():
    return {"status": "ok"}
