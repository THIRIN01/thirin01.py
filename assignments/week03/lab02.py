# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
       
        choice = input("Choose option: ")

        if choice == "1":
            print("Your balance is:", balance)

        elif choice == "2":
            try:
                withdraw = float(input("Withdraw amount: "))
                if withdraw <= 0:
                    print("Withdrawal amount must be greater than 0.")
                elif withdraw > balance:
                    print("Insufficient funds.")
                else:
                    balance -= withdraw
                    print("Withdrawal successful. Your balance is now:", balance)
            except ValueError:
                print("Invalid amount.")

        elif choice == "3":
            try:
                deposit = float(input("Deposit amount: "))
                if deposit <= 0:
                    print("Cannot deposit less than or equal to 0.")
                else:
                    balance += deposit
                    print("Deposit successful. Your balance is now:", balance)
            except ValueError:
                print("Invalid amount.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid PIN")
