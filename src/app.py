# App CLI 
from rag_agent import ask

def main():
    print("🚀 Bienvenido al RAG con LangChain + Pinecone + OpenAI")
    while True:
        query = input("\nEscribe tu pregunta (o 'salir'): ")
        if query.lower() in ["salir", "exit", "quit"]:
            break
        ask(query)

if __name__ == "__main__":
    main()
