import joblib
from clean_function import clean_text

class FakeNewsModel:
    def __init__(self):
        self.vectorizer = joblib.load("saved_model/vectorizer.pkl")
        self.model = joblib.load("saved_model/model.pkl")

    def predict(self, text):
        text = clean_text(text)
        X=self.vectorizer.transform([text])
        pred=self.model.predict(X)[0]
        proba=self.model.predict_proba(X)[0][pred]
        return {"label":int(pred),"confidence":float(proba)}
    
_model=None

def get_model():
    global _model
    if _model is None:
        _model=FakeNewsModel()
    return _model