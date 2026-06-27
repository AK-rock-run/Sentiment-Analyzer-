from datasets import load_dataset
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import accuracy_score
import joblib

#--------------Dataset
dataset = load_dataset("stanfordnlp/imdb")
texts = dataset["train"]["text"]
labels = dataset["train"]["label"]

#-------------Cleaning
cleaned_texts = []

for text in texts:
    text = re.sub(r'<.*?>', '', text) # remove html tage 
    text = text.lower()
    cleaned_texts.append(text)

#print(cleaned_texts[0])
#print(labels[0])

#-------------Train-test Split 
X_train, X_test, y_train, y_test = train_test_split(
    cleaned_texts, labels, test_size=0.2, random_state=42
)

#-------------TF IDF
vectorizer = TfidfVectorizer(max_features=10000)
# matrix = vectorizer.fit_transform(cleaned_texts)
X_train_tfidf = vectorizer.fit_transform(X_train)  
X_test_tfidf = vectorizer.transform(X_test) 
# print(matrix.toarray())
# print(vectorizer.get_feature_names_out())

#--------------logistic regression 
model=LogisticRegression()
model.fit(X_train_tfidf,y_train) # learns

#--------------store
joblib.dump(model, "sentiment_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

#---------------prediction
y_pred = model.predict(X_test_tfidf) # uses what it learn

#---------------Acuracy
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")


#---------------classification report 
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred, target_names=["Negative", "Positive"]))

def predict_review(text):
    text = re.sub(r'<.*?>', '', text)
    text = text.lower()
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    probability = model.predict_proba(vector)[0]
    label = "Positive" if prediction == 1 else "Negative"
    confidence = probability[prediction]
    print(f"Sentiment  : {label}")
    print(f"Confidence : {confidence*100:.2f}%")

predict_review("This movie was absolutely brilliant, I loved every moment of it!")
predict_review("Terrible film, complete waste of time.")

