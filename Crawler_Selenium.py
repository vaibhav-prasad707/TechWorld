from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


urls = [
    "https://www.wired.com/category/business/", 
    "https://techcrunch.com/category/artificial-intelligence/"
]

keywords = ["ai", "artificial intelligence", "machine learning", "deep learning", "chatgpt", "openai", "llm", "generative ai"]


with open("ai_business_news_updated.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL", "Summary"])
    for url in urls:
        driver.get(url)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        if "wired" in url:
            articles = soup.select("a[href^='/story/']")
            for article in articles:
                title = article.get_text(strip=True)
                href = article.get("href")
                full_url = f"https://www.wired.com{href}" if "wired" in url else href
                summary_tag = article.find_next("p")
                summary = summary_tag.get_text(strip=True) if summary_tag else ""
                content = f"{title} {summary}".lower()
                if any(keyword in content for keyword in keywords):
                    writer.writerow([title, full_url, summary])
                    print(f"Saved: {title} - {full_url}")
        
        elif "techcrunch" in url:
            h3_tags = soup.find_all("h3")
            for h3 in h3_tags:
                title = h3.get_text(strip=True)
                href = h3.find("a")["href"] if h3.find("a") else ""
                full_url = f"https://techcrunch.com{href}" if href else ""
                summary_tag = h3.find_next("p")
                summary = summary_tag.get_text(strip=True) if summary_tag else ""
                content = f"{title} {summary}".lower()
                if any(keyword in content for keyword in keywords):
                    writer.writerow([title, full_url, summary])
                    print(f"Saved: {title} - {full_url}")


driver.quit()
