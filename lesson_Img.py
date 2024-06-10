import requests
import pprint

img = "https://main-cdn.sbermegamarket.ru/big2/hlr-system/582/840/369/961/328/100059863984b0.jpg"

responce = requests.get(img)

with open ("test.jpg", "wb") as file:
    file.write(responce.content)