import os

class Expense :
    def __init__(self,name,category,amount):
        self.name = name
        self.category = category
        self.amount = amount
    

def get_user_expense():
        print("Enter expense details :")
        expense_name = input("Enter the name of your expense :")
        expense_category = input("Enter the category of your expense (eg. Food, Entertainment , Work etc.):")
        expense_amount = float(input("Enter expense amount in rupees : "))
        return Expense(name = expense_name, category = expense_category, amount = expense_amount)
    

def save_expense_to_file(expense):
        with open("expenses.txt","a") as file :
            file.write(f"{expense.name}, {expense.category}, {expense.amount}\n")
        print("Expense saved successfully!")

    
def summarize_expenses():
        total_expenses = 0
        try:
            with open("expenses.txt","r") as file :
                print("\n Expenses Summary :")
                print("{:<20} {:<15} {:<10}".format("Name","Category","Amount"))
                print("-"*45)
                for line in file :
                    name , category ,amount = line.strip().split(",")
                    print("{:<20} {:<15} Rs{:<10.2f}".format(name, category, float(amount)))
                    total_expenses += float(amount)
        except FileNotFoundError:
            print("No expenses found")
        
        print("\nTotal Expenses: Rs{:.2f}".format(total_expenses))

    
def main():
        while True:
            print("\n Expense Tracker Menu")
            print("1. Add Expense")
            print("2. View Summary")
            print("3. Exit")

            choice = input("Enter your choice (1,2 or 3):")

            if choice == "1":
                expense = get_user_expense()
                save_expense_to_file(expense)
            elif choice == "2":
                summarize_expenses()
            elif choice == "3":
                print("***Exiting expense tracker***")
                break
            else :
                print("Invalid choice. Please enter 1,2 or 3")

if __name__ == "__main__":
        if not os.path.exists("expenses.txt"):
            open("expenses.txt","w").close()
        main()


            
