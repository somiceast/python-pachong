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
