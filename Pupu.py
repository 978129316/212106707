import json
import string
from time import sleep
from wsgiref import headers

import requests
from urllib3.util import url
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import datetime

def Pupu():
  url="https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/d8a2b28f-487a-44af-a1a9-4bfd4aea471b"
  headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'}
  response =requests.get(url=url,headers=headers,verify=False) #向网站发起请求，并获取响应对象
  d=json.loads(response.text) #转为字典
  name=d["data"]["name"]     #名称
  spec=d["data"]["spec"]     #规格
  price=str(float(d["data"]["price"]/100))   #折扣价
  market_price=str(float(d["data"]["market_price"]/100) )  #原价
  share_content=d["data"]["share_content"] #详细内容
  print("---------------商品："+name+"---------------")
  print("规格："+spec)
  print("价格："+market_price)
  print("原价/折扣价："+market_price+"/"+price)
  print("详细内容:"+share_content)
  print("---------------"+name+"的价格波动---------------")
  for i in range(1, 10):
      url = "https://j1.pupuapi.com/client/product/storeproduct/detail/deef1dd8-65ee-46bc-9e18-8cf1478a67e9/d8a2b28f-487a-44af-a1a9-4bfd4aea471b"
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'}
      #重新获取价格
      time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M')  #当前时间
      print("当前时间为"+time+"价格为："+price)
      sleep(3)  # 等待三秒输出
if __name__ == '__main__':
   Pupu()  #调用函数
