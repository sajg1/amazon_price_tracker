import requests
from bs4 import BeautifulSoup
from pprint import pprint

BASE_URL = 'https://www.amazon.co.uk/Furbo-Dog-Camera-2-Way-Audio-Compatible/dp/B01FXC7JWQ'

HEADERS = {
    'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0'
                   '.4515.131 Safari/537.36'
}

response = requests.get(BASE_URL, headers=HEADERS)
furbo = response.text

soup = BeautifulSoup(furbo, 'html.parser')
price_span = soup.find(name='span', class_='a-offscreen')
print(price_span.getText())




