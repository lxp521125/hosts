#coding:utf-8

import socket
import os
   #这个方法是直接调用标准C的system() 函数，仅仅在一个子终端运行系统命令，而不能获取命令执行后的返回信息。


def URL2IP():
   for oneurl in urllist.readlines():
       url=oneurl
    #    url=str(oneurl.strip())[7:]
       url = url.strip()
       print url
       try:
           ip =socket.gethostbyname(url)
           print ip
           iplist.writelines(str(ip)+"   "+url+ "\n")
       except:
           print "this URL 2 IP ERROR "

try:
    urllist=open("urllist.txt","r")
    iplist=open("iplist.txt","w")
    URL2IP()
    urllist.close()
    iplist.close()
 #   os.system('git commit -am "更新host"')
 #   os.system('git push')
    print "complete !"
except:
    print "ERROR !"
