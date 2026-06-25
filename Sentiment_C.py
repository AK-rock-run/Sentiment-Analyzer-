from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

# Create analyzer only once
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores["compound"]

    if compound >= 0.05:
        label = "Positive"
    elif compound <= -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return label, compound


def display_result(text, label, score,num):
    print("-" * 40)
    print("Sr number :", num)
    print("Review    :", text)
    print("Sentiment :", label)
    print("Score     :", score)


file_path = "review.txt"

# Read all reviews
with open(file_path, "r") as file:
    reviews = file.readlines()

# Store all results here
results = []
num=0

# Process every review
for review in reviews:

    review = review.strip()

    if review == "":
        continue

    label, score = analyze_sentiment(review)
    num+=1

    # Display on terminal
    display_result(review, label, score,num)

    # Store for JSON
    results.append({
        "review": review,
        "sentiment": label,
        "score": score
    })

# Write JSON only once
with open("result.json", "w") as json_file:
    json.dump(results, json_file, indent=4)

print("\nResults successfully saved to result.json")
print("="*40)
positive = 0
negative = 0
neutral = 0
total_score = 0

for item in results:
    if item["sentiment"] == "Positive":
        positive += 1
    elif item["sentiment"] == "Negative":
        negative += 1
    else:
        neutral += 1

    total_score += item["score"]

total_reviews = len(results)
average_score = total_score / total_reviews if total_reviews > 0 else 0
print("=" * 40)
print("SUMMARY")
print("=" * 40)
print(f"Total reviews : {total_reviews}")
print(f"Positive      : {positive}")
print(f"Negative      : {negative}")
print(f"Neutral       : {neutral}")
print(f"Average score : {average_score:.3f}")

output = {
    "summary": {
        "total_reviews": total_reviews,
        "positive": positive,
        "negative": negative,
        "neutral": neutral,
        "average_score": round(average_score, 3)
    },
    "results": results
}

with open("result.json", "w") as json_file:
    json.dump(output, json_file, indent=4)
