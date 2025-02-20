from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 SensAI Live Dashboard is Running!"

@app.route("/status")
def status():
    return jsonify({"status": "running", "posts_made": 10, "dms_sent": 25})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
