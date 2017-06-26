import os
import shutil
import re

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(l, key = alphanum_key)

def main():
	str1=os.getcwd()
	ls = natural_sort(os.listdir(str1))
	print(ls)
	print(str1+"/"+str1.split("_")[1]+" "+str(5)+".mkv")
	#return
	k = 1
	for i in ls:
		if ".mkv" in i and "ED" not in i and "OP" not in i:
			shutil.move(str1+"/"+i, str1+"/"+str1.split("_")[1]+" "+str(k)+".mkv")
			k+=1


main()
