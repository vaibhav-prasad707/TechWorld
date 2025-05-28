from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.wired.com/category/business/")

time.sleep(5)
soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

keywords = ["ai", "artificial intelligence", "machine learning", "deep learning", "chatgpt", "openai", "llm", "generative ai"]

articles = soup.select("a[href^='/story/']")

with open("ai_business_news.csv", "w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "URL", "Summary"])

    for article in articles:
        title = article.get_text(strip=True)
        url = "https://www.wired.com" + article.get("href")
        summary_tag = article.find_next("p")  # Often next to <a>, adjust as needed
        summary = summary_tag.get_text(strip=True) if summary_tag else ""

        # Check for AI keywords in title or summary
        content = (title + " " + summary).lower()
        if any(keyword in content for keyword in keywords):
            writer.writerow([title, url, summary])

