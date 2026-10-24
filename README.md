# Insurance Policy Assistant (RAG)

RAG assistant for public insurance policy documents using Grok, Chroma, FastAPI and Streamlit.

**Not financial advice.**

## Status

~20% complete. Folder structure, basic ingest skeleton, FastAPI /ask stub, docker-compose, and requirements.

## Next steps

- PDF loading with page metadata (pypdf)
- Chunking and embedding into Chroma (Grok embeddings)
- Scheduled ingestion for new files
- Full /ask with retrieval, citations, and "I don't know" handling
- Streamlit UI
- 30-question evaluation harness
