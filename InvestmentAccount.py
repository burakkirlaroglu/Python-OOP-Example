from OOP.Bank_OOP.BankAccount import BankAccount
import random
class Investment(BankAccount):

    def __init__(self):
        super().__init__("user")

    def account_rep(self, process):
        if process == 1:
            return BankAccount.__str__(self)

    #overriding
    def withdraw(self, amount):
        phone_code = random.randint(1,1000)
        print("Phone Verify code: ", phone_code)
        if amount > 650:
            onay = int(input("Please enter verify code: "))
            if onay == phone_code:
                self._balance -= amount
                return self._balance
