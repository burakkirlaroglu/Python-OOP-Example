from OOP.Bank_OOP.SavingsAccount import SavingAccount
from OOP.Bank_OOP.InvestmentAccount import Investment
from OOP.Bank_OOP.CheckingAccount import CheckingAccount


sa = SavingAccount()

ia = Investment()

ca = CheckingAccount()

print("""

Welcome To Bank Account App
***********************************
1. Current information

2. Deposit

3. Withdraw

4. According to interest calculate your earn

5. Current Interest

6. Information about all process
***********************************
""")


while True:
    process = input("Choose action: ")

    if process == "q":
        print("Application is closing...")
        break
    elif process == "1":
        print(ca)
    elif process == "2":
        amount = int(input("Amount: "))
        print(ca.deposit(amount))
    elif process == "3":
        amount = int(input("Amount: "))
        print(ca.withdraw(amount))
    elif process == "4":
        month = int(input("How many month in include calculate ?"))
        print(sa.interest_Rate(month))
    elif process == "5":
        print(sa)
    elif process == "6":
        action = int(input("It depend on deposit - push : 1\nIt depends on withdraw - push : 2"))
        print(ca.last_check_num(action))
    else:
        print("Invalid Process !!!")


















