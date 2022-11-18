class Account:

    def __init__(self, name):
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount):
        amount = float(input("Enter amount to be deposited: "))
        if amount > 0:
            self.__account_balance += amount
        else:
            pass

    def withdraw(self, amount):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            pass

    def get_balance(self):
        print(self.__account_balance)

    def get_name(self):
        print(self.__account_name)
