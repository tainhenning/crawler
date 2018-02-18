import requests
from bs4 import BeautifulSoup as bs

def trade_spider(max_pages):
    page = 0
    while page <= max_pages:
        url = 'https://majestic.com/reports/majestic-million?s=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = bs(plain_text, "lxml")
        for link in soup.findAll('a', {'rel':'nofollow'}):
            href = link.get('href')
        page += 100
trade_spider(999900)
