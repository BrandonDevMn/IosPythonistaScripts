# import needs libs
import clipboard
import xml.etree.ElementTree as XmlET

# flatten the xmlx structure 
def getPaths(text):
	# parse the text xml coming in
	xml = XmlET.fromstring(text)
	# go
	getPaths_helper(xml, "./")

# helper runction
def getPaths_helper(xml, parentPath):
	# get list
	children = xml.iter()
	# loop over children
	for child in children:
		print(child.text)

# pull text from clipboard - "clean" the text
xml = clipboard.get()

# get paths
paths = getPaths(xml)

# print paths
print(paths)
