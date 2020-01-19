from bs4 import BeautifulSoup
from selenium import webdriver
import time
import xlwt


class ShopSpider:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.next_url = []

    def run(self):
        url = "https://www.xiaomiyoupin.com"
        self.browser.get(url)
        time.sleep(5)
        # 获取商品索引
        nav_list = self.browser.find_elements_by_xpath("//ul[@class='nav-list']/li/span/a")
        for index in nav_list:
            nav = url + index.get_attribute("data-src")
            self.next_url.append(nav)
        self.next_url = list(set(self.next_url))
        print(len(self.next_url))
        # 获取商品信息
        gid_list = []
        name_list = []
        for url in self.next_url:
            self.browser.get(url)
            time.sleep(5)
            soup = BeautifulSoup(self.browser.page_source, "html.parser")
            for gid in soup.find_all("div", "pro-item"):
                gid_list.append(gid.get("data-src")[-6:])
            for name in soup.find_all("p", "pro-info"):
                name_list.append(name.get("title"))

        # 将结果保存为excel文档
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("商品")
        sheet.write(0, 0, "编号")
        sheet.write(0, 1, "商品名")
        j = 1
        for i in range(len(name_list)):
            sheet.write(j, 0, gid_list[i])
            sheet.write(j, 1, name_list[i])
            j = j + 1
        workbook.save('result.xls')


if __name__ == "__main__":
    spider = ShopSpider()
    spider.run()
