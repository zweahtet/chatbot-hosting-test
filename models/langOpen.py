import os

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embedding_function = OpenAIEmbeddings()

def initialize_index(index_name):  
    if os.path.exists(index_name):
        return FAISS.load_local("./", embedding_function, index_name=index_name)
    else:
        faiss = FAISS.from_texts("./data/calregs.txt")
        faiss.save_local("./")
        return faiss
