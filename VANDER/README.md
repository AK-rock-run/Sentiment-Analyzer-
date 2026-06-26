# Sentiment Analysis using VADER

## 📌 Project Overview

This project performs sentiment analysis on customer reviews using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analyzer.

The program reads reviews from a text file, analyzes each review, classifies it as Positive, Negative, or Neutral, and stores the results in a JSON file. It also generates a summary containing the total number of reviews, sentiment counts, and the average sentiment score.

---

## 🚀 Features

* Read multiple reviews from a text file
* Analyze sentiment using the VADER library
* Classify reviews as:

  * Positive
  * Negative
  * Neutral
* Display results in the terminal
* Save results in JSON format
* Generate a sentiment summary

---

## 📂 Project Structure

```
Sentiment-Analysis-VADER/
│── main.py
│── review.txt
│── result.json
│── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* Python 3
* VADER Sentiment Analysis
* JSON

---

## 📥 Installation

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📄 Input

Store reviews inside `review.txt`.

Example:

```
The product is amazing.
Battery life is poor.
Worth every penny.
```

---

## 📊 Output

Terminal:

```
Review: The product is amazing.
Sentiment: Positive
Score: 0.82
```

JSON:

```json
{
    "summary": {
        "total_reviews": 3,
        "positive": 2,
        "negative": 1,
        "neutral": 0,
        "average_score": 0.31
    },
    "results": [
        {
            "review": "...",
            "sentiment": "...",
            "score": ...
        }
    ]
}
```

---

## 🎯 Future Improvements

* Build a Machine Learning version using Logistic Regression.
* Compare VADER with ML-based sentiment analysis.
* Add a graphical user interface.
* Support CSV datasets.
* Visualize sentiment distribution using charts.

---

## 👩‍💻 Author

Arya Pradeep Khamayacha

Mini Project – Sentiment Analysis using VADER
