import requests
from bs4 import BeautifulSoup

def getStockdata(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}";
    r = requests.get(url=url);
    website_info = r.text;
    soup = BeautifulSoup(website_info, "html.parser");
    price = soup.find('fin-streamer', {'class': 'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text;
    change = soup.find_all('fin-streamer', {'class': 'Fw(500) Pstart(8px) Fz(24px)'});
    print(price);
    [print(change[x].text) for x in range(len(change))];
ticker = input('What stock would you like to look up? ');
getStockdata(ticker)
