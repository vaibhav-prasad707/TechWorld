import pandas as pd
import re

df = pd.read_csv('ai_business_news_updated.csv')

df.dropna(how = 'all',inplace = True)

df.dropna(subset=['Title', 'URL', 'Summary'], inplace=True)

def clean_url(url):
    if pd.isna(url):
        return None
    url = url.strip()
    matches = re.findall(r'https?://[^\s]+', url)
    return matches[0] if matches else None

df['URL'] = df['URL'].apply(clean_url)

df['Title'] = df['Title'].astype(str).str.strip()
df['Summary'] = df['Summary'].astype(str).str.strip()

df.dropna(subset=['Title', 'URL', 'Summary'], inplace=True)

df.to_csv('ai_business_news_updated.csv', index=False, encoding='utf-8')

print(df.head)