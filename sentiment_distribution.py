import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ai_business_news_with_sentiment.csv")

print("Available Sentiments:", df['Sentiment'].unique())

sentiment_counts = df['Sentiment'].value_counts()

plt.figure(figsize=(10, 6))
sentiment_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Sentiment Distribution of AI Business News')
plt.xlabel('Sentiment')
plt.ylabel('Number of Articles')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('sentiment_distribution.png')
plt.show()