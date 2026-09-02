from flask import Flask, render_template, request, jsonify

from prompt_engine import create_prompt
from ollama_service import generate_response


app = Flask(__name__)


# -------------------------
# Home Page
# -------------------------

@app.route("/")
def home():

    return render_template("index.html")


# -------------------------
# Generate Response
# -------------------------

@app.route("/api/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        module = data.get(
            "module",
            "Code Generation & Explanation"
        )

        strategy = data.get(
            "strategy",
            "Zero-Shot"
        )

        task = data.get(
            "task",
            ""
        ).strip()

        examples = data.get(
            "examples",
            ""
        )

        if not task:

            return jsonify({
                "error":
                "Engineering task is required."
            }), 400


        # Construct prompt

        prompt = create_prompt(
            module,
            strategy,
            task,
            examples
        )


        # Send to Ollama

        result = generate_response(
            prompt
        )


        return jsonify({

            "success": True,

            "module": module,

            "strategy": strategy,

            "prompt": prompt,

            "response":
                result["response"],

            "latency":
                result["latency"],

            "tokens":
                result["tokens"],

            "model":
                result["model"]

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        }), 500


# -------------------------
# Health Check
# -------------------------

@app.route("/api/health", methods=["GET"])
def health():

    return jsonify({

        "status": "running",

        "service": "PromptCraft",

        "llm": "Ollama"

    })


# -------------------------
# Run Flask
# -------------------------

if __name__ == "__main__":

    print()
    print("=" * 50)
    print("       PROMPTCRAFT")
    print("LLM-Powered Engineering Assistant")
    print("=" * 50)
    print("LLM Backend : Ollama")
    print("Server      : http://127.0.0.1:5000")
    print("=" * 50)
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )