def expense():
    def add_expense(expenses):
        category = input("Enter the expense category: ")
        amount = float(input("Enter the amount spent: "))
        expenses.append((category, amount))

    def main():
        print("Welcome to the Expense Tracker!")
        expenses = []
        total_income = float(input("Enter your total income: "))

        while True:
            add_expense(expenses)
            more = input("Do you want to add another expense? (yes/no): ").lower()
            if more != 'yes':
                break

        total_expenses = sum(amount for _, amount in expenses)
        balance = total_income - total_expenses

        print("\nSummary:")
        for category, amount in expenses:
            print(f"{category}: ₹{amount:.2f}")
        print(f"Total Expenses: ₹{total_expenses:.2f}")
        print(f"Remaining Balance: ₹{balance:.2f}")
        if balance < 0:
            print("You are in debt!")

    main()

if __name__ == "__main__":
    expense()
