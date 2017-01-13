#http://www.imekaku.com/2015/08/31/python-work-tieba2/
# -*- coding: utf-8 -*
import re
import urllib

def getHtml(url):

    page = urllib.urlopen(url)
    html = page.read()
#    print html
    return html

def getTxt(html):
    regg='<div class="book_con">(\S*)<div class="pagination_wrap">'
    # reg = r'src="(\S*\.jpg)"'
    #正则表达式开始匹配
    txtre = re.compile(regg)
    #返回的是一个列表,所以将得到的所有楼层中的文本
    # 得出,放在一个列表items中.最后依次打印出来就可以.
    items = txtre.findall(html)
    print items


    # 去除标签
    removeImg=re.compile('<img.*?>')
    removeImg=re.compile('<img.*?>')
    removeImg=re.compile('<img.*?>')

url='http://lz.book.sohu.com/chapter-1363259.html'
html=getHtml(url)
getTxt(html)
print 'finished!'
