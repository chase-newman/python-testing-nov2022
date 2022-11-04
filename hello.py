import csv

date = ["This", "is", "a", "Test"]


with open('example.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(date)
    

# file = open('securities.csv')

# type(file)

# csvreader = csv.reader(file)

# header = []
# header = next(csvreader)
# print(header)

# first_name = input("What's your first name? ")
# print(first_name)