# example rss: http://www.theverge.com/apple/rss/index.xml
# import needs libs
import clipboard
import requests
import xml.etree.ElementTree as XmlET

# a function that takes in a url and prints rss
def pullRss(url):
	# verify its a url
	if not url.startswith("http"):
		print("ERROR: invalid url")
		return ""
	# call url
	rss = get(url)
	# print the rss
	parseRss(rss)
	
# parse the xml
def parseRss(rss):
	print(rss)
	# parse file
	xml = XmlET.fromstring(rss)

# a function to call a url
def get(URL):
	r = requests.get(url = URL)
	return r.text

# pull text from clipboard - "clean" the text
url = clipboard.get()

# GO
pullRss(url)
