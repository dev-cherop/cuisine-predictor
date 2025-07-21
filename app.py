from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your pickled model once
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expecting a JSON array of selected ingredient indices from client
        selected_indices = request.json.get("ingredients")  # List of ints

        # Create input vector: 380-length zero array, mark selected indices as 1
        input_vector = np.zeros(380)
        for idx in selected_indices:
            input_vector[int(idx)] = 1

        input_vector = input_vector.reshape(1, -1)  # reshape for model

        prediction = model.predict(input_vector)[0]

        return {"prediction": prediction}

    except Exception as e:
        return {"error": str(e)}, 400

if __name__ == "__main__":
    app.run(debug=True)
