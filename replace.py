# import csv

# inputfile = csv.reader(open('dates.csv','r'))
# outputfile = open('placelist.txt','w')

# i=0

# for row in inputfile:
#     place = row[1].replace('1/8/2022')
#     print(place)
#     outputfile.write(place+'\n')
#     i+=1
    
    
text = open("dates.csv", "r")
text = ''.join([i for i in text]) \
    .replace("1/8/2022", "8/1/2022")
x = open("output.csv","w")
x.writelines(text)
x.close()