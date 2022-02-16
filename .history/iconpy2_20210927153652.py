import mmh3
import requests
response = requests.get('https://www.xxxx.com/favicon.ico')
favicon = response.content.encode('base64')
hash = mmh3.hash(favicon)
print 'http.favicon.hash:'+str(hash)