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
    # return imglist
    print imglistjpg
    x = 0
    for imgurl in imglistjpg:
        urllib.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

url = "http://image.baidu.com/"
html = getHtml(url)

getImg(html)
print "get .jpg finished"

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(\S*\.jpeg)"'
    imgre = re.compile(reg)
    imglistjpeg = re.findall(imgre,html)
    # return imglist
    print imglistjpeg
    x = 90
    for imgurl in imglistjpeg:
        urllib.urlretrieve(imgurl,'%s.jpeg' % x)
        x+=1
        
getImg(html)

def getImg(html):
    reg = r'src="(\S*\.png)"'
    imgre = re.compile(reg)
    imglistpng = re.findall(imgre,html)
    # return imglist
    print imglistpng
    x = 50
    for imgurl in imglistpng:
        urllib.urlretrieve(imgurl,'%s.png' % x)
        x+=1
        
getImg(html)
print "get .png finished"