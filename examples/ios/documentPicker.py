# imports
import dialogs

# pick the file - result is the path
filePath = dialogs.pick_document(types=['public.data'])

# save a spot for the data
data = ""

# open the file by path
with open(filePath, 'r') as f:
		# read the text from the file
		data = f.read()

# print the picked data to the console
print(data)
