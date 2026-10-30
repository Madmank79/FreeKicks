from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from pathlib import Path
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = Path("leaderboard.json")

def load_scores():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_scores(scores):
    with open(DATA_FILE, "w") as f:
        json.dump(scores, f, indent=2)

@app.route("/")
def home():
    return "Cosmic Free Kicks Leaderboard is running!"

@app.route("/api/leaderboard", methods=["GET"])
def get_leaderboard():
    scores = load_scores()
    # Highest score first
    scores = sorted(scores, key=lambda x: (x.get("score", 0), x.get("goals", 0)), reverse=True)
    return jsonify(scores[:20])

@app.route("/api/leaderboard", methods=["POST"])
def submit_score():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data received"}), 400

    name = str(data.get("name", "Anonymous")).strip()[:20]
    score = int(data.get("score", 0))
    goals = int(data.get("goals", 0))

    if score <= 0:
        return jsonify({"error": "Score must be higher than 0"}), 400

    scores = load_scores()

    new_entry = {
        "name": name or "Anonymous",
        "score": score,
        "goals": goals,
        "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    }

    scores.append(new_entry)
    save_scores(scores)

    return jsonify({"success": True, "message": "Score saved!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
