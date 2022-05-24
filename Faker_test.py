from bs4 import BeautifulSoup
import requests

url = 'https://vc.ru/new'
response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
news = soup.find_all('div', class_='content-title content-title--short l-island-a')
for el in news:
    print(el.text.replece('Span'))
print(news)
# for el in news:
