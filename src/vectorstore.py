# Vectorstore file 
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone as PineconeVectorStore
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.config import (
    OPENAI_API_KEY,
    PINECONE_API_KEY,
    PINECONE_ENVIRONMENT,
    PINECONE_INDEX_NAME
)
from pinecone import Pinecone, ServerlessSpec
import os

def get_vectorstore():
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    pc = Pinecone(api_key=PINECONE_API_KEY)

    if PINECONE_INDEX_NAME not in [idx["name"] for idx in pc.list_indexes()]:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    index = pc.Index(PINECONE_INDEX_NAME)
    vectorstore = PineconeVectorStore(index=index, embedding=embeddings, text_key="text")
    return vectorstore
