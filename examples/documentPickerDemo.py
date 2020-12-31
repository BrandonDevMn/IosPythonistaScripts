import dialogs

# pick the file - result is the path
filePath = dialogs.pick_document(types=['public.data'])

# open the file by path
with open(filePath, 'r') as f:
		# read the text from the file
    data = f.read()
