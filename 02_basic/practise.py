#coding=utf-8

import urllib
import urllib2

values = {"Online User ID":"wm1206112003","Password":"nectest09"}
data = urllib.urlencode(values)
url = "https://www.walmartmoneycard.com/login"
request = urllib2.request(url,data)
response = urllib2.urlopen(request)
print response.read()


