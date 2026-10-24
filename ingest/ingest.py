"""Skeleton for PDF ingestion into Chroma."""
from pathlib import Path

DOCS_DIR = Path("docs")

def load_pdfs():
    pdfs = list(DOCS_DIR.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs (skeleton — implement pypdf + chunking later)")
    return pdfs

if __name__ == "__main__":
    load_pdfs()
