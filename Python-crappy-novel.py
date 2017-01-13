# coding=utf-8
import re
import urllib

def getHtml(url):
  page = urllib.urlopen(url)
  html = page.read()

  return html


def getTxt(html):
  regg = '<div class="book_con">([\s\S]*)<div class="pagination_wrap">'
  # reg = r'src="(\S*\.jpg)"'
  txtre = re.compile(regg)
  # html = html.decode('utf-8').encode('gbk')
  items = txtre.findall(html)
  
  print items[0].decode('utf-8')
  removeImg = re.compile('<img.*?>')
  removeImg = re.compile('<img.*?>')
  removeImg = re.compile('<img.*?>')


url = 'http://lz.book.sohu.com/chapter-1363259.html'
htmld = getHtml(url)
getTxt(htmld)
print 'finished!'
