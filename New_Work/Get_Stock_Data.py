import requests
import json
import alpha_vantage
import time

Stock_Tickers_File = open("Stock_Tickers.json")
Stock_Tickers = json.load(Stock_Tickers_File)

Api_Keys_File = open("api_keys.json")
api_keys = json.load(Api_Keys_File)
AlphaVantageKey = api_keys["AlphaVantage"]

API_URL = "https://www.alphavantage.co/query"
stock_data_jsons = {}
api_call_counter = 5
for stock_symbol in Stock_Tickers:
    if api_call_counter >= 5:
        api_call_counter = 0
        time.sleep(300)
    api_call_counter = api_call_counter + 1
    data = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": stock_symbol,
        "outputsize": "full",
        "datatype": "json",
        "apikey": AlphaVantageKey
    }
    response = requests.get(API_URL, data)
    if response.status_code != 200:
        break
    response_json = response.json()
    stock_data_jsons[stock_symbol] = response_json

with open("Stock_Data.json", "w") as f:
    f.write(json.dumps(stock_data_jsons, indent=2))