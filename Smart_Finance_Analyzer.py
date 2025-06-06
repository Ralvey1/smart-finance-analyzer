import csv
from datetime import datetime

def load_transactions(filename='financial_transactions.csv'):
    transactions = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    parsed_date = datetime.strptime(row['date'], "%Y-%m-%d")
                    amount = float(row['amount'])
                    if row['type'] == 'debit':
                        amount *= -1
                    transaction = {
                        'transaction_id': int(row['transaction_id']),
                        'date': parsed_date,
                        'customer_id': int(row['customer_id']),
                        'amount': amount,
                        'type': row['type'],
                        'description': row['description']
                    }
                    transactions.append(transaction)
                except Exception:
                    print(f"Skipping invalid row: {row}")
        print(f"{len(transactions)} transactions loaded.")
    except FileNotFoundError:
        print("Error: File not found.")
    return transactions

def add_transaction(transactions):
    try:
        date_input = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, "%Y-%m-%d")
        customer_id_input = input("Enter customer ID: ")
        customer_id = int(customer_id_input)
        amount_input = input("Enter amount: ")
        amount = float(amount_input)
        trans_type = input("Enter type (credit/debit/transfer): ").lower()

        # Verbose type validation
        valid_type = False
        if trans_type == 'credit':
            valid_type = True
        elif trans_type == 'debit':
            valid_type = True
        elif trans_type == 'transfer':
            valid_type = True

        if not valid_type:
            print("Invalid transaction type.")
            return

        if trans_type == 'debit':
            amount *= -1

        description = input("Enter description: ")

        # Manual max transaction_id
        new_id = 0
        for t in transactions:
            if t['transaction_id'] > new_id:
                new_id = t['transaction_id']
        new_id += 1

        new_transaction = {
            'transaction_id': new_id,
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': trans_type,
            'description': description
        }

        transactions.append(new_transaction)
        print("Transaction added!")

     except Exception as e:
        print(f"Error: {e}")

def view_transactions(transactions):
    print(f"{'ID':<5}{'Date':<15}{'Customer':<10}{'Amount':<10}{'Type':<10}Description")
    print("-" * 60)
    for t in transactions:
        date_str = t['date'].strftime('%b %d, %Y')
        print(f"{t['transaction_id']:<5}{date_str:<15}{t['customer_id']:<10}${t['amount']:<10.2f}{t['type']:<10}{t['description']}")

def analyze_finances(transactions):
    totals = {'credit': 0, 'debit': 0, 'transfer': 0}
    for t in transactions:
        amt = abs(t['amount'])
        if t['type'] in totals:
            totals[t['type']] += amt

    net = 0
    for t in transactions:
        net += t['amount']
  
    print("\nFinancial Summary:")
    for key, val in totals.items():
        print(f"Total {key.title()}s: ${val:.2f}")
    print(f"Net Balance: ${net:.2f}")

def main():
    transactions = []
    while True:
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Analyze Finances")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            transactions = load_transactions()
        elif choice == '2':
            add_transaction(transactions)
        elif choice == '3':
            view_transactions(transactions)
        elif choice == '4':
            analyze_finances(transactions)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
   
