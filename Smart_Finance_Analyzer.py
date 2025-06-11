# Cleaned and corrected version of the Smart Personal Finance Analyzer

import csv
from datetime import datetime

# Define transaction types globally
TRANSACTION_TYPES = {"credit", "debit", "transfer"}

def parse_transaction(row):
    """Convert a CSV row into a transaction dictionary."""
    try:
        parsed_date = datetime.strptime(row["date"], "%Y-%m-%d")
        amount = float(row["amount"])
        if row["type"] == "debit":
            amount *= -1
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
    """Read transactions from a CSV file."""
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

def add_transaction(transactions):
    """Prompt the user for a new transaction and append it to the list."""
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
    """Display a table of all transactions."""
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
    """Print totals by transaction type and the net balance."""
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

def main():
    """Command-line interface for the finance analyzer."""
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

