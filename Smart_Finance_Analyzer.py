import csv
from datetime import datetime

TRANSACTION_TYPES = {"credit", "debit", "transfer"}

def parse_transaction(row):
    try:
        parsed_date = datetime.strptime(row["date"], "%Y-%m-%d")
        amount = float(row["amount"])
        if row["type"] == "debit":
            amount *= -1
        if row["type"] not in TRANSACTION_TYPES:
            raise ValueError("Invalid transaction type.")
        return {
            "transaction_id": int(row["transaction_id"]),
            "date": parsed_date,
            "customer_id": int(row["customer_id"]),
            "amount": amount,
            "type": row["type"],
            "description": row["description"],
        }
    except Exception:
        print(f"Skipping invalid row: {row}")
        return None

def load_transactions(filename="financial_transactions.csv"):
    transactions = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transaction = parse_transaction(row)
                if transaction:
                    transactions.append(transaction)
        print(f"{len(transactions)} transactions loaded.")
    except FileNotFoundError:
        print("Error: File not found.")
    return transactions

def save_transactions(transactions, filename="financial_transactions.csv"):
    with open(filename, mode='w', newline='') as file:
        fieldnames = ["transaction_id", "date", "customer_id", "amount", "type", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for t in transactions:
            writer.writerow({
                "transaction_id": t["transaction_id"],
                "date": t["date"].strftime("%Y-%m-%d"),
                "customer_id": t["customer_id"],
                "amount": abs(t["amount"]),
                "type": t["type"],
                "description": t["description"],
            })
    print("Transactions saved.")

def add_transaction(transactions):
    try:
        date_input = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_input, "%Y-%m-%d")

        customer_id = int(input("Enter customer ID: "))
        amount = float(input("Enter amount: "))
        trans_type = input("Enter type (credit/debit/transfer): ").lower()

        if trans_type not in TRANSACTION_TYPES:
            print("Invalid transaction type.")
            return

        if trans_type == "debit":
            amount *= -1

        description = input("Enter description: ")
        new_id = max((t["transaction_id"] for t in transactions), default=0) + 1

        new_transaction = {
            "transaction_id": new_id,
            "date": date,
            "customer_id": customer_id,
            "amount": amount,
            "type": trans_type,
            "description": description,
        }

        transactions.append(new_transaction)
        print("Transaction added!")

    except Exception as e:
        print(f"Error: {e}")

def view_transactions(transactions):
    if not transactions:
        print("No transactions to display.")
        return

    header = (
        f"{'ID':<5}{'Date':<15}{'Customer':<10}"
        f"{'Amount':<10}{'Type':<10}Description"
    )
    print(header)
    print("-" * 60)
    for t in transactions:
        date_str = t["date"].strftime("%b %d, %Y")
        line = (
            f"{t['transaction_id']:<5}{date_str:<15}{t['customer_id']:<10}"
            f"${t['amount']:<10.2f}{t['type']:<10}{t['description']}"
        )
        print(line)

def analyze_finances(transactions):
    totals = {'credit': 0, 'debit': 0, 'transfer': 0}
    net = 0
    for t in transactions:
        amt = abs(t['amount'])
        if t['type'] in totals:
            totals[t['type']] += amt
        net += t['amount']

    print("\nFinancial Summary:")
    for key, val in totals.items():
        print(f"Total {key.title()}s: ${val:.2f}")
    print(f"Net Balance: ${net:.2f}")

def edit_transaction(transactions):
    try:
        trans_id = int(input("Enter transaction ID to edit: "))
        t = next((tx for tx in transactions if tx["transaction_id"] == trans_id), None)
        if not t:
            print("Transaction not found.")
            return

        print("Press Enter to keep the current value.")
        date_input = input(f"Date ({t['date'].strftime('%Y-%m-%d')}): ")
        if date_input:
            t['date'] = datetime.strptime(date_input, "%Y-%m-%d")

        cust_input = input(f"Customer ID ({t['customer_id']}): ")
        if cust_input:
            t['customer_id'] = int(cust_input)

        amount_input = input(f"Amount ({abs(t['amount'])}): ")
        if amount_input:
            amount = float(amount_input)
            t['amount'] = -amount if t['type'] == 'debit' else amount

        type_input = input(f"Type ({t['type']}): ").lower()
        if type_input:
            if type_input in TRANSACTION_TYPES:
                if type_input == 'debit':
                    t['amount'] = -abs(t['amount'])
                else:
                    t['amount'] = abs(t['amount'])
                t['type'] = type_input
            else:
                print("Invalid type. Keeping old value.")

        desc_input = input(f"Description ({t['description']}): ")
        if desc_input:
            t['description'] = desc_input

        print("Transaction updated.")
    except Exception as e:
        print(f"Error: {e}")

def delete_transaction(transactions):
    try:
        trans_id = int(input("Enter transaction ID to delete: "))
        index = next((i for i, tx in enumerate(transactions) if tx["transaction_id"] == trans_id), None)
        if index is not None:
            transactions.pop(index)
            print("Transaction deleted.")
        else:
            print("Transaction not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    transactions = []
    while True:
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Edit Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Exit")

        choice = input("Select an option: ")
        if choice == '1':
            transactions = load_transactions()
        elif choice == '2':
            add_transaction(transactions)
        elif choice == '3':
            view_transactions(transactions)
        elif choice == '4':
            edit_transaction(transactions)
        elif choice == '5':
            delete_transaction(transactions)
        elif choice == '6':
            analyze_finances(transactions)
        elif choice == '7':
            save_transactions(transactions)
        elif choice == '8':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()