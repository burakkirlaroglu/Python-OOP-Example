from OOP.Bank_OOP.BankAccount import BankAccount
from OOP.Bank_OOP.Constats import INTEREST_RATE
class SavingAccount(BankAccount):

    def __init__(self):
        super().__init__("user")

    def __str__(self):
        return f"Current Interest Rate:  {INTEREST_RATE}"


    def interest_Rate(self, month):
        print("Current Balance: {} $".format(self._balance))
        interest = self._balance * INTEREST_RATE
        interest *= month
        self._balance += interest
        if interest:
            return f"{month} months later price: {interest} $. New Balance: {self._balance}"