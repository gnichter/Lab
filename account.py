class Account:

    def init(self, name):
        self._account_name: str = f'{name}'
        self._account_balance: int = 0
    '''This function initializes the account'''

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance += amount
            return True
        else:
            return False

    '''This function sees if your deposit is a valid positive number and
    if it is deposits it into the account'''

    def withdraw(self, amount: int) -> bool:
        if amount > 0:
            self._account_balance -= amount
            return True
        else:
            return False
    '''This function sees if your withdrawal is a valid positive number
        and if it is, that amount is subtracted to the account'''

    def get_balance(self) -> str:
        return f'{self._account_balance}'
    '''This function returns the amount left in the account'''

    def get_name(self) -> str:
        return f'{self._account_name}'
    '''This function returns the name from the account'''
