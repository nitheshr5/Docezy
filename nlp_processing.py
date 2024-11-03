from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes import BM25Retriever

document_store = InMemoryDocumentStore()
retriever = BM25Retriever(document_store=document_store)

def index_documents(documents):
    document_store.write_documents(documents)

def query_with_rag(query):
    results = retriever.retrieve(query)
    return [result.content for result in results]


# from llama_index import LlamaIndex

# from crewai import AutoGen

# def query_with_rag(query, documents):
#     ll_index = LlamaIndex(documents)
#     agent = AutoGen(index=ll_index)
#     response = agent.query(query)
#     return response

