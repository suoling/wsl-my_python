import http.client

conn = http.client.HTTPSConnection('www.baidu.com')
conn.request('GET', '/')
r1 = conn.getresponse()
# print(r1.getheaders())
# print(r1.read())
aaa = {}
for index in range(len(r1.getheaders())):
    aaa[r1.getheaders()[index][0]] = r1.getheaders()[index][1]

print(aaa)
