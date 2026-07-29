import json


def menu():
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Show expenses by category")
    print("5. Exit")


def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    description = input("Enter description: ")

    if not description:
        print("Description cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    category = input("Enter category: ")

    if not category:
        print("Category cannot be empty.")
        return

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    save_expenses()

    print("Expense added successfully.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSES =====")

    for expense in expenses:
        print(f"Description: {expense['description']}")
        print(f"Amount: €{expense['amount']:.2f}")
        print(f"Category: {expense['category']}")
        print("--------------------")


def show_total():
    if not expenses:
        print("No expenses found.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"Total expenses: €{total:.2f}")


def show_by_category():
    if not expenses:
        print("No expenses found.")
        return

    category = input("Enter category: ")

    total = 0

    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]

    print(f"Total for {category}: €{total:.2f}")


expenses = load_expenses()


while True:
    menu()

    option = input("Choose an option: ")

    if option == "1":
        add_expense()

    elif option == "2":
        view_expenses()

    elif option == "3":
        show_total()

    elif option == "4":
        show_by_category()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
