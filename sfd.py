#encoding:UTF-8
# -*- coding: <encoding name> -*-
import requests #__version__ = 2.3.0 这里直接使用session，因为要先登陆 
from bs4 import BeautifulSoup #__version__ = 4.3.2

#加了下面3行就不会有问题了（不知道是哪个编码的问题'btnquery'应该是gbk）
import sys
reload(sys)
sys.setdefaultencoding('utf-8')  
s = requests.session() #创建一个session对象
for x in range(0,300):
	link="http://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=E30CE38558999470&ie=utf-8&f=8&rsv_bp=1&tn=84053098_dg&wd=site%3Awww.rong360.com%20%C3%A5%E2%80%9C%E9%A6%96%E4%BB%98%E8%B4%B7%E2%80%9D&oq=site%3Awww.rong360.com%20%E2%80%9C%E9%A6%96%E4%BB%98%E8%B4%B7%E2%80%9D&rsv_pq=e0317d7a00013fc3&rsv_t=800dUJ%2BHhby7OABqnGg2nekwAGqQJZQbZrsyHGDG7LaNK309lhlyhW6nbhtayLoUuPA&rsv_enter=1&pn="+str(x)+"&usm=1&bs=site%3Awww.rong360.com%20%E2%80%9C%E9%A6%96%E4%BB%98%E8%B4%B7%E2%80%9D&rsv_sid=undefined&_ss=1&clist=&hsug=&csor=0&pstg=4&_cr1=35508"
	r = s.get(link) 
	#print r.text
	#print bs
	bs = BeautifulSoup(r.content).find_all("a","m")
	n=range(0)
	for i in bs:
		if i["href"][:10] != 'http://www':
			str(n.append(i["href"]))

	for m in range(len(n)):
		link2=n[m]
		if s.get(link2).status_code == 404:
			print n[m], '\n'


		    

