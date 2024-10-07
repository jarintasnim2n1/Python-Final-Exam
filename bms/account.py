class Account:
    def __init__(self, name, email, address, account_type, account_num):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_num = account_num
        self.balance = 0
        self.transactions = []
        self.total_loan = 0
        self.loan_taken = 0
            
    def deposit(self, amount):  
        self.balance += amount 
        self.transactions.append(f"Deposited : {amount}") 
        print(f" The amount {amount} deposited successfully!")
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"withdraw : {amount}")
            print(f" The amount {amount} is Withdrawn successfully! ")
        else:
            print("Withdrawal amount exceeded")    
             
    def checl_balance(self):
        print(f"The current balance is {self.balance}")
        
    def transaction(self): 
        for i in self.transactions:
            print(f"The transactions are {i}")           
            
    def take_loan(self, amount):
        if self.loan_taken < 2:
            self.total_loan += amount 
            self.balance += amount
            self.loan_taken += 1
            self.transactions.append(f"Loan Taken : {amount}")
            print(f"The loan amount {amount} is taken Successfully!")
        else:
            print("Account does not exist")    
    
    def tranfer(self, amount, recipient, bank):
        if amount <= self.balance: 
            self.balance -= amount
            recipient.balance += amount
            self.transactions.append(f"Tranferred : {amount}")
            recipient.transactions.append(f" tranfer aomunt {amount} Added ")
            print("Amount Tranfer Successfully!!")
        elif recipient not in bank.users:
            print("Recipient account does not exit ")
            return
        else:
            print("Insufficient Balance ")
            return
        
    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Address: {self.address}, Account Type: {self.account_type}, Account Number: {self.account_num}, Balance: {self.balance}"        
            
                   
            
         
                  
        