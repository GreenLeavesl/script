import requests, base64, fire
from lxml import etree


def icohash(s):
    s = (base64.b64encode(s.encode('utf-8'))).decode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    url = "https://www.fofa.so/result?qbase64=%s" % s
    r = requests.get(url=url, headers=headers)
    soup = etree.HTML(r.text)
    result = soup.xpath('//*[@id="q"]/@value')
    for i in result:
        print("http.favicon.hash:%s" % i[11:-1])


if __name__ == '__main__':
    fire.Fire(icohash)
