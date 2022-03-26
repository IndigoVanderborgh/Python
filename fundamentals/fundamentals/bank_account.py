class BankAccount:
    account=[]
    def __init__(self, int_rate, balance): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.account.append(self)
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if(self.balance-amount)>=0:
            self.balance-=amount
        else:
            print("No funds available")
        return self
    def display_account_info(self):
        print(f"Current Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance+=(self.balance*self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.account:
            account.display_account_info()

Indi = BankAccount(.30,10)
Jerry = BankAccount(.01,50)

Indi.deposit(400).deposit(100).deposit(100).withdraw(45).yield_interest()
Jerry.deposit(1040).deposit(10).deposit(41).withdraw(44).yield_interest()

BankAccount.print_all_accounts()