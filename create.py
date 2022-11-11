import csv  

header = ['name', 'area', 'country_code2', 'country_code3']
data = ['Afghanistan', 652090, 'AF', 'AFG']
myRow = [['United States', '12345', 'US', 'USA', 'USA', 'USA'],
        ['United Kingdom', '1234', "Britian"],
        ['Canada', '1234','CA']]

# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)


for x in range(len(myRow)):
    with open('countries.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow(myRow[x])  