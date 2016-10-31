import requests
from bs4 import BeautifulSoup
'''
    查看github中wechat-core项目的访问流量
'''

loginGetUrl = "https://github.com/login"
loginPostUrl = 'https://github.com/session'
cloneDataUrl = "https://github.com/151376liujie/wechat-core/graphs/clone-activity-data"
trafficDataUrl = 'https://github.com/151376liujie/wechat-core/graphs/traffic-data'
sess = requests.session()
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding' : 'gzip',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}

data = {
    "commit":"Sign in",
    # "authenticity_token":"eFni+ReTCsNffmDIxEblyPbvp4cKOsJx58/BpO4N0D2uReO1tA3h5GGNW200srjZWd1dLpccbNEgsw4E9jE+Bw==",
    "login":"980463316@qq.com",
    "password":"liujie151376",
    "utf8":"%E2%9C%93"
}
# 第一步 获取authenticity_token值

resp = sess.get(loginGetUrl,headers=headers)
soup = BeautifulSoup(resp.text,'html.parser')
token = soup.find('input',attrs={"type":"hidden","name":"authenticity_token"})['value']
print("获取token值结果：%s" % token)

# 请求登录接口进行登录
data["authenticity_token"] = token
r = sess.post(loginPostUrl,data=data,headers=headers)
if r.ok:
    print("登录成功！")
    headers['Accept'] = "application/json"
    # 获取project 的clone数量
    cloneDataRes = sess.get(cloneDataUrl, headers=headers)
    if cloneDataRes.ok:
        cloneDataJson = cloneDataRes.json()
        print('total cloners:%s' % cloneDataJson['summary']['total'])
        print('unique cloners:%s' % cloneDataJson['summary']['unique'])

    trafficDataRes = sess.get(trafficDataUrl,headers=headers)
    if trafficDataRes.ok:
        trafficDataJson = trafficDataRes.json()
        print('total views:%s' % trafficDataJson['summary']['total'])
        print('unique views:%s' % trafficDataJson['summary']['unique'])

