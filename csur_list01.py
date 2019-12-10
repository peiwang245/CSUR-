import urllib.request
import requests
from bs4 import BeautifulSoup

url = "https://dl.acm.org/pub_series.cfm?id=J401&_cf_containerId=cf_layoutareapubs&_cf_nodebug=true&_cf_nocache=true&_cf_clientid=BA4CB827F72F640030DAA517180AA5F4&_cf_rc=1"
headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36'}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.content,'lxml')
soup2=soup.find_all('td', {"nowrap": "nowrap"})


fp_href = open('csur00.txt', 'w')
fp_volume = open('csur01.txt', 'w')
fp_href_volume = open('csur02.txt', 'w')
for i in soup2:
    s00 =i.find('a')['href'];
    fp_href.write(s00)
    fp_href.write('\n')
    s01 =i.find_all(text=True)[0];
    fp_volume.write(s01)
    fp_volume.write('\n')

    fp_href_volume.write(s00)
    fp_href_volume.write(' ')
    fp_href_volume.write(s01)
    fp_href_volume.write('\n')
fp_href.close()
fp_volume.close()


