# rychlo-ukázka
import requests
import bs4
# from bs4 import BeautifulSoup
#
# url = "https://www.idnes.cz/"
#
# odpoved_serveru = requests.get(url)
#
# rozdelene_html = BeautifulSoup(odpoved_serveru.content)
# vsechny_elementy_a = rozdelene_html.find_all("a", {"class": "art-link"})
#
# vysledky = {}
#
# for elem_a in vsechny_elementy_a:
#     vysledky[elem_a["href"]] = elem_a.get_text()
#
# for i, clanek in enumerate(vysledky):
#     print(i, vysledky[clanek].strip())


# response = requests.get('https://httpbin.org')
# response = requests.post('http://httpbin.org/post', data = {'my_message':'Hello'})
#
# print(response.status_code)
# print(response.text)

getr = requests.get('https://example.com')
soup = bs4.BeautifulSoup(getr.text, 'html.parser')
print(soup.p)
print(soup.a)
print(soup.body.div.contents)