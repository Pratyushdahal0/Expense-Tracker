

#making function 
expenses = []
def add():
    category = input("Enter a category : ")
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
    



    
