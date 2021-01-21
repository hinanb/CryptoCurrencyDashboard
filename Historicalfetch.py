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
import pandas as pd 


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
from datetime import datetime
import datetime
import _datetime

cg = CoinGeckoAPI()


startdate = "01/01/2010"
enddate = _datetime.datetime.now()
enddate=str(enddate.day)+ '/'+str( enddate.month)+ '/'+str( enddate.year)


startdate=time.mktime(datetime.datetime.strptime(startdate, "%d/%m/%Y").timetuple())
enddate=time.mktime(datetime.datetime.strptime("19/01/2021", "%d/%m/%Y").timetuple())

readablestart=time.ctime(int(startdate))
readableend=time.ctime(int(enddate))
counter=0
failCounter=0

li=[]
fail=0
success=0
        
print(len(topCoins))
writebaleList=[]
counter=0
counteri=0

repeat=0
dataInput=[]   
df =pd.read_csv("fileHist.csv") 

#for coin in topCoins:
while counteri<=600:
        coin=topCoins[counteri]
        time.sleep(1)
            
          
         
    
          
        try:
          get=cg.get_coin_market_chart_range_by_id(coin[0],'usd',startdate,enddate)
           
          get=get['prices']
          dataInput.clear()

          df[str(coin[0])] = ""
          
          for writein in get:
                    
                    
                    
                    price=str(writein[1])
                    dataInput.append(price)
                    
                    
                    df.loc[df["TimeStamp"] == int(writein[0]), str(coin[0])]=price
                    
                      
                      
                              
          
        
          print(counteri)
          counteri=counteri+1 

          
          
        except:
          repeat=repeat+1
          failCounter=failCounter+1
          print('failed Coin'+ str(counteri))
          if repeat==1:  #only three tries for each crypto
            counteri=counteri+1
            repeat=0
            
df.to_csv("hist.csv",mode='a')
          
