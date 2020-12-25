import joblib

class Classifier(object):
    def __init__(self):
        self.vectorizer = joblib.load("news_vectorizer_dump.pkl")
        self.model = joblib.load("news_model_dump.pkl")
        self.target_names = ['Плохой отзыв', 'Хорошый отзыв']
    
    def get_name_by_label(self, label):
        try:
            return self.target_names[label]
        except:
            return "label error"

    def predict_text(self, text):
        try:
            vectorized = self.vectorizer.transform([text])
            return self.model.predict(vectorized)[0] 
        except:
            print("prediction error")
            return None 

    def get_result_message(self, text):
        prediction = self.predict_text(text)
        return self.get_name_by_label(prediction)

