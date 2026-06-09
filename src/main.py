import csv

with open('data/raw/transactions.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader[1:]:  # Skip the header row
        print(row)