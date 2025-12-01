📌 Fake News Classifier — Full Stack Machine Learning Project

A complete End-to-End Fake News Detection System built using:

Python (EDA, Data Cleaning, Training)

Scikit-Learn (TF-IDF + Logistic Regression)

Flask (REST API)

React + Vite (Frontend Web App)

Glassmorphism + Neon UI Design

This project predicts whether a news article is REAL or FAKE using machine learning and a clean, modern UI.

🚀 Features
🔍 Machine Learning

Full EDA + Cleaning in Jupyter Notebook

Uses Headline + Body text

Cleaned dataset → clean_fake_news.csv

TF-IDF Vectorizer (100k features)

Logistic Regression with balanced class weights

Saves model as .pkl files

🖥️ Backend (Flask API)

/api/predict endpoint

Loads trained model + vectorizer

Applies same cleaning pipeline as training

Returns:

{
  "prediction": "REAL" | "FAKE",
  "confidence": 0.89
}

🌐 Frontend (React + Vite)

Modern, glowing glassmorphism design

Dark neon gradient theme

Input fields for Headline + Body

Displays prediction with confidence score

Fully responsive design

📂 Project Structure
fake-news-classifier/
│
├── eda/
│   └── fake_news_eda.ipynb        # EDA + preprocessing notebook
│
├── backend/
│   ├── app.py                     # Flask API
│   ├── model.py                   # Model loader + predict function
│   ├── train_model.py             # Training script
│   ├── clean_function.py          # Text cleaning function
│   ├── saved_model/
│   │     ├── model.pkl
│   │     └── vectorizer.pkl
│   └── data/
│         ├── data.csv             # Raw dataset
│         └── clean_fake_news.csv  # Cleaned dataset (generated)
│
└── frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── App.jsx
        ├── App.css                # Neon/glass UI
        ├── main.jsx
        └── index.css

📊 Dataset Used

Kaggle Fake News Dataset with these columns:

URLs	Headline	Body	Label

0 = REAL

1 = FAKE

Notebook cleans this and creates:

clean_fake_news.csv

🔧 How to Run the Project
1️⃣ Backend Setup
Install dependencies:
cd backend
pip install -r requirements.txt

Train the model:
python train_model.py


This generates:

saved_model/model.pkl
saved_model/vectorizer.pkl

Start Flask API:
python app.py


Backend runs at:

http://localhost:5000

2️⃣ Frontend Setup
Install dependencies:
cd frontend
npm install

Start frontend:
npm run dev


Frontend runs at:

http://localhost:5173

🧠 How the Model Works

Combine Headline + Body

Apply cleaning:

lowercase

remove URLs

remove HTML

remove punctuation

normalize whitespace

Transform with TF-IDF (100k features)

Predict using Logistic Regression

Return prediction + confidence

🎨 UI Highlights

Futuristic neon glow

Smooth fade animations

Glassmorphism card

Tech-UI gradient background

Animated input focus ring

📸 Screenshots

(You can add your screenshots here)

![App Screenshot](screenshot.png)

📦 Technologies Used
Machine Learning

Python

Pandas, NumPy

Scikit-Learn

TF-IDF Vectorizer

Backend

Flask

Flask-CORS

joblib

Frontend

React

Vite

Axios

Neon/glass UI CSS

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

📜 License

This project is licensed under the MIT License.