from flask import Flask, request, jsonify, send_from_directory
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Get the API key from .env
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("ANTHROPIC_API_KEY is not set")

client = Anthropic(api_key=api_key)


@app.route("/")
def home():
    return send_from_directory("static", "Lead triage app.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    leads = data.get("leads", [])

    if not leads:
        return jsonify({
            "error": "No leads were provided"
        }), 400

    prompt = f"""
You are scoring inbound sales leads for buyer intent based on free-text notes from a prior conversation.

For EACH item below, return an intent score from 0-100
(100 = urgent, budget-approved, ready to buy now;
0 = clearly not a buyer).

Also return:

- a one-sentence reason under 20 words
- whether this note reveals the lead is NOT a real buyer at all
- disqualify_flag
- a short disqualify_reason if true

Examples of disqualified leads include:
- job seeker
- investor
- recruiter
- student
- competitor
- explicit non-buyer

Return ONLY a JSON array.

Do not use markdown fences.
Do not include a preamble.

Use exactly this shape:

[
    {{
        "lead_id": "ID",
        "intent_score": 0,
        "reason": "Short reason",
        "disqualify_flag": false,
        "disqualify_reason": ""
    }}
]

Leads:

{leads}
"""

    try:

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=2000,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        # Convert Anthropic's response into the format
        # expected by your JavaScript.
        return jsonify({
            "content": [
                {
                    "type": "text",
                    "text": response.content[0].text
                }
            ]
        })

    except Exception as e:

        print("Anthropic API error:", e)

        return jsonify({
            "error": "Unable to analyze leads"
        }), 500


if __name__ == "__main__":
    app.run(debug=True)