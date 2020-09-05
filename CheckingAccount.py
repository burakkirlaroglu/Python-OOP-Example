from OOP.Bank_OOP.BankAccount import BankAccount

class CheckingAccount(BankAccount):

    NUMBER_OF_OPERATION = 0

    def __init__(self):
        super().__init__("user")

    def last_check_num(self, process):
        self.NUMBER_OF_OPERATION = self.deposit_count + self.witdraw_count
        if process == 1:
            return f"{self.deposit_count} deposit process completed.\nProcess made by {self._account_name}'s account.\nSum Process: {self.NUMBER_OF_OPERATION}" \
                   f"\nDeposit process count: {self.deposit_count}\nWithdraw process count: {self.witdraw_count}"
        elif process == 2:
            return f"{self.witdraw_count} withdraw process completed.\nProcess made by {self._account_name}'s account.\nSum Process: {self.NUMBER_OF_OPERATION}" \
                   f"\nWithdraw process count: {self.witdraw_count}\nDeposit process count: {self.deposit_count}"