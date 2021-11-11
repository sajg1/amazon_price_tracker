import requests
from bs4 import BeautifulSoup
import os
import smtplib



BASE_URL = 'https://www.amazon.co.uk/Furbo-Dog-Camera-2-Way-Audio-Compatible/dp/B01FXC7JWQ'
YAHOO_MAIL_PASS = os.environ.get('YAHOO_MAIL_PASS')
YAHOO_MAIL_ADD = os.environ.get('YAHOO_MAIL_PASS')
GMAIL_ADD = 'stephengossip@gmail.com'

HEADERS = {
    'Accept-Language' : 'en-GB,en-US;q=0.9,en;q=0.8',
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0'
                   '.4515.131 Safari/537.36'
}

response = requests.get(BASE_URL, headers=HEADERS)
furbo = response.text

soup = BeautifulSoup(furbo, 'html.parser')
price_span = soup.find(name='span', class_='a-offscreen')
price_str = price_span.getText()
price_float = float(price_str.split("£")[1])
product_title = soup.find(name='span', id='productTitle').getText().replace('\n','')
acceptable_price = 195.0

message = f"Subject:Buy Now! \n\nAttention!! \n\n{product_title}\n\n Price is now £{price_float}.\n Buy it now at {BASE_URL}"
if price_float <= acceptable_price:
    # try:
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user='appbreweryinfo@yahoo.com', password=YAHOO_MAIL_PASS)
            connection.sendmail(from_addr='appbreweryinfo@yahoo.com', to_addrs=GMAIL_ADD,
                                msg=(message.encode()))
            connection.close()

    # except:
    #     print('Could not send email')






