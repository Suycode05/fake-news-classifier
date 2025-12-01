from flask import Flask, jsonify,request
from flask_cors import CORS
from model import get_model
from clean_function import clean_text

app = Flask(__name__)
CORS(app)

@app.route("/api/predict", methods=["POST"])
def predict():
    data = request.get_json()
    headline = data.get("title", "")
    body = data.get("text", "")

    combined_raw = f"{headline} {body}"
    combined = clean_text(combined_raw)     # APPLY SAME CLEANING
    model = get_model()

    result = model.predict(combined)

    label_map={0:"REAL",1:"FAKE"}
    return jsonify({
        "prediction": label_map[result["label"]],
        "confidence": result["confidence"]
    })

if __name__ == "__main__":
    app.run(port=5000, debug=True)