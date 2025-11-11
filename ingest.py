# Ingest pipeline 
from src.loader import load_documents
from src.splitter import split_documents
from src.vectorstore import get_vectorstore

def ingest():
    documents = load_documents("data/documents")
    chunks = split_documents(documents)
    vectorstore = get_vectorstore()
    vectorstore.add_documents(chunks)
    print(f"[INGEST] {len(chunks)} documentos almacenados en Pinecone.")

if __name__ == "__main__":
    ingest()
