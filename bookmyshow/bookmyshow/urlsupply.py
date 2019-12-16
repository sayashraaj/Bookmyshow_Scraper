from datetime import date


today=date.today()
date= int(today.strftime("%Y%m%d"))

for i in range(0,4):
    temp=str(int(today.strftime("%Y%m")))+str(int(today.strftime("%d"))+i);
    file.write("https://in.bookmyshow.com/buytickets/panipat-national-capital-region-ncr/movie-ncr-ET00072511-MT/"+(temp)+"\n")

file.close()