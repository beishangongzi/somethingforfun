from urllib.request import urlretrieve

import requests


def setDataFromFile(file):
    """
    set data From File
    :param file:
    :return: a dictionary
    """
    rH = {}
    fp = open(file, "r", encoding="utf-8")
    lines = fp.readlines()
    for line in lines:
        key, value = line.split(": ")
        key = key.replace(":", "")
        rH[key] = value.strip()
    return rH


# text 是要被转换的文字
def postTest(text):
    headers = setDataFromFile("headers")
    postTestUrl = "https://shouxie.laoxiezi.com/function.php?make"
    data = setDataFromFile("data")
    data["text"] = text
    postTexturl = requests.post(postTestUrl, data=data, headers=headers).text.strip()
    resUrl = "https://shouxie.laoxiezi.com/"
    resUrl = resUrl + postTexturl[0:]
    return resUrl

# 下载图片
def download(url, file):
    urlretrieve(url, file)
    print("download success and save to: " + file)


# 被转换文字的文件
# 结果存放的文件
def main(file, resFile):
    with open(file, "r", encoding="utf-8") as f:
        text = f.readlines()
    text = "".join(text)
    resUrl = postTest(text)
    download(resUrl, resFile)


if __name__ == '__main__':
    main("text", "res.png")
