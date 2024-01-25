import requests
from bs4 import BeautifulSoup

def get_currency_rate(query):
    url = "https://www.google.com/search?q="+query

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    result = soup.find("div", class_="BNeawe iBp4i AP7Wnd").get_text()
    result = result.split()[0]
    return float(result.replace(",","."))

'''if __name__ == "__main__":
    query = input("введите запрос")
    query = query.replace(" ", "+")
    currency_rate = get_currency_rate(query)
    print(f"текущий курс валюты: {currency_rate}")'''