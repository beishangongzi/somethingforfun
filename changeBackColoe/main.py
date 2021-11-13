import os, random, requests
from urllib.request import urlretrieve

from requests_toolbelt.multipart.encoder import MultipartEncoder


def setDataFromFile(file):
    """
    set data From File
    :param file:
    :return:
    """
    rH = {}
    fp = open(file, "r", encoding="utf-8")
    lines = fp.readlines()
    for line in lines:
        key, value = line.split(": ")
        key = key.replace(":", "")
        rH[key] = value.strip()
    return rH


def getInfo(file):
    url = 'https://tool.lu/attachment/1B/tmp_upload'

    headers = {
        "origin": "https://tool.lu",
        "referer": "https://tool.lu/cutout/",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"
    }

    multipart_encoder = MultipartEncoder(
        fields={
            'file': (os.path.basename(file), open(file, 'rb'), 'application/octet-stream')
        },
        boundary='-----------------------------' + str(random.randint(1, 20))
    )

    headers['Content-Type'] = multipart_encoder.content_type

    r = requests.post(url, data=multipart_encoder, headers=headers)
    info = r.json()["data"]["info"]
    return info


def downloadPhoto(info, file, model, bg_index):
    """

    :param info:
    :param file:
    :param model: "human", "comman"
    :param bg_index:
            {0: 透明
            1,白色
            2,红色
            3,灰色
            4, 蓝色
            5，渐变
            }
    :return:
    """
    url2 = "https://tool.lu/cutout/ajax.html"
    data = {
        "original_image": info,
        "model": model,
        "bg_index": bg_index
    }
    res = requests.post(url2, data=data, headers=setDataFromFile("headers")).json()["url"]
    urlretrieve(res, file)
    print("success: " + file)


def main(picture="test.png", mode="human", bg_index=0, to="res.png"):
    info = getInfo(picture)
    downloadPhoto(info, to, mode, bg_index)


if __name__ == '__main__':
    for i in range(6):
        main(bg_index=i, to=str(i) + ".png")
