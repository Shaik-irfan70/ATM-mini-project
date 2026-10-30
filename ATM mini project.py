balance = 1000
def check_balance():
    print("your available blance is:",balance)


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: ₹"))

    if amount > 0:
        balance += amount
        print("Amount deposited successfully!")
        print("Updated balance: ", balance)
    else:
        print("Please enter a valid amount.")


def withdraw():
    global balance
    amount =float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("please enter a valid amount.")
    elif amount <= balance:    
        balance -= amount
        print("please collect the cash.")
        print("Remaning Balance: ",balance)
    else:
        print("Insufficient balance!")


def show_menu():
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            print("Thank you for using our ATM!")
            break
        else:
            print("Invalid choice! Please try again.")


v






    
        
        
