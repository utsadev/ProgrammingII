"""Testing pulling data from bittrex"""

import json
import csv
from bittrex import Bittrex

#API Key, Bittrex b8fff1ce3fc24461af8755b802256431
#secret or api key? b586b6fcb829494b90ee14c28128b11d


#Key:8b634f9a28fe44fd8d1266b16f9b232b
#Secret:864d7a972918478b9e78f9f5dc6f761e


def main():

    api_key = "8b634f9a28fe44fd8d1266b16f9b232b"
    api_secret = "864d7a972918478b9e78f9f5dc6f761e"

    print("** Tesing out Bittrex **")
    bitWeb = "https://bittrex.com/api/v1.1/public/getmarkets"
    #markSum = "https://bittrex.com/api/v1.1/public/getmarketsummaries"

    #my_bittrex = Bittrex(api_key, api_secret) # or defaulting to v1.1 as Bittrex(None, None)
    #testing = my_bittrex.get_markets()

    #myTest = bt.bittrex.Bittrex(api_key,api_secret)

    #print(testing)


    #page = url.urlopen(bitWeb).read()
    #mSum = url.urlopen(markSum).read()

    #print(page)
    #-------------------------------------------------
    myB = Bittrex(api_key, api_secret)
    #print(myB.get_marketsummary('BTC-NAV'))
    #print(myB.get_balance('ETH'))
    #print(myB.get_balance('NAV'))
    #print("-------------")
    #print(myB.get_market_history('BTC-NAV'))
    navHist = myB.get_market_history('BTC-NAV')
    getBalance = myB.get_balance('NAV')
    #test = json.loads(myB.get_balance('ETH'))
    #dump = json.dumps(test)
    #print(dump)
    #print(type(getBalance))
    #balTest = test["Balance"]
    #if "result"in getBalance:
     #   print(getBalance["result"]["Balance"])
     #   result = getBalance["result"]

    #print(result)
    #print(navHist["result"])
    print("---------------------")
    print("---------------------")
    print("---------------------")
    print(navHist["result"][0])
    print(navHist["result"][-1])
    #print(navHist["result"][2])
    #print(navHist["result"][-4])
    print(len(navHist["result"]))

    #with open('data.csv', 'w', newline='') as csvfile:
    ##    fieldnames = ['Id', 'TimeStamp', 'Quantity', 'Price', 'Total', 'FillType', 'OrderType']
     #   writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #    writer.writeheader()

    #    for i in range(0,200):
    #        writer.writerow({'Id', 'TimeStamp', 'Quantity', 'Price', 'Total', 'FillType', 'OrderType'})

    print(type(navHist))

    with open('data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in navHist.items():
            writer.writerow([key, value])

    #print(navHist.items())
    print("finished")




    

if __name__ == "__main__":
    main()
