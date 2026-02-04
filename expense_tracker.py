

def menu() :
    print("Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

expenses = [] 


def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    date = input("Enter date (YYYY-MM-DD): ")

    expense = {
        "category": category,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)
    print("Expense added !")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e['category']} | ${e['amount']} | {e['date']}")


while True :
    menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        view_expenses(expenses)
    elif choice == "3":
        calculate_total(expenses)
    elif choice == "4":
        delete_expense(expenses)
    elif choice == "5":
        print("Exiting Expense Tracker.")
        break
    else:
        print("Invalid choice. Please try again.")





    