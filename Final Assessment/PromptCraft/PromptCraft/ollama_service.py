from ollama import chat
import time

MODEL = "gemma3"


def generate_response(prompt):

    start = time.time()

    result = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    end = time.time()

    response = result["message"]["content"]

    latency = round(end - start, 2)

    tokens = result.get(
        "eval_count",
        "N/A"
    )

    return {
        "response": response,
        "latency": latency,
        "tokens": tokens,
        "model": MODEL
    }