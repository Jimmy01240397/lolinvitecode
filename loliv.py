import requests
import json
import time
import re

def loadData(url, code):
    headers = {
        'content-type':'application/json',
        'Accept-encoding':'gzip,deflate',
        'token':'[你的Token]'
    }
    datajson = {"code":code,"confirm":True}
    r = requests.post(url, headers = headers, json=datajson)
    return r


def main():
    url = "https://bargain.lol.garena.tw/api/enter"
    nowstate = ""
    while True:
        headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        r = requests.get("https://forum.gamer.com.tw/ajax/moreCommend.php?bsn=17532&snB=5838400&returnHtml=0", headers = headers)
        data = json.loads(r.text)
        matches = re.finditer(r'LOL[A-Z,0-9]{10}', data["0"]["comment"], re.MULTILINE)
        nowget = ""
        allget = []
        for match in matches:
            allget.append(str(match.group()))
            nowget = str(match.group())
        
        if nowstate != nowget:
            for match in allget:
                content = loadData(url, match)
                print(match)
                print(json.loads(content.text))
        
        nowstate = nowget
        time.sleep(1)

if __name__ == '__main__':
    main()
