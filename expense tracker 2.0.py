expenses = []

# Function to add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    category = input("Enter category (Food/Travel/Shopping): ")
    month = input("Enter month (Example: September): ")

    expenses.append([desc, amount, category, month])

    print("Expense added successfully!\n")


# Function to view all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses found.")

    else:
        for item in expenses:
            print(f"Item: {item[0]}, Amount: {item[1]}, Category: {item[2]}, Month: {item[3]}")

    print()


# Function to search by category
def search_category():
    search = input("Enter category to search: ")

    print(f"\n--- Expenses in {search} ---")

    found = False

    for item in expenses:
        if item[2].lower() == search.lower():
            print(f"Item: {item[0]}, Amount: {item[1]}")
            found = True

    if not found:
        print("No matching expenses found.")

    print()


# Function to calculate category total
def category_total():
    search = input("Enter category: ")

    total = 0

    for item in expenses:
        if item[2].lower() == search.lower():
            total += item[1]

    print(f"\nTotal spent on {search}: {total}\n")


# Function to calculate monthly total
def monthly_total():
    search_month = input("Enter month: ")

    total = 0

    for item in expenses:
        if item[3].lower() == search_month.lower():
            total += item[1]

    print(f"\nTotal spent in {search_month}: {total}\n")


# Main menu
while True:
    print("===== Expense Tracker 2.0 =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. View Category Total")
    print("5. View Monthly Total")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        search_category()

    elif choice == "4":
        category_total()

    elif choice == "5":
        monthly_total()

    elif choice == "6":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice! Please try again.\n")