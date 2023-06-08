import json
import os

# Function to load expenses from a JSON file
def load_expenses():
    if not os.path.exists("expenses.json"):
        return []
    
    with open("expenses.json") as file:
        return json.load(file)

# Function to save expenses to a JSON file
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

# Function to add a new expense
def add_expense():
    description = input("Enter a description for the expense: ")
    amount = float(input("Enter the amount spent: "))
    
    expenses = load_expenses()
    expenses.append({"description": description, "amount": amount})
    save_expenses(expenses)
    
    print("Expense added successfully.")

# Function to view all expenses
def view_expenses():
    expenses = load_expenses()
    
    if not expenses:
        print("No expenses found.")
        return
    
    total_amount = 0
    for expense in expenses:
        description = expense["description"]
        amount = expense["amount"]
        total_amount += amount
        print(f"{description}: ${amount:.2f}")
    
    print(f"Total expenses: ${total_amount:.2f}")

# Main function
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete expense")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Expense Deleted.")    
        elif choice == "4":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Function to delete an expense
def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("Select an expense to delete:")
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {expense['description']} - ${expense['amount']:.2f}")

    while True:
        choice = input("Enter the number of the expense to delete (or 0 to cancel): ")

        if choice == '0':
            print("Deletion canceled.")
            return

        try:
            choice = int(choice)
            if 1 <= choice <= len(expenses):
                deleted_expense = expenses.pop(choice - 1)
                save_expenses(expenses)
                print(f"Deleted expense: {deleted_expense['description']} - ${deleted_expense['amount']:.2f}")
                return
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please enter a number.")

# Main function
def main():
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Thank you for using Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")



