import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category (Food, Travel, Shopping, etc.): ")
        note = input("Enter a short note: ")

        expense = {
            "amount": amount,
            "category": category,
            "note": note,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount entered.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- EXPENSE LIST ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ${exp['amount']} | {exp['note']}")


def total_expense(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ${total:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n--- PERSONAL EXPENSE TRACKER ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expense")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            total_expense(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
