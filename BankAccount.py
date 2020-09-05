from OOP.Bank_OOP.Constats import INTEREST_RATE

class BankAccount():

    def __init__(self, account_name, balance=1000, deposit_count=0, witdraw_count=0):
        self._account_name = account_name
        self._balance = balance
        self.deposit_count = deposit_count
        self.witdraw_count = witdraw_count

    def deposit(self, amount):
        self._balance += amount
        self.deposit_count += 1
        return f"Left balance: {self._balance} Increase amount: {amount}"

    def withdraw(self, amount):
        self._balance -= amount
        self.witdraw_count += 1
        return f"Left balance: {self._balance} Withdraw amount: {amount}"

    def __str__(self):
        return f"Account: {self._account_name} Balance: {self._balance} Current Interest Rate: {INTEREST_RATE}"


