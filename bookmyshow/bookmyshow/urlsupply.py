from datetime import date
import os.path
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
file=open(parent_directory+"/urls.txt", "a")

today=date.today()
date= int(today.strftime("%Y%m%d"))

count=int(0)
with open("url.txt") as f:
    # Content_list contains the read lines
    content_list = f.readlines()
    count+=1

for j in range(0,count):

    for i in range(0,7):
        temp=str(int(today.strftime("%Y%m")))+str(int(today.strftime("%d"))+i);
        file.write(str(content_list[j])+(temp)+"\n")

    file.close()