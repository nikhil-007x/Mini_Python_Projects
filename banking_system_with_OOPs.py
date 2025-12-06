class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,intitialAmount,acctName):
        self.balance = intitialAmount
        self.name = acctName
        print(f"\n Account '{self.name}' Created \n {self.balance:.2f}Rs ")

    def getBalance(self):
        print(f"\n Account - '{self.name}'\n Balance = {self.balance:.2f}Rs ")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\n Deposit Complete")
        self.getBalance()

    def viableTransaction(self,amount):
        if(self.balance >= amount):
            return
        else:
            raise BalanceException(
                f"Sorry '{self.name}' Has only '{self.balance}'Rs "
            )

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)    
            self.balance = self.balance - amount
            print(f"Withrawal Complete")
            self.getBalance()
        except BalanceException as error:
            print(f"Withdrawal Interrupted {error}")

    def transfer(self,amount,account):
        try:
            print("\n *************")
            print("\n Begining Transer........")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n Transfer Complete !!!")
        except BalanceException as error:
            print(f"\nTransfer Interrupted. ##{error}#")

class InterestRewardAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + amount*1.08
        print("\n Deposit Complete.")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initial_amount, acct_name): 
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def withdraw(self, amount): 
        try: 
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee) 
            print("\nWithdraw completed.")
            self.get_balance() 
        except BalanceException as error: 
            print(f'\nWithdraw interrupted: {error}')