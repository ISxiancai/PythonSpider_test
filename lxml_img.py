#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2
from lxml import etree

def loadPage(url):
    print 'loading...'
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)
    link_list = content.xpath('//div[@class="t_con cleafix"]/div[@class="col2_right j_threadlist_li_right "]/div/div/a/@href')
    #组合为每个帖子的链接
    for link in link_list:
        fulllink = "http://tieba.baidu.com" + link
        # print fulllink
        loadImage(fulllink)
#去除每个帖子里的每个图片的链接
def loadImage(linkk):
    print 'loading Image...'
    headers = {"User-Agent" :
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)"
                   " AppleWebKit/535.11 (KHTML, like Gecko) Chrom"
                   "e/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(linkk,headers=headers)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)
    link_list = content.xpath('//img[@class="BDE_Image"]/@src')
    print 'download...'
    for link in link_list:
        # print link

        writeImage(link)

def writeImage(link,i):
    # 文件写入
    headers = {"User-Agent" :
                   "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0)"
                   " AppleWebKit/535.11 (KHTML, like Gecko) Chrom"
                   "e/17.0.963.56 Safari/535.11"}
    request = urllib2.Request(link,headers=headers)
    image = urllib2.urlopen(request).read()
    filename = 'D:/WORK/PythonTest/test02/lxml_ing/'+link[-10:]
    print filename
    with open(filename, "wb") as f:
        f.write(image)
        print "image->",'->' ,'*'* 30

def tiebaSpider(url, beginPage, endPage):
    """
        作用：贴吧爬虫调度器，负责组合处理每个页面的url
        url : 贴吧url的前部分
        beginPage : 起始页
        endPage : 结束页
    """
    print 'now we go ...'
    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50
        fullurl = url + "&pn=" + str(pn)
        loadPage(fullurl)
        print "谢谢使用"

if __name__ == "__main__":
    kw = raw_input("请输入需要爬取的贴吧名:")
    beginPage = int(raw_input("请输入起始页："))
    endPage = int(raw_input("请输入结束页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.urlencode({"kw": kw})
    fullurl = url + key
    tiebaSpider(fullurl, beginPage, endPage)




