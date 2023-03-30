import sys
import random as rand
import json

assert(len(sys.argv) == 2)
num_stocks = int(sys.argv[1])

All_Nasdaq_Stocks_File = open("All_Nasdaq_Stocks.json")
All_Nasdaq_Stocks = json.load(All_Nasdaq_Stocks_File)

with open("Stock_Tickers.json", "w") as f:
    output_string = "[ "
    i = 0
    stocks_seen = {}
    total_num_stocks = len(All_Nasdaq_Stocks)
    while i < num_stocks:
        rand_stock = All_Nasdaq_Stocks[rand.randrange(total_num_stocks)]
        if stocks_seen.get(rand_stock, False):
            continue
        else:
            output_string = output_string + "\"" + rand_stock + "\", "
            stocks_seen[rand_stock] = True
            i = i + 1
    output_string = output_string[:-2]
    output_string = output_string + " ]"
    f.write(output_string)