import csv
from datetime import datetime


EXPENSES_FILE = 'expenses.csv'
BUDGET_FILE = 'budget.csv'
SAVINGS_GOAL_FILE = 'savings_goal.csv'



def initialize_files():
    for file in [EXPENSES_FILE, BUDGET_FILE, SAVINGS_GOAL_FILE]:
        try:
            with open(file, 'r'):
                pass
        except FileNotFoundError:
            with open(file, 'w') as f:
                if file == EXPENSES_FILE:
                    f.write('Date,Description,Amount\n')
                elif file == BUDGET_FILE:
                    f.write('Month,Budget\n')
                elif file == SAVINGS_GOAL_FILE:
                    f.write('Month,Saving Goal,Current Savings\n')



def add_expense():
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount: $"))

    with open(EXPENSES_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, description, amount])

    print(f"Added expense: {description} - ${amount} on {date}")



def view_expenses():
    with open(EXPENSES_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        expenses = list(reader)

    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpenses:")
        for expense in expenses:
            print(f"{expense[0]} - {expense[1]} - ${expense[2]}")
        print("\n")



def set_budget():
    month = input("Enter the month (YYYY-MM): ")
    budget = float(input("Enter your monthly budget: $"))

    with open(BUDGET_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([month, budget])

    print(f"Budget of ${budget} set for {month}\n")



def view_budget(month=None):
    if month is None:
        month = input("Enter the month (YYYY-MM): ")

    with open(BUDGET_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == month:
                print(f"Budget for {month}: ${row[1]}")
                return float(row[1])
    
    print(f"No budget set for {month}.")
    return 0



def set_savings_goal():
    month = input("Enter the month (YYYY-MM): ")
    goal = float(input("Enter your savings goal: $"))

    with open(SAVINGS_GOAL_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([month, goal, 0])

    print(f"Savings goal of ${goal} set for {month}\n")



def add_savings():
    month = input("Enter the month (YYYY-MM): ")
    amount = float(input("Enter the amount to add to savings: $"))

    updated = False
    rows = []

    with open(SAVINGS_GOAL_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == month:
                row[2] = float(row[2]) + amount  # Update current savings
                updated = True
            rows.append(row)

    if updated:
        with open(SAVINGS_GOAL_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        print(f"Added ${amount} to savings for {month}.")
    else:
        print(f"No savings goal set for {month}.\n")



def view_savings_goal(month=None):
    if month is None:
        month = input("Enter the month (YYYY-MM): ")

    with open(SAVINGS_GOAL_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == month:
                print(f"Savings goal for {month}: ${row[1]}")
                print(f"Current savings: ${row[2]}")
                return float(row[1]), float(row[2])
    
    print(f"No savings goal set for {month}.")
    return 0, 0



def generate_report():
    month = input("Enter the month to generate a report for (YYYY-MM): ")
    total_expenses = 0


    with open(EXPENSES_FILE, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].startswith(month):
                total_expenses += float(row[2])


    budget = view_budget(month)
    goal, current_savings = view_savings_goal(month)

    print("\n=== Monthly Report ===")
    print(f"Total Expenses: ${total_expenses}")
    print(f"Budget: ${budget}")
    if budget > 0:
        print(f"Budget Remaining: ${budget - total_expenses}")
    print(f"Savings Goal: ${goal}")
    print(f"Current Savings: ${current_savings}")
    print("======================\n")



def main():
    initialize_files()

    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Set Monthly Budget")
        print("4. View Monthly Budget")
        print("5. Set Savings Goal")
        print("6. Add Savings")
        print("7. View Savings Goal")
        print("8. Generate Monthly Report")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            view_budget()
        elif choice == '5':
            set_savings_goal()
        elif choice == '6':
            add_savings()
        elif choice == '7':
            view_savings_goal()
        elif choice == '8':
            generate_report()
        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
    main()