import csv
import os
# Using datetime for date handling
import datetime

EXPENSES_FILE = 'expenses.csv'

def load_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
        with open(EXPENSES_FILE, 'r', newline='') as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
            return expenses
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading expenses: {e}")
        return []


def save_expenses(expenses):
    try:
        with open(EXPENSES_FILE, 'w', newline='') as file:
            fieldnames = ['date', 'description', 'amount', 'category']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for expense in expenses:
                for key in fieldnames:
                    expense.setdefault(key, '')
            writer.writerows(expenses)
    except IOError as e:
        print(f"Error saving expenses: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during saving: {e}")


def add_expense(date, description, amount, category):
    expenses = load_expenses()
    expenses.append({'date': date, 'description': description, 'amount': str(amount), 'category': category})
    save_expenses(expenses)
    print(f"Added: {date} - {description} - ${amount} [{category}]")


def view_expenses(filter_date=None):
    expenses = load_expenses()

    if filter_date:
        filtered_expenses = [expense for expense in expenses if expense.get('date') == filter_date]
    else:
        filtered_expenses = expenses

    if not filtered_expenses:
        if filter_date:
            print(f"No expenses found for date: {filter_date}")
        else:
            print("No expenses yet.")
        return

    if filter_date:
        print(f"\n--- Expenses for {filter_date} ---")
    else:
        print("\n--- All Expenses ---")

    for i, expense in enumerate(filtered_expenses, 1):
        date_str = expense.get('date', 'N/A')
        desc_str = expense.get('description', 'N/A')
        amount_str = expense.get('amount', '0')
        cat_str = expense.get('category', 'N/A')
        print(f"{i}. {date_str} - {desc_str} - ${amount_str} [{cat_str}]")

    print("--------------------\n")


def total_expenses():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        try:
            amount = float(expense.get('amount', 0))
            total += amount
        except (ValueError, TypeError):
            pass
    print(f"Total Expenses: ${total:.2f}")


# Refined main function
def main():
    while True:
        # Menu section remains the same
        print("\nExpense Tracker Menu")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Date")
        print("4. Total Expenses")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            date_str = input("Date (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue # Correct: continue is present

            description = input("Enter expense description: ")
            amount_str = input("Enter amount: ")
            category = input("Enter category: ")
            try:
                amount = float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a number.")
                continue

            add_expense(date_str, description, amount, category)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            date_to_filter = input("Enter date to filter by (YYYY-MM-DD): ")
            try:
                datetime.datetime.strptime(date_to_filter, '%Y-%m-%d')
                view_expenses(filter_date=date_to_filter)
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                continue # Enhancement: Added continue here

        elif choice == '4':
            total_expenses()

        elif choice == '5':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    if not os.path.exists(EXPENSES_FILE) or os.path.getsize(EXPENSES_FILE) == 0:
        save_expenses([])
    main()
