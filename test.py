import requests
from bs4 import BeautifulSoup
import json

def get_quotes(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []

    for quote in soup.select('.quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes

def main():
    base_url = 'https://quotes.toscrape.com/'
    all_quotes = []
    page = 1

    while True:
        url = f'{base_url}page/{page}/'
        quotes = get_quotes(url)
        if not quotes:
            break
        all_quotes.extend(quotes)
        page += 1

    with open('quotes.json', 'w') as f:
        json.dump(all_quotes, f, indent=4)

if __name__ == '__main__':
    main()
