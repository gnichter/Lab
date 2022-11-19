import account

account = Account()
print(account.deposit(100))
print(account._account_balance)
print(account.deposit(0))
print(account._account_balance)
print(account.deposit(-100))
print(account._account_balance)
