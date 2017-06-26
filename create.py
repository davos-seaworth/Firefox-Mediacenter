import sys
import os
import getpass
import re
from shutil import copyfile

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def getFileNames(dir):
	try:
		filelist = os.listdir(dir)
	except FileNotFoundError:
		print("Directory not found. Does it exist? Did you enter it correctly?")
	filelist.sort()
	return filelist

def createMainTextFile(nameList):
	fl = open("names.txt","w")
	for i in nameList:
		fl.write(i+"\n")
	fl.close()

def getSubFileList(dir, title):
	allfiles = getFileNames(dir+"/"+title)
	mkvlist = []
	for i in allfiles:
		if i[-4:]==".mkv" and "[" not in i:
			mkvlist.append(i)
	mkvlist.sort()
	print(title)
	mkvlist = natural_sort(mkvlist)
	fl = open(dir+"/"+title+"/"+title+".txt","w")
	print(dir+"/"+title+".txt")
	for i in mkvlist:
		fl.write(i+"\n")
	fl.close()

#THIS FUNCTION DOES THE <title>.txt files for FRANCHISES ONLY
#THE SPLIT ON @ IS A FORM THING THAT MUST BE THERE, ALL FRANCHISES MUST CONFORM
def getSubFileList2(dir, title):
	allfiles = getFileNames(dir+"/"+title)
	mkvlist = []
	for i in allfiles:
		if i[-4:]==".mkv" and "[" not in i:
			mkvlist.append(i)
	mkvlist.sort()
	print(title)
	mkvlist = natural_sort(mkvlist)
	fl = open(dir+"/"+title+"/"+title.split("_")[1]+".txt","w")
	print(dir+"/"+title.split("_")[1]+".txt")
	for i in mkvlist:
		fl.write(i+"\n")
	fl.close()



#This sets up names.txt and subseries <title>.txt files, setting up fileDisplayArea

def getFranchiseFileList(dir, title):
	print("\n\n\n\n")
	allfiles = getFileNames(dir+"/"+title)
	subList = []
	for i in allfiles:
		if "." not in i:
			subList.append(i)
	print(subList)
	print("\n\n\n\n")
	copyfile(dir[:len(dir)-5]+"Franchise.html",dir+"/"+title+"/"+title+".html")
	print(allfiles)
	print(title)
	subList = natural_sort(subList)
	fl = open(dir+"/"+title+"/names.txt","w")
	for i in subList:
		fl.write(i+"\n")
	fl.close()
	for i in subList:
		getSubFileList2(dir+"/"+title,i)


def main():
	root_dir = "/home/davos/.mediacenter/MEdia"
	#root_dir = input("Enter the root directory from which to create metadata:\n")
	print(root_dir)
	if root_dir[0]=="~":
		root_dir = "/home/"+getpass.getuser()+root_dir[1:]
	print(root_dir)
	titles = getFileNames(root_dir)
	createMainTextFile(titles)

	for i in titles:
		if "Franchise" not in i:
			getSubFileList(root_dir,i)
		else:
			getFranchiseFileList(root_dir,i)



main()
