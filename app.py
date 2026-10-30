from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to SWYNEX API Project!",
        "status": "success"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "API is running successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)