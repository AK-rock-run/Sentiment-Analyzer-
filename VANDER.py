from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# input
text = input("Enter your review: ")
c=1

# get scores
scores = analyzer.polarity_scores(text)

# decision based on compound score
compound = scores['compound']

if compound >= 0.05:
    print("Positive ")
elif compound <= -0.05:
    print("Negative ")
else:
    print("Neutral ")
