import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(info, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:  # 找标签名为tbody的标签  <tbody> </tbody>:
        if isinstance(tr, bs4.element.Tag):
            tds = tr.find_all('td')  # 把 tr 标签中的所有 td 标签的内容存储在列表 tds
            # 把排名、大学名字、总分放入 info 列表

            out = tds[1].find('span')
            if out:
                info.append([tds[0].string.strip(), tds[1].find('span').string.strip(), tds[4].string.strip()])
            else:
                info.append([tds[0].string.strip(), tds[1].find('a').string.strip(), tds[4].string.strip()])


def printUnivList(ulist, num):
    # print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    # for i in range(num):
    #     u=ulist[i]
    #     print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0], u[1], u[2], chr(12288)))


def main():
    info = []
    url = "https://www.shanghairanking.cn/rankings/arwu/2021"
    html = getHTMLText(url)
    fillUnivList(info, html)
    printUnivList(info, 30)


main()

# import requests
# from bs4 import  BeautifulSoup
# import  bs4
# def getHTMLText(url):
#     try:
#         kv = {'user-agent': 'Mozilla/5.0'}
#         mydata = {'func':'login-session', 'login_source':'bor-info', 'bor_id': '***', 'bor_verification': '***','bor_library':'NEU50'}
#         re = requests.post(url, data=mydata, headers=kv)
#         re.raise_for_status()
#         re.encoding = re.apparent_encoding
#         return re.text
#     except:
#         print("异常")
#         return""
# def fillBookList(booklist, html):
#     soup = BeautifulSoup(html,"html.parser")
#     for tr in soup.find(id='history').descendants:
#         if isinstance(tr, bs4.element.Tag):
#             temp = tr.find_all('td')
#             if len(temp)>0:
#                 booklist.append(temp[1].string.strip())
#                 booklist.append(temp[3].string.strip())
#                 booklist.append(temp[5].string.strip())
#                 break
# def printUnivList(booklist):
#     print("{:^10}\t{:^6}\t{:^10}".format("外借","借阅历史列表","预约请求"))
#     print("{:^10}\t{:^6}\t{:^10}".format(booklist[0],booklist[1],booklist[2]))
#
# def main():
#     html = getHTMLText("http://202.118.8.7:8991/F/-?func=bor-info")
#     booklist = []
#     fillBookList(booklist, html)
#     printUnivList(booklist)
# main()


# import requests
# r = requests.get("https://www.shanghairanking.cn/rankings/arwu/2021")  # get 请求指定的页面信息
# print(r.status_code)  # 检查状态码是否正确，状态为 200，说明访问成功
# r.encoding = r.apparent_encoding  # 转换成 utf-8 的编码
# print(r.encoding)
# html = r.text  # 获取页面内容
# from bs4 import BeautifulSoup
# import  bs4
# soup = BeautifulSoup(html, "html.parser")  # 解析世界大学排名的页面
# data = soup.find("tbody").children  #找标签名为tbody的标签  <tbody> </tbody>
# # for tr in data:
# #     print(tr)
# info = []  # 定义一个列表去保存最后需要的数据
# for tr in soup.find('tbody').children:
#     # 用 isinstance() 函数来判断一个对象是否是一个已知的类型
#     if isinstance(tr, bs4.element.Tag):  # 判断 tr 是否是 bs4 标签类型的元素
#         tds = tr.find_all('td')  # 把 tr 标签中的所有 td 标签的内容存储在列表 tds
#         # 把排名、大学名字、总分放入 info 列表
#         # print(tds)
#         # tr('span')
#         out = tds[1].find('span')
#         if out:
#             info.append([tds[0].string.strip(), tds[1].find('span').string.strip(), tds[4].string.strip()])
#         else:
#             info.append([tds[0].string.strip(), tds[1].find('a').string.strip(), tds[4].string.strip()])
# print(info)
