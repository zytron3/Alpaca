import Constants
import requests
import alpaca_trade_api as tradeapi

API_KEY = Constants.API_KEY
API_SECRET = Constants.API_SECRET
APCA_API_BASE_URL = "https://data.alpaca.markets"

alpaca = tradeapi.REST(API_KEY, API_SECRET, APCA_API_BASE_URL, 'v2')

request_url = "/stocks/AAPL/trades?start=1985-04-12T23:20:50Z"
print(alpaca.get(request_url))
