#pip install textblob

from textblob import TextBlob

emails = [
    "Thank you for the great service. I am very satisfied",
    "I am disappointed with the product quality.",
    "Your team's support was outstanding. Thank you",
    # Add more example emails here
]

for email in emails:
    blob = TextBlob(email)
    sentiment = blob.sentiment

    if sentiment.polarity > 0:
        sentiment_label = "Positive"
    elif sentiment.polarity < 0:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    print(f"Email: {email}")
    print(f"Sentiment: {sentiment_label}")
    print(f"Polarity: {sentiment.polarity}")
    print("-" * 50)
