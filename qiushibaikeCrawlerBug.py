from bs4 import BeautifulSoup
import crawlbug

'''
    扒取糗事百科热门段子
'''

url = 'http://www.qiushibaike.com/'

html = crawlbug.download(url)

html = html.decode('utf-8')

doc = BeautifulSoup(html,'html.parser')
# element.Tag.getText
ele = doc.find_all('div',attrs={'class':'article block untagged mb15'})
for content in ele:
    div = content.find('div',attrs={'class':'content'})
    print(div.getText())
