from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 按照标准的缩进格式的结构输出
soup = BeautifulSoup(html, "html.parser")

# 将Beautiful Soup的文档树格式化后以Unicode编码输出,
# 每个XML/HTML标签都独占一行
# print(soup.prettify())

# 从文档中找到所有<a>标签的链接
# print(soup.find_all('a'))

for link in soup.find_all('a'):
    # 获取link的href属性内容
    print(link.get('href'))
    # 获取link的文字内容
    print(link.get_text())

