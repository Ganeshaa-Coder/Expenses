import csv
import os

EXPENSES_FILE = 'expenses.csv'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w', newline='') as file:
        fieldnames = ['description', 'amount', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(description, amount, category):
    expenses = load_expenses()
    expenses.append({'description': description, 'amount': amount, 'category': category})
    save_expenses(expenses)
    print(f"Added: {description} - ${amount} [{category}]")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return
    for i, expense in enumerate(expenses, 1):
        print(f"{i}. {expense['description']} - ${expense['amount']} [{expense['category']}]")

def total_expenses():
    expenses = load_expenses()
    total = sum(float(e['amount']) for e in expenses)
    print(f"Total: ${total:.2f}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Description: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            add_expense(description, amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

