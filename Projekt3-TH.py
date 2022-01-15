# Projekt 3 – Tomas H.
import requests
import bs4



getr = requests.get('https://example.com')
soup = bs4.BeautifulSoup(getr.text, 'html.parser')
print(soup.p)
print(soup.a)
print(soup.body.div.contents)