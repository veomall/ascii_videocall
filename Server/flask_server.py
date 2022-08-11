from flask import Flask
import json
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/<username>/<frame>")
def send(username, frame):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    try:
        data[username] = frame
    except:
        data += f"{username}: {frame}" 
    with open("data.json", "w") as write_file:
        json.dump(data, write_file)
    return "ok"


@app.route("/<username>")
def get(username):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)
    return data[username]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # app.run()
