
#making function 
expenses = []
def add():
    category = input("Enter a category : ").strip()
    try:
        amount = int(input("Enter a amount : "))
    except ValueError:
        print("Amount only contains integer")
        return
    

    #checking if user give us any wrong words or not 
    if not category.isalpha():
       print("Category should only contain alphabets")
       return
    else:
        expense = {
            "category": category,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully")


def showallExpenses():
    for expense in expenses:
        print(f" Category : {expense['category']}, Amount : {expense['amount']}")


def totalexpenses():
    totalAmount = 0 
    for amt in expenses:
        amounts = amt['amount']
        totalAmount += amounts
        
    print(f"Total amount : {totalAmount}")


def expensesCategory():
    totals = {}
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    for category, total in totals.items():
        print(f"{category} : {total}")




while True:
    print("Welcome to expense tracking")
    print(f"1. Add Expenses")
    print(f"2. Show All Expenses")
    print(f"3. Total Expenses")
    print(f"4. Expenses Category")
    print(f"5. Exit")
    userInput = int(input("Enter a Number : "))
    if userInput == 1:
        add()
    elif userInput == 2:
        showallExpenses()
    elif userInput == 3:
        totalexpenses()
    elif userInput == 4:
        expensesCategory()
    elif userInput == 5:
        break
    else: 
        print("Only user above options")
    


    

    
