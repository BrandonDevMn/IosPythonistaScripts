# imports
import dialogs
import xml.etree.ElementTree as XmlET

# defines a method to open a file picker
def pickFilePath():
	# pick the file - result is the path
	return dialogs.pick_document(types=['public.data'])
	
# defines a method to load a file by path
def loadFileByPath(filePath):
	# save rhe spot for data
	data = ""
	# open the file by path
	with open(filePath, 'r') as f:
		# read the text from the file
		data = f.read()
	# return the found data
	return data;

def parseXml(sXml):
	return XmlET.ElementTree(sXml)

# defines our MAIN function
def viewPickedOpml():
	# have the use pick a file path
	filePath = pickFilePath()
	# verify the file path
	if not filePath.endswith(".opml"):
		# if we have the wrong file, tell the user and stop
		print ("ERROR: wrong file type")
		return ""
	# load file
	text = loadFileByPath(filePath)
	# parse file
	xml = parseXml(text)
	
# GO
viewPickedOpml()
