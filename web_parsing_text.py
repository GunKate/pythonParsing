from bs4 import BeautifulSoup
import requests

url = "https://quotes.toscrape.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")

author = soup.find_all("small", class_ = "author")


for i in range(len(text)):
    print(f"цитата номер - {i+1}")
    print(text[i].text)
    print(f"автор цитаты - {author[i].text}\n")