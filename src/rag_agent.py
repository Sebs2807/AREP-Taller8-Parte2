# src/rag_agent.py
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from vectorstore import get_vectorstore
from config.config import TOP_K

def create_rag_agent():
    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # 🧩 Definimos el prompt base
    prompt = ChatPromptTemplate.from_template("""
    Usa el siguiente contexto para responder la pregunta del usuario.
    Si no sabes la respuesta, di "No tengo suficiente información para responder".

    Contexto:
    {context}

    Pregunta: {input}
    """)

    # 🧱 Creamos la cadena que combina los documentos recuperados
    combine_docs_chain = create_stuff_documents_chain(llm, prompt)

    # 🔗 Finalmente, la cadena completa de RAG
    retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

    return retrieval_chain


def ask(question: str):
    rag_agent = create_rag_agent()
    result = rag_agent.invoke({"input": question})

    print("\n[Respuesta]")
    print(result["answer"])
    print("\n[Fuentes]")
    for doc in result["context"]:
        print("-", doc.metadata.get("source", "sin fuente"))
