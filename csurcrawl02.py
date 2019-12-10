import urllib.request
import requests
import wget as wget
import urllib
from bs4 import BeautifulSoup
import re
import  time
from mkdir import mkdir
lines = open('csur00.txt').readlines()
issue_lines = open('csur01.txt').readlines()
mkpath = r".\cusr"
mkdir(mkpath)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
}
para={
         'type': 'issue',
         'sellOnline': '0',
         'parent_id': 'J401',
         'parent_type': 'periodical',
         'title': 'Journal of the ACM (JACM) - Distributed Computing, Algorithms and Data Structures, Algorithms, Scientific Computing, Derandomizing Algorithms, Online Algorithms and Algorithmic Information Theory',
         'toctitle': 'Journal of the ACM (JACM)',
         'tocissue_date': 'Volume 52 Issue 6, November 2019',
         'notoc': '0',
         'usebody': 'tabbody',
         'tocnext_id':'',
         'tocnext_str':'',
         'tocprev_id': '3362097',
         'tocprev_str': 'Volume 52 Issue 5, October 2019',
         'toctype': 'Issue',
         '_cf_containerId': 'cf_layoutareaprox',
         '_cf_nodebug': 'true',
         '_cf_nocache': 'true',
         '_cf_clientid': '279D435735CD397B357E7BBFDCF679BC',
         '_cf_rc': '1'
         }
for i in range(30,60):
    s = lines[i]
    para['tocissue_date'] = issue_lines[i]
    para['tocnext_id']=re.findall('\d+',lines[i-1])
    para['tocnext_str'] = issue_lines[i-1]
    para['tocprev_id'] =re.findall('\d+',lines[i+1])
    para['tocprev_str'] = issue_lines[i+1]
    num = ''.join(re.findall('\d+', para['tocissue_date']))
    urlparam = urllib.parse.unquote_plus(urllib.parse.urlencode(para)).replace(' ', '20%')
    url = 'https://dl.acm.org/'+s.replace('citation.cfm','tab_about.cfm').strip('\n')+'&'+urlparam
    res = requests.get(url= url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    soup2 = soup.find_all('a', {"name": "FullTextPDF"})
    soup3 = soup.find_all('td', {"colspan": "1"})
    mkpath = r".\cusr\{}".format(num)
    mkdir(mkpath)
    fp = open(mkpath+'\csurpaperlist.txt', 'w')
    ft = open(mkpath +'\csurtitlelist.txt', 'w')

    for j in range(len(soup2)):
        try:
            p=soup2[j]
            purl = 'https://dl.acm.org/'+p['href']
            fp.write(purl)
            fp.write('\n')

            t= soup3[j]
            ptitle = t.find_all(text=True)[0]
            ft.write(ptitle)
            ft.write('\n')
        except:
            pass
    fp.close()
    ft.close()


    plines = open(mkpath+'\csurpaperlist.txt').readlines()
    tlines = open(mkpath +'\csurtitlelist.txt').readlines()
    for j in range(len(plines)):
        purl=plines[j][:-1]
        res = requests.get(purl, headers=headers)
        ptitle=tlines[j][:-1]
        out_fname = str(j) + '.pdf'
        with open(mkpath+'\\'+out_fname,'wb') as f2:
            # time.sleep(2)
            f2.write(res.content)
        time.sleep(2)
        f2.close()
        # time.sleep(1)





