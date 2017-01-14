# coding=utf-8
import re
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#获取网页
def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read().decode('utf-8')
  return html

#爬取想要的文字
def getTxt(html):
  # regg = '<div class="fun_list">([\s\S]*)<div class="pagination_wrap">'
  # 正则表达式
  regg = '<p><p>([\s\S]*)<div class="pagination_wrap">'
  txtre = re.compile(regg)
  # 存入数组
  items = txtre.findall(html)
  items[0] = replace(items[0])
  return items[0]

  # 替换不必要的字符
def replace(items):
  removeP = re.compile('</p><p>')
  removePslash = re.compile('</p></p>')
  removePr = re.compile('\*r')
  removePstar = re.compile('\*')
  removeClass = re.compile('<div class=".*?>')
  removeClassP = re.compile('</div>')
  # 省略号
  # removeNotFinished = re.compile('[\u4e00-\u9fa5]&&……')

  items = re.sub(removeP, "\r\n", items)
  items = re.sub(removePr, '', items)
  items = re.sub(removePstar, "", items)
  items = re.sub(removePslash, "\r\n", items)
  items = re.sub(removeClass, "", items)
  items = re.sub(removeClassP, "", items)
  # items = re.sub(removeNotFinished, "weiwandaixu", items)
  # 删除空白符
  items = items.strip()
  return items
#写入文件
def writeIntoTxt(x, url, item):
  chapter = '\n'+'_' * 50 + '分割线\n第' + str(x) + '章\n'
  print chapter
  enter = '\n\n'
  print url

  f = open('faxue.txt', 'a')
  f.write(chapter)
  f.write(url)
  f.write(enter)
  f.write(item)
  f.close()

# 制造url
def getUrl():
  list = range(0, 65)
  for x in list:
    d = x + 259
    url = '.html'
    url1 = '.html'
    url3 = 'http://lz.book.sohu.com/chapter-1363'
    url = url3 + str(d) + url1
    htmld = getHtml(url)
    item = getTxt(htmld)
    writeIntoTxt(x, url, item)

getUrl()
print 'finished!'
