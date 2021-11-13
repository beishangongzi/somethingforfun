# encoding:utf-8

import requests
import base64


# client_id 为官网获取的AK， client_secret 为官网获取的SK
def getToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mmQnMG1Um66XS61FjDMqRaMt&client_secret=AxSP62vTNT9IVuf0PnAWZkVFrHiPWviD'
    response = requests.get(host)
    token = None
    if response:
        try:
            token = response.json()["access_token"]
        except:
            token = None
    return token


'''
人像动漫化
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime"
# 二进制方式打开图片文件
filename = input("input image path or type 'Enter' to use 'test.jpg' as default name: ")
if filename == "":
    filename = "test.jpg"
f = open(filename, 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
access_token = getToken()
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())

    try:
        imgdata = base64.b64decode(response.json()["image"])
        file = open("res" + filename, 'wb')
        file.write(imgdata)
        file.close()
    except:
        print("check your token")
else:
    print("failed")
