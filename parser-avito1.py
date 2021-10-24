from bs4 import BeautifulSoup
import requests
product = input()

url = "https://www.avito.ru/pskov/telefony/mobile-ASgBAgICAUSwwQ2I_Dc?cd=1&q=iphone+7&s=1" + product
request = requests.get(url)
bs = BeautifulSoup(request.text, "html.parser")

all_links = bs.find_all("a", class_= "iva-item-title")
for link in all_links:
    print("https://www.avito.ru" + link["href"])