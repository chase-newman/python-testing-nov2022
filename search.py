# file = open('13fseclist.txt')
# content = file.readlines()


# print(content[250])


# # string to search in file
# with open(r'13fseclist.txt', 'r') as fp:
#     # read all lines using readline()
#     lines = fp.readlines()
#     for row in lines:
#         # check if string present on a current line
#         word = 'ACE CONVERGENCE ACQU CORP'
#         #print(row.find(word))
#         # find() method returns -1 if the value is not found,
#         # if found it returns index of the first occurrence of the substring
#         if row.find(word) != -1:
#             print('string exists in file')
#             print(row)

# string to search in file
word = '021ESC 01 7'
with open(r'13fseclist.txt', 'r') as fp:
    # read all lines in a list
    lines = fp.readlines()
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print(word, 'string exists in file')
            print('Line Number:', lines.index(line))
            print('Line:', line)
            num = lines.index(line)
            print(num + 36)
            print(type(num))
        
   
# open the sample file used
file = open('13fseclist.txt')
  
# read the content of the file opened
content = file.readlines()
  



  
