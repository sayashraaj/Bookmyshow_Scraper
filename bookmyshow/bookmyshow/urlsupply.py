from datetime import date
#Finding path
import os.path
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
file=open(parent_directory+"/urls.txt", "a")
#Getting system date
today=date.today()
date= int(today.strftime("%Y%m%d"))

count=int(0)
#Input URLs
with open("url.txt") as f:
    # Content_list contains the read lines
    content_list = f.readlines()

f = "url.txt"
with open(f, 'r') as f:
    for line in f:
        count += 1.

print(content_list) #To test if content_list is giving proper output

for j in range(0,int(count)):
# x is the string variable which is altered to add a 0 digit if the int(day)<10
    for i in range(0,4):
        if(int(today.strftime("%d"))+i<10):
            x='0'+str(int(today.strftime("%d"))+i)
        temp=str(int(today.strftime("%Y%m")))+x;

        url=str(content_list[j])
        print(url[:-9])
        file.write((url[:-9])+(temp)+"\n")
file.close()