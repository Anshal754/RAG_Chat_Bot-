from backend.app.services.rag.embedding_service import model
from transformers import pipeline


# ==========================================
# MODELS
# ==========================================

# Main model (fast + stable)
generator_fast = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

# Fallback model
generator_fallback = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


# ==========================================
# BAD ANSWER DETECTION
# ==========================================

def is_bad_answer(ans):
    ans = ans.lower().strip()

    bad_phrases = [
        "i don't know",
        "not mentioned",
        "cannot answer",
        "unknown",
        "no information"
    ]

    return (
        len(ans) < 50
        or any(x in ans for x in bad_phrases)
    )


# ==========================================
# QUERY RAG
# ==========================================

def query_rag(vector_store, query: str, mode: str = "fast"):

    try:
        # Encode question
        query_embedding = model.encode([query])


        # ==================================
        # FAST MODE
        # ==================================
        if mode == "fast":

            retrieved_chunks = vector_store.search(
                query_embedding,
                k=5
            )

            best_chunks = retrieved_chunks[:3]


        # ==================================
        # ACCURATE MODE
        # ==================================
        else:

            retrieved_chunks = vector_store.search(
                query_embedding,
                k=8
            )

            # remove tiny/weak chunks
            retrieved_chunks = [
                c for c in retrieved_chunks
                if len(c.strip()) > 100
            ]

            best_chunks = retrieved_chunks[:4]


        # keep context compact for speed
        best_chunks = [
            chunk[:500]
            for chunk in best_chunks
        ]

        context = "\n\n".join(best_chunks)


        # ==================================
        # PROMPT
        # ==================================
        prompt = f"""
Use ONLY the context below to answer.

Rules:
- Answer directly.
- Be concise but informative.
- Use the number of sentences based on the requrienment and based on users prompt .
- Do not invent facts.
- If missing information say:
I don't know.

Context:
{context}

Question:
{query}

Answer:
"""


        # ==================================
        # MAIN GENERATION
        # ==================================
        result = generator_fast(
            prompt,
            max_new_tokens=180,
            do_sample=False
        )

        answer = result[0]["generated_text"].strip()

        print("\nMAIN ANSWER:\n", answer)


        # ==================================
        # SMART FALLBACK
        # ==================================
        if mode == "accurate" and is_bad_answer(answer):

            print("Fallback triggered...")

            result = generator_fallback(
                prompt,
                max_new_tokens=220,
                do_sample=False
            )

            answer = result[0]["generated_text"].strip()


        return answer


    except Exception as e:
        return f"Error: {str(e)}"