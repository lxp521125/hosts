#coding:utf-8

import socket

def URL2IP():
   for oneurl in urllist.readlines():
       url=oneurl
    #    url=str(oneurl.strip())[7:]
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
    print "complete !"
except:
    print "ERROR !"
