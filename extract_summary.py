import csv
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm  # For progress bar


with open("ai_business_news.csv", newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    articles = list(reader)

updated_articles = []

for article in tqdm(articles):
    url = article["URL"]
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        meta_desc = soup.find("meta", attrs={"property": "og:description"})
        summary = meta_desc["content"] if meta_desc else "Summary not found"
    except Exception as e:
        summary = f"Error fetching summary: {e}"

    updated_articles.append({
        "Title": article["Title"],
        "URL": article["URL"],
        "Summary": summary
    })

# Save to new CSV
with open("ai_business_news_with_summaries.csv", "w", newline='', encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Title", "URL", "Summary"])
    writer.writeheader()
    writer.writerows(updated_articles)

print("Done! Summaries extracted and saved.")
