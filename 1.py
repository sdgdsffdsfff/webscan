#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lcy
# @Date:   2015-07-22 10:41:17
# @Last Modified by:   Lcy
# @Last Modified time: 2015-07-22 10:49:44
import urllib2
import re
import sys
import socket

def curl(ip,first):
	#设置ip代理，
	#proxy_handler = urllib2.ProxyHandler({"http" : 'http://127.0.0.1:1080'})
	#null_proxy_handler = urllib2.ProxyHandler({})
	#opener = urllib2.build_opener(proxy_handler)
	#urllib2.install_opener(opener)
	uri = "http://www.bing.com/search?q=ip%3A" + ip +"&go=%E6%8F%90%E4%BA%A4&qs=n&first="+ str(first) +"&form=QBRE&pq=ip%3A" + ip +"&sc=0-0&sp=-1&sk=&cvid=5e52385772e24683a0bdf047de60abfc"
	request = urllib2.Request(uri)
	request.add_header('User-Agent', 'BaiduSpider')
	response = urllib2.urlopen(request, timeout=10)
	res = response.read()
	return res
def getIp(domain):
    myaddr = socket.getaddrinfo(domain,'http')[0][4][0]
    return myaddr
def get(ip):
	ip = getIp(ip)
	print "[+] Query IP:" + ip + "\n"
	rev = []
	first = 1
	while True:
		res = curl(ip,first)
		first = first + 10
		r = re.findall(r'<h2><a href="((http|https):\/\/([\w|\.]+)\/)([\w|\/|&|=|\.|\?]+)?" h="ID=\w+,\w+\.\w+">',res)
		for i in r:
			print "[+] " + i[0]
			rev.append(i[0])
		m = re.search(r'<div class="sw_next">', res)
		if not m:
			break
	result = list(set(rev))
	return result
if __name__ == "__main__":
	print u"""------------------------------------------------------------------------------
必应旁站查询                                                    qq:1141056911
                                                                       By Lcy
                                                            http://phpinfo.me
------------------------------------------------------------------------------
	"""
	if len(sys.argv) != 2:
		print "Usage: %s ip" % sys.argv[0]
		exit()	
	urllist = get(sys.argv[1])
	result = ""
	for i in urllist:
		result = result + i + "\r\n"
	f = open("Result.txt","w")
	f.write(result)
	f.close()
	print u"\r\n结果已经保存为Result.txt"
