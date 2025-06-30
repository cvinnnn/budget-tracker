# Budget Tracker Project
# By Calvin Shetty
# This programme tracks income and expenses, saves them to a file, and calculates current balance.
total_income = 0
total_expense = 0
# Load saved transactions from file
try:
    with open("transactions.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            entry_type, amount = line.split(",")
            amount = float(amount)
            if entry_type == "income":
                total_income += amount
            elif entry_type == "expense":
                total_expense += amount
except FileNotFoundError:
    pass # If the file doesn't exist yet, just start with 0s
def add_income():
    try:
        income = float(input("Enter your income: £"))
        with open("transactions.txt", "a") as file:
            file.write(f"income,{income}\n")
        print(f"£{income} successfully added to income balance.")
        return income
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0
def add_expense():
    try:
        expense = float(input("Enter your expense: £"))
        with open("transactions.txt", "a") as file:
            file.write(f"expense,{expense}\n")
        print(f"£{expense} successfully added to your balance.")
        return expense
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0
while True:
    print("\nWelcome to your budget tracker!")
    print("1. Add your income")
    print("2. Add your expenses")
    print("3. View your balance")
    print("4. Exit")

    choice = input("Choose an option 1-4 :) ")

    if choice == "1":
        total_income += add_income()
    elif choice == "2":
        total_expense += add_expense()
    elif choice == "3":
        balance = total_income - total_expense
        print(f"\nTotal income: £{total_income}")
        print(f"Total expenses: £{total_expense}")
        print(f"Current balance: £{balance}")
    elif choice == "4":
        print("Exiting budget tracker. Bye-bye!")
        break # The loop is stopped and the programme therefore ends.
    else:
        print("Invalid choice. Please select an option between 1 and 4")
