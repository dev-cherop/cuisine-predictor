# Cuisine Predictor Web App 

A Flask-based web app that predicts the cuisine of a dish based on its ingredients.

##  Tech Stack
- Python, Flask
- Scikit-learn / Pandas (if applicable)
- Docker
- GitHub Actions (CI)

## Features
- Web form to input ingredients
- Predict cuisine using a trained ML model
- Containerized with Docker
- CI pipeline using GitHub Actions

## How to Run (Docker)
```bash
docker build -t cuisine-predictor .
docker run -p 5000:5000 cuisine-predictor
