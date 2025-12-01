import pandas as pd
import joblib, os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

DATA_PATH = './backend/data/clean_fake_news.csv'
MODEL_DIR="saved_model"

os.makedirs(MODEL_DIR, exist_ok=True)

def train_and_save():
    df = pd.read_csv(DATA_PATH)

    X = df["clean_text"].astype(str).values
    y = df["Label"].astype(int).values

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(max_features=50000, stop_words="english")
    X_train_vec = vectorizer.fit_transform(X_train)

    model = LogisticRegression(max_iter=2000)
    model.fit(X_train_vec, y_train)

    X_test_vec = vectorizer.transform(X_test)
    preds = model.predict(X_test_vec)

    print("Accuracy:", accuracy_score(y_test, preds))
    print("Report:\n", classification_report(y_test, preds))

    joblib.dump(vectorizer, f"{MODEL_DIR}/vectorizer.pkl")
    joblib.dump(model, f"{MODEL_DIR}/model.pkl")

    print("Model saved!")

if __name__ == "__main__":
    train_and_save()
