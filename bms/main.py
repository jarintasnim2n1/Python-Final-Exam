from account import Account
from admin import Admin
from bank import Bank

bank = Bank("Islami Bank")
admin = Admin()
curr_user = None

while True:
    print("----ASSALAMUALIKUM----")
    print(f"\n\tWelcome to {bank.name} Bank!!")
    print("1. Admin")
    print("2. User")
    print("3. Exit") 
    
    choice = int(input("Enter your preferable option :"))
    
    if choice == 1:
        print("1. Create Account")
        print("2. Delete Account") 
        print("3. View all Account")
        print("4. Check Amount")
        print("5. Check total Loan Account")
        print("6. ON Loan feature")
        print("7. OFF Loan feature")
          
        c = int(input("Enter An Opion : "))
        if c == 1:
            name = input("Namne :")
            email = input("Emaail :")
            address = input("Address :")
            type = input("Account Type :")
            curr_user = admin.create_account(bank, name, email, address, type)
        elif c == 2:
            account = int(input("Account Number :"))
            admin.delete_account(bank, account)    
        elif c == 3:
            admin.get_all_accounts(bank)
        elif c == 4:
            admin.get_total_amount(bank)
        elif c == 5:
            admin.get_total_loan_amount(bank)
        elif c == 6:
            bank.on_loan() 
        elif c == 7:
            bank.off_loan()       
        else:
            print("Invalid Option")
    
    elif choice == 2:                    
        print("1.Create Account")
        print("2.Deposite Amount")
        print("3.Withdraw Amount")
        print("4.Check available balance")
        print("5.Check Transfer History")
        print("6.Take Loan")
        print("7.Transfer Money")    
        
        c = int(input("Enter An Option"))        
        
        if c == 1:
            name = input("Namne :")
            email = input("Emaail :")
            address = input("Address :")
            type = input("Account Type :")
            curr_user = bank.create_account( name, email, address, type)
        elif c == 2:
            deposit_amount = int(input("Amount :"))
            curr_user.deposit(deposit_amount)  
        elif c == 3:
            withraw_amount = int(input("Amount :"))
            curr_user.withdraw(withraw_amount) 
        elif c == 4:
            curr_user.checl_balance()
        elif c == 5:
            curr_user.transaction()
        elif c == 6:
            amount = int(input("Amount :"))
            curr_user.loan_taken(amount) 
        elif c == 7:
            print("Give the receiver Information ")
            name = input("Namne :")
            email = input("Emaail :")
            address = input("Address :")
            account_type = input("Account Type :") 
            account_num = int(input("Account number :"))  
            receiver = Account(name, email, address, account_type, account_num)     
            amount = int(input("Amount :"))
            curr_user.tranfer(amount, receiver, bank)
        else:
            print("Invalid Option")