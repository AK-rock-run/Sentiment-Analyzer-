# Machine Learning Based Sentiment Analysis

## Overview

This project implements a sentiment analysis system using Machine Learning. Unlike rule-based approaches, the model learns patterns from labeled data and predicts whether a review expresses a positive or negative sentiment.

The project uses the IMDB movie review dataset, preprocesses the text, converts it into numerical features using TF-IDF Vectorization, trains a Logistic Regression classifier, evaluates its performance, and saves the trained model for future predictions.

---

## Objectives

* Understand the complete Machine Learning workflow for text classification.
* Learn text preprocessing techniques.
* Convert textual data into numerical feature vectors.
* Train and evaluate a supervised learning model.
* Save the trained model for reuse without retraining.

---

## Technologies Used

* Python
* scikit-learn
* Hugging Face Datasets
* Joblib
* Regular Expressions (re)

---

## Project Workflow

1. Load the IMDB dataset from Hugging Face.
2. Extract reviews and sentiment labels.
3. Clean the review text by:

   * Removing HTML tags
   * Converting text to lowercase
4. Split the dataset into training and testing sets.
5. Convert text into TF-IDF feature vectors.
6. Train a Logistic Regression classifier.
7. Evaluate the model using the test dataset.
8. Display evaluation metrics.
9. Save the trained model and TF-IDF vectorizer using Joblib.
10. Load the saved model and predict the sentiment of new reviews.

---

## Machine Learning Pipeline

```text
IMDB Dataset
      │
      ▼
Text Cleaning
      │
      ▼
Train-Test Split
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Logistic Regression Training
      │
      ▼
Model Evaluation
      │
      ▼
Save Model (.pkl)
      │
      ▼
Predict Sentiment for New Reviews
```

---

## Dataset

The project uses the IMDB Movie Review Dataset available through the Hugging Face Datasets library.

Dataset characteristics:

* 50,000 labeled movie reviews
* Binary sentiment classification
* Labels:

  * 0 → Negative
  * 1 → Positive

The dataset is automatically downloaded when the program is executed.

---

## Model

Algorithm:

* Logistic Regression

Feature Extraction:

* TF-IDF Vectorizer

Training Strategy:

* 80% Training Data
* 20% Testing Data

---

## Evaluation

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Support

These metrics provide an overall understanding of the classifier's performance on unseen data.

---

## Output

The program displays:

* Model Accuracy
* Classification Report
* Predicted Sentiment
* Prediction Confidence

Example:

```text
Accuracy: 88.66%

Sentiment  : Positive
Confidence : 91.82%
```

---

## Saved Files

After training, the following files are generated:

* `sentiment_model.pkl` – Trained Logistic Regression model.
* `tfidf_vectorizer.pkl` – Trained TF-IDF vectorizer.

These files are reused for future predictions without retraining the model.

---

## Project Structure

```text
Machine_Learning/
│── ml_sentiment.py
│── requirements.txt
│── README.md
│── .gitignore
```

Generated after training:

```text
sentiment_model.pkl
tfidf_vectorizer.pkl
```

---

## Future Improvements

Possible enhancements include:

* Support for Neutral sentiment classification.
* Train on social media datasets.
* Perform sentiment analysis on tweets and product reviews.
* Experiment with other Machine Learning algorithms such as Naive Bayes, Support Vector Machines, and Random Forest.
* Improve preprocessing through stopword removal, stemming, and lemmatization.
* Replace TF-IDF with modern word embeddings or transformer-based models.

---

## Requirements

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python ml_sentiment.py
```

---

## Author

Arya Pradeep Khamayacha

Mini Project – Machine Learning Based Sentiment Analysis
