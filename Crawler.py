import requests
from bs4 import BeautifulSoup, SoupStrainer



r = requests.get('https://www.wired.com/?_sp=b3392f00-2e3a-4c46-9a06-262d87c11ace.1748318789247')
print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')

headlines = soup.find_all('h2')
headlines_2 = soup.find_all('h3')
articles = soup.find_all('a',class_= 'BaseWrap-sc-gjQpdd BaseText-ewhhUZ SectionTitleHed-dKqZet bVCFRm cMsmZO gwAAxP')

for link in BeautifulSoup(r.text, 'html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        print(link['href'])

print("All the H2 ones\n", len(headlines))
for headline in headlines:
    print(headline.text.strip())
print("All the H3 ones\n", len(headlines_2))
for headline in headlines_2:
    print(headline.text.strip())



