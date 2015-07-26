import json  
import urllib2  
from threading import Thread


print "name"+"," +"likeCount"
access_token="Your Access Token"

def th(ur):  
    j =urllib2.urlopen('https://graph.facebook.com/'+ur'?fields=id,name,likes&access_token='+access_token)
    js = json.load(j)
    print str(js['name'])+","+str(js['likes'])

threadlist = []

medialist = open("medialist.txt").read()  
medialist = medialist.split("\n")


for u in medialist:  
    t = Thread(target = th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:  
    b.join()
