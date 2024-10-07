import random
from account import Account
from admin import Admin


class Bank:
    def __init__(self, name) :
        self.name = name
        self.users = [] 
        self.admin = Admin()
        self.loan = True
        
    def create_account(self, name, email, address, account_type):
        account_num = random.randint(1000, 50000)
        account = Account(name, email, address, account_type, account_num)
        self.users.append(account)
        print(f"Account number {account_num} created Successfully!!")
        return account
    
    def delete_account(self, account_num):
        for i in self.users:
            if i.account_num == account_num:
                self.users.remove(i)
                print(f"The account {account_num} is deleted")  
                return
        print(f"The account {account_num} is not found")    
    
    def get_all_accounts(self, bank):
        for i in self.users:
            print(i)
            
    def get_available_balance(self, bank):
        total_amount = sum(i.balance for i in self.users) 
        print(f"The Total amount is {total_amount}")  
        
    def get_total_loan_amount(self, bank):
        total_amount = sum(i.total_loan for i in self.users) 
        print(f"The Total loan amount is {total_amount}")               
    
    def on_loan(self):
        self.loan = True
        print("Loan is Active!!")
        
    def off_loan(self):
        self.loan = False
        print("Loan is diactive!!")                  