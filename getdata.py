import urllib,urllib2
from urllib2 import Request, urlopen, URLError, HTTPError
import time
import json
import os

os.system('mkdir -p ./data')
datafile = open('./data/data.txt', 'w')

#global setting
urllib2.socket.setdefaulttimeout(10)
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.122 Safari/537.36'
headers = { 'User-Agent' : user_agent }

#request url
r_ticker=urllib2.Request('http://market.huobi.com/staticmarket/ticker_btc_json.js')
r_depth=urllib2.Request('http://market.huobi.com/staticmarket/depth_btc_json.js')

counter = 0
while(1):

    counter = counter + 1
    print counter
	
    try:
        #open url
        o_ticker = urllib2.urlopen(r_ticker)
        o_depth = urllib2.urlopen(r_depth)

        #get content from response
        c_ticker = eval(o_ticker.read())
        c_depth = eval(o_depth.read())
    
        #combine content to a result
        result = {}
        result['ticker'] = c_ticker['ticker']
        result['time'] = c_ticker['time']
        result['asks'] = c_depth['asks']
        result['bids'] = c_depth['bids']
        
        #write to file
        datafile.write(str(result)+'\n')

    except URLError, e:
        datafile.write('fail\n')
        if hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        elif hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        else:
            print 'Undetected exception.'

    #fetch data every minutes
    time.sleep(60)

datafile.close()
