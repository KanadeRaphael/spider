import http.client
import json
import xlwt
conn = http.client.HTTPSConnection("www.xiaomiyoupin.com")
headers = {
    'Content-Type': 'application/json'
}
index = list(range(100, 1000))+list(range(100000, 120000))
list = []
for i in index:
    payload = "{\"groupName\":\"details\",\"groupParams\":[[\"%d\"]],\"methods\":[],\"version\":\"1.0.0\",\"debug\":false,\"channel\":\"\"}" % i
    conn.request("POST", "/api/gateway/detail", payload, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    json_d = json.loads(data)
    if json_d.get('code') == 0:
        name = json_d.get('data').get('goods').get('goodsInfo').get('name')
        print(str(i)+' '+name)
        new_dict = {'gid': i, 'name': name}
        list.append(new_dict)
# 将结果保存为excel文档
workbook = xlwt.Workbook()
sheet = workbook.add_sheet('商品')
sheet.write(0, 0, '编号')
sheet.write(0, 1, '商品名')
j = 1
for l in list:
    sheet.write(j, 0, l['gid'])
    sheet.write(j, 1, l['name'])
    j = j + 1
workbook.save('result.xls')
