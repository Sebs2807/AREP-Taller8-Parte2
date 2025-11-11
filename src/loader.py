from langchain_community.document_loaders import DirectoryLoader, TextLoader

def load_documents(directory_path: str):
    loader = DirectoryLoader(directory_path, glob="**/*.txt", loader_cls=TextLoader)
    documents = loader.load()
    print(f"[LOADER] Documentos cargados: {len(documents)}")
    return documents
