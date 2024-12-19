def expense_analysis(expenses):
    if not expenses:
        return {"highest": None, "lowest": None, "average": None}

    highest = None
    highest_amount = -float('inf')  # Initialize to negative infinity
    lowest = None
    lowest_amount = float('inf')    # Initialize to positive infinity
    total = 0

    for category, amount in expenses.items():
        if amount > highest_amount:
            highest = category
            highest_amount = amount
        if amount < lowest_amount:
            lowest = category
            lowest_amount = amount
        total += amount

    average = total / len(expenses)
    return {
        "highest": (highest, highest_amount),
        "lowest": (lowest, lowest_amount),
        "average": average,
    }


def display_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nYour Expenses:")
        for category, amount in expenses.items():
            print(f"  - {category}: ₱{amount:.2f}")

def main():
    expenses = {}
    
    while True:
        print("\n- Expense Tracker -")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            category = input("Enter expense category (e.g Clothing, Food, Savings): ")
            amount = input("Enter amount spent: ")
            
            valid_amount = True
            decimal_count = 0
            for char in amount:
                if char == '.':
                    decimal_count += 1
                elif not char.isdigit():
                    valid_amount = False
                    break
            
            if valid_amount and decimal_count <= 1:
                amount = float(amount)
                if category in expenses:
                    expenses[category] += amount  
                    print(f"Additional expense for '{category}' has been added. New total: ₱{expenses[category]:.2f}")
                else:
                    expenses[category] = amount  
                    print(f"Expense for '{category}' has been added with ₱{amount}.")
            else:
                print("Invalid input. Please enter a valid amount.")

        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            analysis = expense_analysis(expenses)
            if analysis["highest"]:
                print("\nExpense Analysis:")
                print(f"Highest Expense: {analysis['highest'][0]} (₱{analysis['highest'][1]:.2f})")
                print(f"Lowest Expense: {analysis['lowest'][0]} (₱{analysis['lowest'][1]:.2f})")
                print(f"Average Expense: ₱{analysis['average']:.2f}")
            else:
                print("No expenses to analyze.")

        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()
