from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load model once at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

FEATURE_COUNT = 380  # total possible ingredients

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        selected_indices = data.get("ingredients", [])

        if not selected_indices:
            return jsonify({"error": "No ingredients provided"}), 400

        # Create binary input vector
        input_vector = np.zeros(FEATURE_COUNT)
        for idx in selected_indices:
            if 0 <= idx < FEATURE_COUNT:
                input_vector[idx] = 1

        prediction = model.predict([input_vector])[0]

        return jsonify({"prediction": prediction})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
