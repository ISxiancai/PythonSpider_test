#!/usr/bin/python
#  coding: utf-8
import urllib2
import re

class Spider:
    def __init__(self):
        self.page = 2
        self.switch = True

    def loadPage(self):
        print 'loading...'
        url = "http://www.neihanpa.com/wenzi/index_"+str(self.page)+".html"
        headers = {"User-Agent":"Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"}
        request = urllib2.Request(url,headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
        # print html
        pattern = re.compile('<div\sclass="desc">(.*?)</div>',re.S)
        content_list = pattern.findall(html)
        # print content_list[0]
        self.dealPage(content_list)
    def writePage(self,content):
        print 'writing...'
        with open("duanzi.txt",'a')as f:
            f.write(content+'\n')

    def dealPage(self,content_list):
        print 'dealwith it...'
        for content in content_list:
            self.writePage(content)
    def startWork(self):
        while self.switch:
            self.loadPage()

            command = raw_input("going ? Enter (exit->quit)")
            if command == 'quit':
                self.switch = False
            else:
                print 'next ...'
                self.page += 1
        print 'thank you for using...'

if __name__ == '__main__':
    duanzi = Spider()
    duanzi.startWork()

