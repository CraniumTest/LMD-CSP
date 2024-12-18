from textblob import TextBlob
import matplotlib.pyplot as plt

def analyze_feedback(feedback_text):
    analysis = TextBlob(feedback_text)
    return {
        'polarity': analysis.sentiment.polarity,
        'subjectivity': analysis.sentiment.subjectivity
    }

def visualize_sentiment(analyses):
    polarities = [analysis['polarity'] for analysis in analyses]
    plt.hist(polarities, bins=10)
    plt.title("Sentiment Polarity Distribution")
    plt.xlabel("Polarity")
    plt.ylabel("Frequency")
    plt.show()
