
import csv
import os

EXPENSES_FILE = 'expenses.csv'

def load_expenses():
    """Load expenses from the CSV file."""
    if not os.path.exists(EXPENSES_FILE):
        return []
    with open(EXPENSES_FILE, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def save_expenses(expenses):
    """Save the list of expenses to the CSV file."""
    with open(EXPENSES_FILE, 'w', newline='') as file:
        fieldnames = ['description', 'amount', 'category']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(description, amount, category):
    """Add a new expense."""
    expenses = load_expenses()
    expenses.append({'description': description, 'amount': amount, 'category': category})
    save_expenses(expenses)
    print(f"Expense added: {description} - ${amount} [{category}]")

def view_expenses():
    """View all expenses."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['description']} - ${expense['amount']} [{expense['category']}]")

def total_expenses():
    """Calculate and display the total expenses."""
    expenses = load_expenses()
    total = sum(float(expense['amount']) for expense in expenses)
    print(f"Total Expenses: ${total:.2f}")

def main():
    """Main menu for the expense tracker."""
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category (e.g., Food, Transport): ")
            add_expense(description, amount, category)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
