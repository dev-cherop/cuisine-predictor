# Cuisine prediction

**Author:** dev-cherop  


---

## Project Overview
This Flask web application allows users to make predictions based on a pre-trained machine learning model (`model.pkl`). Users select input features (ingredients), which are converted into a binary vector and fed into the model to get predictions.

---

## Features
- Web interface for selecting input features.
- Real-time predictions via Flask API.
- Input validation and error handling.
- Lightweight and easy-to-extend architecture.

---

---

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/dev-cherop/FlaskModelProject.git
cd FlaskModelProject

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py


Access the app:
Open http://127.0.0.1:5000 in your browser.

Usage

1.Open the web interface.

2.Select the ingredients/features from the available list.

3.Click the predict button.

4.View the prediction returned by the model.
