import csv

income_count = 0
expense_count = 0
verification_count = 0
income_total = 0
expense_total = 0
invalid_currency_count = 0
invalid_amount_count = 0

with open('data/raw/transactions.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:

        if row["currency"] != "EUR":
            print("Skipping transaction: ", row["transaction_id"], ", unsupported currency: ", row["currency"])
            invalid_currency_count += 1
            continue    

        try:
            float_amount = float(row["amount"])
        except ValueError:
            print("Skipping transaction: ", row["transaction_id"], ", invalid amount: ", row["amount"])
            invalid_amount_count += 1
            continue

        if float_amount > 0:
            cashflow_type = "income"
            income_total += float_amount
            income_count += 1
        elif float_amount < 0:
            cashflow_type = "expense"
            expense_total -= float_amount   
            expense_count += 1
        else:
            cashflow_type = "account-verification"
            verification_count += 1

        print(row["transaction_id"], float_amount, cashflow_type)  

    print("\nIncome transactions: ", income_count)
    print("Expense transactions: ", expense_count)
    print("Account verifications: ", verification_count)
    print("\nTotal income: ", income_total)
    print("Total expenses: ", expense_total)
    print("Net total: ", income_total - expense_total)
    print("\nInvalid currency transactions: ", invalid_currency_count)
    print("Invalid amount transactions: ", invalid_amount_count)