import requests
import  xlwt

url = 'https://www.xiaomiyoupin.com/app/shopv3/pipe'

nav_payload = 'data=%7B%22result%22%3A%7B%22model%22%3A%22Homepage%22%2C%22action%22%3A%22GetGroup2ClassInfo%22%2C%22parameters%22%3A%7B%7D%7D%7D'
nav_headers = {
  'Referer': 'https://www.xiaomiyoupin.com/',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'youpindistinct_id=16f548b79fd138-0af230a57395eb-4c302a7b; mjclient=PC; youpindistinct_id=16f548b79fd138-0af230a57395eb-4c302a7b; mjclient=PC; Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1577671426; youpin_sessionid=16f5665d1e3-04ca5bc108af0f8-15af; youpin_sessionid=16f5aeb14a5-0f34b141ff6bce-15af; Hm_lpvt_025702dcecee57b18ed6fb366754c1b8=1577778354'
}
goods_headers = {
  'Referer': 'https://www.xiaomiyoupin.com/goodsbycategory?',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'Hm_lvt_025702dcecee57b18ed6fb366754c1b8=1577671426,1578898661,1578898677; youpin_sessionid=16f5665d1e3-04ca5bc108af0f8-15af; youpin_sessionid=16f9db503df-0913480a67e0d68-15b1; Hm_lpvt_025702dcecee57b18ed6fb366754c1b8=1578898884; youpindistinct_id=16f9db1950f45-04478f383045bf8-4c302978; mjclient=PC; youpindistinct_id=16f548b79fd138-0af230a57395eb-4c302a7b; mjclient=PC'
}
# 爬取商品分类信息
response = requests.request('POST', url, headers=nav_headers, data=nav_payload)
data = response.json()
nav_data = data.get('result').get('result').get('data').get('groups')
nav_list = []
for i in range(len(nav_data)):
    for j in range(len(nav_data[i])):
        nav = nav_data[i][j]['class']['ucid']
        nav_list.append(nav)

# 循环爬取分类商品界面的商品信息
goods_list = []
for i in nav_list:
    goods_payload = 'data=%7B%22uClassList%22%3A%7B%22model%22%3A%22Homepage%22%2C%22action%22%3A%22BuildHome%22%2C%22parameters%22%3A%7B%22id%22%3A%22'+ str(i) +'%22%7D%7D%7D'
    response = requests.request('POST', url, headers=goods_headers, data=goods_payload)
    data = response.json()
    seq_data = data.get('result').get('uClassList')['data']
    for j in range(len(seq_data)):
        if 'data' not in seq_data[j].keys():
            continue
        # print(seq_data[j]['data'])
        goods_data = seq_data[j]['data']
        for k in range(len(goods_data)):
            if 'gid' not in goods_data[k].keys():
                continue
            gid = goods_data[k]['gid']
            name = goods_data[k]['name']
            new_dict = {'gid': gid, 'name': name}
            goods_list.append(new_dict)
# 将结果保存为excel文档
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('商品')
sheet.write(0, 0, '编号')
sheet.write(0, 1, '商品名')
j = 1
for l in goods_list:
    sheet.write(j, 0, l['gid'])
    sheet.write(j, 1, l['name'])
    j = j + 1
workbook.save('another_result.xls')

