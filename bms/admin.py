class Admin:
    def __init__(self) -> None:
        pass
    
    def create_account(self, bank, name, email, address, account_type):
        return bank.create_account(name, email, address, account_type)
    
    def delete_account(self, bank, account_num):
        bank.delete_account(account_num)
        
    def get_all_accounts(self, bank):
        bank.get_all_accounts(bank)    
        
    def get_total_amount(self, bank):
        bank.get_available_balance(bank) 
        
    def get_total_loan_amount(self, bank):
        bank.get_total_loan_amount(bank)
        