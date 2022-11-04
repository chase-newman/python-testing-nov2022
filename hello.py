import csv
from csv import writer


def append_list_as_row(file_name, list_of_elem):
     with open('securitieslist.csv', 'a+', newline='') as write_obj:
         csv_writer = writer(write_obj)
         csv_writer.writerow(list_of_elem)

row_contents = ["Second Test", "COM", "112ABC44", "786", "11234", "SH", "Call", "Discretion", "Managers", "Sole", "Shared", "None"]

x = 0

for x in range(0,3):
    append_list_as_row('securitieslist.csv', row_contents)
    x + 1


# data = ["This", "is", "a", "Test"]


# with open('example.csv','w') as file:
#     writer = csv.writer(file)
#     writer.writerow(data)
    

# file = open('securities.csv')

# type(file)

# csvreader = csv.reader(file)

# header = []
# header = next(csvreader)
# print(header)

# first_name = input("What's your first name? ")
# print(first_name)