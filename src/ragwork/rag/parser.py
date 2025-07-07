import json

from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np
import os
import os
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
from sentence_transformers import SentenceTransformer
import pickle

def get_chunk(doc):
    doc_id=doc['metadata_header']['case_id']
    return [
        {"document_id": doc_id, "section_type": "summary", "text": doc["summary"]},
        {"document_id": doc_id, "section_type": "facts_of_case", "text": doc["facts_of_case"]},
        {"document_id": doc_id, "section_type": "plaintiff_arguments", "text": doc["plaintiff_arguments"]},
        {"document_id": doc_id, "section_type": "defendant_arguments", "text": doc["defendant_arguments"]},
        {"document_id": doc_id, "section_type": "verdict", "text": doc["verdict"]}
    ]


with open(r'C:\Users\hp\Documents\synbrains_trainee_works\ragwork\ragwork\mock_legal_data.json') as file:
    out=json.load(file)
    
print(out)
model = SentenceTransformer('all-MiniLM-L6-v2')
allchunk=[]
def retriever(chunks, query=None, top_k=3):
    texts = [c['text'] for c in chunks]
    embeddings = model.encode(texts)
    return embeddings
for i in out:
    chunks=get_chunk(i)
    allchunk.extend(chunks)
embedding=retriever(allchunk)
with open(r'C:\Users\hp\Documents\synbrains_trainee_works\ragwork\ragwork\src\ragwork\embeddings.pkl', 'wb') as f:

        pickle.dump({'chunks': allchunk, 'embeddings': embedding}, f)

print(f"Saved {len(allchunk)} chunks ")

# Define retriever function


# Optional: print result
