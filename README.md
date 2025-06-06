# smart-finance-analyzer
A Python command-line app to manage personal finances. Load, add, update, and delete transactions from a CSV file, analyze totals by type, and generate financial reports. Designed for learning and built with core Python features—no external libraries.

Smart Personal Finance Analyzer

A Python command-line app to manage personal finances. Load, add, update, and delete transactions from a CSV file, analyze totals by type, and generate financial reports. Designed for learning and built with core Python features—no external libraries.

Features

Load transactions from a CSV file

Add, view, update, and delete financial records

Analyze totals by transaction type (credit, debit, transfer)

Generate text-based financial summaries

Save updated data back to CSV format

Basic error handling and logging for invalid input rows

Requirements

Python 3.x

No external libraries required

Getting Started

1. Clone this repository

git clone https://github.com/RAlvey1/smart-finance-analyzer.git


2. Change into the project directory

cd smart-finance-analyzer

3. Make sure financial_transactions.csv is in the same folder

4. Run the program

python Smart_Finance_Analyzer.py

Input File Format

CSV must have the following headers:

transaction_id,date,customer_id,amount,type,description

Example row:

1,2020-10-26,926,6478.39,credit,Expect series shake art again our.

Sample Output

Smart Personal Finance Analyzer
1. Load Transactions
2. Add Transaction
3. View Transactions
4. Update Transaction
5. Delete Transaction
6. Analyze Finances
7. Save Transactions
8. Generate Report
9. Exit
Select an option: 3

ID   Date           Customer  Amount     Type      Description
1    Oct 26, 2020   926       $6478.39   credit    Expect series shake art again our.
2    Jan 08, 2020   466       $1255.95   credit    Each left similar likely coach take.

Output Files

errors.txt: Lists skipped rows due to formatting issues

report_YYYYMMDD.txt: Summary report based on transaction data

Updated financial_transactions.csv: Reflects any changes made

Project Structure

smart-finance-analyzer/
├── Smart_Finance_Analyzer.py       # Main Python script
├── financial_transactions.csv      # Input file (must be provided)
├── errors.txt                      # Error log
├── report_YYYYMMDD.txt             # Financial report output
└── README.md                       # Project instructions

Known Limitations

Data exists only during the current session unless saved

No duplicate-checking for transaction IDs

Basic validation only (no advanced type enforcement)

Requires the CSV file to match the expected structure exactly

