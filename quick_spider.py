import requests
from bs4 import BeautifulSoup
import xlwt
import time


class Spider:

    def __init__(self):
        self.url = "https://www.xiaomiyoupin.com/app/shopv3/pipe"
        self.payload = "data=%7B%22result%22%3A%7B%22model%22%3A%22Homepage%22%2C%22action%22%3A%22GetGroup2ClassInfo%22%2C%22parameters%22%3A%7B%7D%7D%7D"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.xiaomiyoupin.com/',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Yp-App-Source': 'front-PC',
            'X-User-Agent': 'channel/youpin platform/youpin.pc',
            'Origin': 'https://www.xiaomiyoupin.com',
            'Content-Length': '130',
            'Connection': 'keep-alive',
            'Cookie': 'youpindistinct_id=16f548b79fd138-0af230a57395eb-4c302a7b; mjclient=PC; youpindistinct_id=16f548b79fd138-0af230a57395eb-4c302a7b; mjclient=PC; Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1577671426; youpin_sessionid=16f5665d1e3-04ca5bc108af0f8-15af; youpin_sessionid=16f5aeb14a5-0f34b141ff6bce-15af; Hm_lpvt_025702dcecee57b18ed6fb366754c1b8=1577778354'
        }

    def start(self):
        response = requests.request("POST", self.url, headers=self.headers, data=self.payload)
        body = response.json().get('result').get('result').get('data').get('groups')
        nav_list = []
        for i in range(9):
            for j in range(2):
                new_dict = {'title': body[i][j]['class']['name'], 'ucid': body[i][j]['class']['ucid']}
                nav_list.append(new_dict)
        print(len(nav_list))
        for nav in nav_list:
            print(nav)
            ucid = nav['ucid']
            title = nav['title']
            url = 'https://www.xiaomiyoupin.com/goodsbycategory?firstId=' + str(ucid) + '&secondId=' + str(ucid) + '&title=' + title
            print(url)


if __name__ == "__main__":
    spider = Spider()
    spider.start()
    # spider.parse_url(nav_list)
