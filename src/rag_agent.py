# RAG agent file 
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA
from src.vectorstore import get_vectorstore
from config.config import TOP_K

def create_rag_agent():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain

def ask(question: str):
    rag_agent = create_rag_agent()
    result = rag_agent.invoke({"query": question})
    print("\n[Respuesta]")
    print(result["result"])
    print("\n[Fuentes]")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source", "sin fuente"))
