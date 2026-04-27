from sentence_transformers import SentenceTransformer
import numpy as np

# ==============================
# 🔹 LOAD EMBEDDING MODEL
# ==============================
model = SentenceTransformer("all-MiniLM-L6-v2")


# ==============================
# 🔹 SIMPLE VECTOR STORE
# ==============================
class VectorStore:
    def __init__(self):
        self.texts = []
        self.embeddings = []

    def add(self, chunks):
        new_embeddings = model.encode(chunks)

        self.texts.extend(chunks)
        self.embeddings.extend(new_embeddings)

    def search(self, query_embedding, k=4):
        similarities = []

        for i, emb in enumerate(self.embeddings):
            score = np.dot(query_embedding[0], emb) / (
                np.linalg.norm(query_embedding[0]) * np.linalg.norm(emb)
            )
            similarities.append((self.texts[i], score))

        # sort by similarity
        similarities = sorted(similarities, key=lambda x: x[1], reverse=True)

        return [text for text, _ in similarities[:k]]


# ==============================
# 🔹 GLOBAL INSTANCE
# ==============================
vector_store = VectorStore()