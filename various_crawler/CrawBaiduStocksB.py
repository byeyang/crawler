import requests
from bs4 import BeautifulSoup
import traceback
import re


def getHTMLText(url, code="utf-8"):
    try:
        r = requests.get("http://q.10jqka.com.cn/")
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    print(html)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    print(a)
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"\d{6}", href)[0])
        except:
            continue


def getStockInfo(lst, stockURL, fpath):
    count = 0
    for stock in lst:
        url = stockURL + stock + "/"
        print(url)
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
        except:
            count = count + 1
            print("\r当前进度: {:.2f}%".format(count * 100 / len(lst)), end="")
            continue


def main():
    stock_list_url = 'http://q.10jqka.com.cn'
    stock_info_url = 'http://stockpage.10jqka.com.cn/'
    output_file = 'D:/BaiduStockInfo.txt'
    slist = []
    getStockList(slist, stock_list_url)
    print(slist)
    getStockInfo(slist, stock_info_url, output_file)

#xueqiu 可以详细信息
#同花顺可以部分全部代码
#东方财富和百度垃圾 JavaScript
main()