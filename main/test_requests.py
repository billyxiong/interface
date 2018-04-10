import json
import requests
# headers = {"Content-Type":"application/json;charset=UTF-8"}
# url = "http://192.168.0.171:8088/api/auth/token"
# data = {"userName":"coolead","password":"000000","grantType":"password","ssoUUID":"","refreshToken":""}
# r = requests.post(url,data=json.dumps(data),headers= headers)
# print data
# print r.content

headers = {"Content-Type":"application/json;charset=UTF-8"}
url2 = "http://192.168.0.171:8088/coolead"
r = requests.get(url2,headers)
print r
print type(r)