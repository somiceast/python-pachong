# -*- coding: utf-8 -*
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(\S*\.jpg)"'
    imgre = re.compile(reg)
    imglistjpg = re.findall(imgre,html)
    print imglistjpg
    return imglistjpg
    x = 0
    for imgurl in imglistjpg:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

keyword=raw_input("请输入关键字:")
url = "http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1483535133108_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word="+keyword
print url
html = getHtml(url)

getImg(html)
print "get  *.jpg finished"

# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html

# def getImg(html):
#     reg = r'src="(\S*\.jpeg)"'
#     imgre = re.compile(reg)
#     imglistjpeg = re.findall(imgre,html)
#     print imglistjpeg
#     return imglistjpeg
#     x = 90
#     for imgurl in imglistjpeg:
#         urllib.urlretrieve(imgurl,'%s.jpeg' % x)
#         x+=1
        
# getImg(html)
# print "get .jpeg finished"

# def getImg(html):
#     reg = r'src="(\S*\.png)"'
#     imgre = re.compile(reg)
#     imglistpng = re.findall(imgre,html)
#     print imglistpng
#     return imglistpng
#     x = 90
#     for imgurl in imglistpng:
#         urllib.urlretrieve(imgurl,'%s.png' % x)
#         x+=1
        
# getImg(html)
# print "get .png finished"