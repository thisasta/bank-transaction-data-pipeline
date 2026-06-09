import csv

with open('data/raw/transactions.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["transaction_id"], row["amount"], row["currency"])