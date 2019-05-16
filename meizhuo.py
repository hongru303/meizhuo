import requests
from lxml import etree
import re


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}
session = requests.Session()
response = session.get('http://www.win4000.com/mt/zhuyilong.html', headers = headers).text
html = etree.HTML(response)
imgs_url = html.xpath('//div[@class="tab_box"]/div/ul[@class="clearfix"]/li/a/@href')[0:-5]#解析出所有组图url
for img_url in imgs_url:
    resp = requests.get(img_url,headers=headers).text
    htm = etree.HTML(resp)
    for i in range(1,8):
        iurl = re.search('http://www.win4000.com/meinv(.*?)_*.html', img_url).group(1)
        all_urls = 'http://www.win4000.com/meinv{}_{}.html'.format(iurl, i)
        res = requests.get(all_urls, headers=headers).text
        ht = etree.HTML(res)
        all_url = ht.xpath('//div[@id="pic-meinv"]/a/img/@url')
        if all_url:
            try:
                r = requests.get(all_url[0], headers=headers)
                with open(r'./zhuyilong/{}.jpg'.format(iurl+'_'+str(i)), 'wb') as f:
                    f.write(r.content)
                print('successed',iurl+'_'+str(i))
            except Exception:
                pass

