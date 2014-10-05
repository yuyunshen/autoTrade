import urllib,urllib2
import time
import json

datafile = open('./data/data.txt', 'w')

#request url
r_ticker=urllib2.Request('http://market.huobi.com/staticmarket/ticker_btc_json.js')
r_depth=urllib2.Request('http://market.huobi.com/staticmarket/depth_btc_json.js')
r_kline001=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_001_json.js') 
r_kline005=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_005_json.js')
r_kline015=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_015_json.js')
r_kline030=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_030_json.js')
r_kline060=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_060_json.js')
r_kline100=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_100_json.js')
r_kline200=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_200_json.js')
r_kline300=urllib2.Request('http://market.huobi.com/staticmarket/btc_kline_300_json.js')



counter = 0
while(1):

    counter = counter + 1
    print counter
	
    #open url
    o_ticker = urllib2.urlopen(r_ticker)
    o_depth = urllib2.urlopen(r_depth)
    o_kline001=urllib2.urlopen(r_kline001) 
    o_kline005=urllib2.urlopen(r_kline005)
    o_kline015=urllib2.urlopen(r_kline015)
    o_kline030=urllib2.urlopen(r_kline030)
    o_kline060=urllib2.urlopen(r_kline060)
    o_kline100=urllib2.urlopen(r_kline100)
    o_kline200=urllib2.urlopen(r_kline200)
    o_kline300=urllib2.urlopen(r_kline300)
    
    #get content from response
    c_ticker = eval(o_ticker.read())
    c_depth = eval(o_depth.read())
    c_kline001=eval(o_kline001.read()) 
    c_kline005=eval(o_kline005.read())
    c_kline015=eval(o_kline015.read())
    c_kline030=eval(o_kline030.read())
    c_kline060=eval(o_kline060.read())
    c_kline100=eval(o_kline100.read())
    c_kline200=eval(o_kline200.read())
    c_kline300=eval(o_kline300.read())
    
    #combine content to a result
    result = {}
    result['ticker'] = c_ticker['ticker']
    result['time'] = c_ticker['time']
    result['asks'] = c_depth['asks']
    result['bids'] = c_depth['bids']
    result['kline001'] = c_kline001
    result['kline005'] = c_kline005
    result['kline015'] = c_kline015
    result['kline030'] = c_kline030
    result['kline060'] = c_kline060
    result['kline100'] = c_kline100
    result['kline200'] = c_kline200
    result['kline300'] = c_kline300
    
    #write to file
    datafile.write(str(result)+'\n')

	#fetch data every 5 minutes
    time.sleep(300)

datafile.close()
