import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    category = input("Category (jaise Food, Travel): ")
    amount = float(input("Amount: "))
    expenses.append({"category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense add ho gaya!\n")

def view_expenses(expenses):
    if not expenses:
        print("Koi expense nahi hai abhi.\n")
        return
    print("\n--- Saare Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['category']} - Rs.{e['amount']}")
    print()

def calculate_total(expenses):
    total = sum(e["amount"] for e in expenses)
    print(f"Total Expense: Rs.{total}\n")

def main():
    expenses = load_expenses()
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            calculate_total(expenses)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Galat choice, dobara try karo.\n")

if __name__ == "__main__":
    main()