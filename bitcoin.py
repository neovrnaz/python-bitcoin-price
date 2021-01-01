import json

try:
    import urllib.request as urllib2
except ImportError:
    raise ImportError('There was a problem importing urllib2')

url = "http://api.coindesk.com/v1/bpi/currentprice/EUR.json"

jsonURL = urllib2.urlopen(url)

jsonObject = json.load(jsonURL)

print(jsonObject['bpi']['USD']['code'])
print(jsonObject['bpi']['USD']['rate'])
