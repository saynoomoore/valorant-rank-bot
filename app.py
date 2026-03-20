from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Valorant rank bot is working!"

@app.route("/api/rank")
def rank():
    region = "eu"
    name = "saynoomoore"
    tag = "ttv"

    url = f"https://api.henrikdev.xyz/valorant/v2/mmr/{region}/{name}/{tag}"

    try:
        r = requests.get(url, timeout=10)
        data = r.json()

        current_rank = data["data"]["current_data"]["currenttierpatched"]
        rr = data["data"]["current_data"]["ranking_in_tier"]
        highest_rank = data["data"]["highest_rank"]["patched_tier"]

        return f"{name} — {current_rank} [{rr}/100] | Highest Rank: {highest_rank}"
    except:
        return "Не удалось получить ранг Valorant"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
