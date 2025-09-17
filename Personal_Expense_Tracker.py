import random
import math
from datetime import datetime

# List to store expenses
expenses = []

# Predefined tips for saving money
tips = [
    "Try cooking at home instead of eating out.",
    "Use public transport to save fuel costs.",
    "Set a monthly budget and stick to it.",
    "Avoid unnecessary subscriptions.",
    "Compare prices before shopping.",
    "Track your expenses daily to spot wasteful spending.",
    "Save a fixed percentage of your income every month.",
    "Use cash instead of credit cards to control spending.",
    "Buy in bulk for items you use regularly.",
    "Wait 24 hours before making non-essential purchases.",
]


# Function to add a new expense
def add_expense():
    amount = input("Enter expense amount: ₹")
    if amount.replace(".", "", 1).isdigit():  # check if input is number
        amount = float(amount)
    else:
        print("Invalid amount! Please enter a number.")
        return

    category = input("Enter expense category (Food, Travel, etc.): ")
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")

    expenses.append({"amount": amount, "category": category, "date": date})
    print(f"Expense added: ₹{amount} for {category} on {date}")
    print(f"💡 Tip: {random.choice(tips)}")


# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- Your Expenses ---")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. ₹{exp['amount']:.2f} | {exp['category']} | {exp['date']}")

    total = sum(exp["amount"] for exp in expenses)
    average = total / len(expenses)
    highest = max(exp["amount"] for exp in expenses)

    print(f"\nTotal spending: ₹{total:.2f}")
    print(f"Average spending: ₹{average:.2f}")
    print(f"Highest expense: ₹{highest:.2f}")
    print(f"💡 Tip: {random.choice(tips)}")


# Function to update an expense
def update_expense():
    view_expenses()
    if not expenses:
        return

    idx = input("Enter the expense number to update: ")
    if idx.isdigit():
        idx = int(idx) - 1
    else:
        print("Invalid input! Enter a number.")
        return

    if 0 <= idx < len(expenses):
        new_amount = input("Enter new amount: ₹")
        if new_amount.replace(".", "", 1).isdigit():
            new_amount = float(new_amount)
        else:
            print("Invalid amount!")
            return

        new_category = input("Enter new category: ")
        new_date = input("Enter new date (YYYY-MM-DD) or press enter for today: ")
        if not new_date:
            new_date = datetime.today().strftime("%Y-%m-%d")

        expenses[idx] = {
            "amount": new_amount,
            "category": new_category,
            "date": new_date,
        }
        print("Expense updated successfully!")
    else:
        print("Invalid expense number.")


# Function to delete an expense
def delete_expense():
    view_expenses()
    if not expenses:
        return

    idx = input("Enter the expense number to delete: ")
    if idx.isdigit():
        idx = int(idx) - 1
    else:
        print("Invalid input! Enter a number.")
        return

    if 0 <= idx < len(expenses):
        removed = expenses.pop(idx)
        print(
            f"Removed expense: ₹{removed['amount']} | {removed['category']} | {removed['date']}"
        )
    else:
        print("Invalid expense number.")


# Main menu loop
def main():
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            update_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Thank you for using the Expense Tracker! 💰")
            break
        else:
            print("Invalid choice! Please select 1-5.")


# Run the program
if __name__ == "__main__":
    main()
