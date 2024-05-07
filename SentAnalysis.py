from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Tuple

def analyse_sentiment(text: str, threshold: float = 0.05) -> Tuple[str, float]:
    # Create a SentimentIntensityAnalyzer object
    analyser = SentimentIntensityAnalyzer()

    # Analyze the sentiment of the text
    sentiment_scores = analyser.polarity_scores(text)

    # Get the overall compound score
    compound_score = sentiment_scores['compound']

    # Determine sentiment based on the compound score
    if compound_score >= threshold:
        sentiment = 'Positive'
    elif compound_score <= -threshold:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Return the sentiment category and compound score
    return sentiment, compound_score

# Read the text content from the input.txt file
with open('input.txt', 'r') as file:
    text_data = file.read()

# Perform sentiment analysis
sentiment, score = analyse_sentiment(text_data)

# Print the results
print(f"Text: {text_data}")
print(f"Sentiment: {sentiment}, Compound Score: {score:.4f}")
