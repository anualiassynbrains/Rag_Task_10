# query_engine.py
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
import pickle
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from rag.prompts import respprompt  # Define respprompt = "Query: {query}\n\nContext:\n{context}\n\nAnswer:"

load_dotenv()

# Load embedding model and LLM once
model = SentenceTransformer('all-MiniLM-L6-v2')
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name='llama3-8b-8192')


class Retriever:
    def __init__(self, index_path):
        self.index_path = index_path
        self.chunks = []
        self.embeddings = None
        self.load_index()

    def load_index(self):
        with open(self.index_path, 'rb') as f:
            data = pickle.load(f)
        self.chunks = data['chunks']
        self.embeddings = data['embeddings']

    def retrieve(self, query, top_k=3):
        query_embedding = model.encode([query])
        sims = cosine_similarity(query_embedding, self.embeddings)[0]
        top_indices = sims.argsort()[::-1][:top_k]
        retrieved_chunks = [self.chunks[i] for i in top_indices]
        scores = [sims[i] for i in top_indices]
        return retrieved_chunks, scores

    def get_response(self, retrieved_chunks, query):
        context = "\n\n".join(
            [f"[{chunk['document_id']} - {chunk['section_type']}]\n{chunk['text']}" for chunk in retrieved_chunks]
        )
        prompt = respprompt.format(query=query, context=context)
        response = llm.invoke(input=prompt)
        return response.content.strip()


def run_query(query: str, index_path: str = None):
    index_path=r'C:\Users\hp\Documents\synbrains_trainee_works\ragwork\ragwork\src\ragwork\output\embeddings.pkl'
    retriever = Retriever(index_path)
    chunks, _ = retriever.retrieve(query)
    answer = retriever.get_response(chunks, query)
    return answer, chunks


if __name__ == "__main__":
    query = "What was the case about medical malpractice?"
    answer, chunks = run_query(query)
    print("\n=== LLM Answer ===\n")
    print(answer)
