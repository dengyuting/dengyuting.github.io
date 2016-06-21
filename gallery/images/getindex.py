import os

homedir = os.getcwd()
index = os.listdir(homedir)
#f = open('index.txt','w')
for url in index:
	listurl = "<a href=\'images/" + url + "\' data-gallery> \n  <img src=\'images/" + url + "\' alt=\" \"   style=\"width:200px;\"> \n</a>"
	print listurl
#print index
#f.close()
