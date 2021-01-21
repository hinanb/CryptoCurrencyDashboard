#https://github.com/man-c/pycoingecko
#https://www.coingecko.com/en/api#
#https://www.coingecko.com/en/api
#https://taapi.io/indicators/


#This example uses Python 2.7 and the python-request library.
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv

symbols=[]
topCoins=[]
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'1000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '7b96af50-71b9-48c8-8211-3396385f4b08',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  d=data['data']
  #f=d[0]['slug']
  for index in range(len(d)):
      topCoins.append([d[index]['slug'],d[index]['symbol']])

  for index in range(len(d)):
      symbols.append(d[index]['symbol'])
  #print(topCoins)    
  print(len(topCoins))
  print(topCoins)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)


with open('TopCoins.csv', 'w') as filehandle:
    for listitem in topCoins:
        filehandle.write('%s\n' % listitem)  
  
from pycoingecko import CoinGeckoAPI
import time
import datetime
cg = CoinGeckoAPI()

startdate = "01/01/2010"
enddate = "17/01/2021"

startdate=time.mktime(datetime.datetime.strptime(startdate, "%d/%m/%Y").timetuple())
enddate=time.mktime(datetime.datetime.strptime(enddate, "%d/%m/%Y").timetuple())
readablestart=time.ctime(int(startdate))
readableend=time.ctime(int(enddate))
counter=0
failCounter=0

li=[]
fail=0
success=125
        
print(len(topCoins))
writebaleList=[]
counter=0
counteri=230

repeat=0
f = open("file.csv", "a")

print("Press 1 to fetch single currency update. Press 2 for bulk update ")
instruction = input("Enter instruction:")
instruction=int(instruction)
if instruction==1:
            currency = input("Enter Currency symbol: e.g btc for bitcoin:")

            endpoint = "https://api.taapi.io/bulk"
            conc=currency+"/USDT"
            # Define a JSON body with parameters to be sent to the API 
            parameters = {
                "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhpbmFuYmlsYWw1MTVAZ21haWwuY29tIiwiaWF0IjoxNjEwODkzNjQ5LCJleHAiOjc5MTgwOTM2NDl9.cEXvZHEGdAWOlrlzHMSTDaguIF4tRmV9Byv7Pa0RpDs",
                "construct": {
                    "exchange": "binance",
                    "symbol": conc,
                    "interval": "1h",
                    "indicators": [
                        {
                            # Relative Strength Index
                            "indicator": "ma"
                        },
                        {
                            # Chaikin Money Flow
                            "indicator": "ema",
                            
                        },
                        {
                            # MACD Backtracked 1
                            "indicator": "bbands2",
                            
                        },
                        
                        {
                            "indicator": "obv",
                        },
                        
                        {
                            "indicator": "rsi",
                        },
                        
                        {
                            "indicator": "stoch",
                        },
                        
                        {
                            "indicator": "trix",
                        }
                        ,
                        
                        {
                            "indicator": "macd",
                        }
                        ,
                        
                        {
                            "indicator": "sar",
                        }
                        ,
                        
                        {
                            "indicator": "ichimoku",
                        }
                        
                    ]
                }
            }

            response = requests.post(url = endpoint, json = parameters)
              
            result = response.json() 
            result=result['data']
            
            print(result)
                  
      
else:  


  #for coin in topCoins:
  while success<=500:

          coin=topCoins[counteri]
          time.sleep(60)
          try:
            
            endpoint = "https://api.taapi.io/bulk"
            conc=coin[1]+"/USDT"
            # Define a JSON body with parameters to be sent to the API 
            parameters = {
                "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImhpbmFuYmlsYWw1MTVAZ21haWwuY29tIiwiaWF0IjoxNjEwODkzNjQ5LCJleHAiOjc5MTgwOTM2NDl9.cEXvZHEGdAWOlrlzHMSTDaguIF4tRmV9Byv7Pa0RpDs",
                "construct": {
                    "exchange": "binance",
                    "symbol": conc,
                    "interval": "1h",
                    "indicators": [
                        {
                            # Relative Strength Index
                            "indicator": "ma"
                        },
                        {
                            # Chaikin Money Flow
                            "indicator": "ema",
                            
                        },
                        {
                            # MACD Backtracked 1
                            "indicator": "bbands2",
                            
                        },
                        
                        {
                            "indicator": "obv",
                        },
                        
                        {
                            "indicator": "rsi",
                        },
                        
                        {
                            "indicator": "stoch",
                        },
                        
                        {
                            "indicator": "trix",
                        }
                        ,
                        
                        {
                            "indicator": "macd",
                        }
                        ,
                        
                        {
                            "indicator": "sar",
                        }
                        ,
                        
                        {
                            "indicator": "ichimoku",
                        }
                        
                    ]
                }
            }

            response = requests.post(url = endpoint, json = parameters)
              
            result = response.json() 
            print(result)
            result=result['data']
            li.clear()
            for i in result:
              li.append(i['result'])
            success=success+1
            
            with open("indicators.csv", 'a', newline='') as file:
               writer = csv.writer(file)
               writer.writerow([coin[0], li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9]])
                

            counteri=counteri+1
            print("SUCCESS"+str(success)+" outof" +str(counteri))
            
     
          except:
            repeat=repeat+1
            failCounter=failCounter+1
            print('failed Coin'+ str(counteri))
            if repeat==1:  #only three tries for each crypto
              counteri=counteri+1
              repeat=0
              print('skiiping')
              
           
      
  f.close()
