import pandas as pd
from transformers import pipeline

df = pd.read_csv("ai_business_news_updated.csv")

sentiment_pipeline = pipeline("sentiment-analysis", model = 'distilbert-base-uncased-finetuned-sst-2-english')

df['text'] = df['Title'].fillna('') + ' ' + df['Summary'].fillna('')

sentiments = sentiment_pipeline(df['text'].tolist(), truncation = True)

df['Sentiment'] = [sent['label'] for sent in sentiments]
df['Confidence'] = [sent['score'] for sent in sentiments]

df.to_csv("ai_business_news_with_sentiment.csv", index=False, encoding='utf-8')

print(df[['Title', 'URL', 'Sentiment', 'Confidence']].head())

