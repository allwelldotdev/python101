import random
from datetime import datetime, timezone


class BankAccount:
    def __init__(self, *,
                 first_name:str,
                 last_name:str,
                 account_number:int,
                 balance:float= 0,
        is_overdraft_allowed:bool= False,
                overdraft_amount:float= 0):

        # validate: first_name
        if not self.is_pure_str(first_name):
            raise ValueError('first_name must be a string')
        self._first_name = first_name.upper()

        # validate: last_name
        if not self.is_pure_str(last_name):
            raise ValueError('last_name must be a string')
        self._last_name = last_name.upper()

        # validate: account_number
        if isinstance(account_number, float) and not(isinstance(account_number, int)):
            raise ValueError('account_number must be an integer')
        elif not(self.count_digits(account_number, 10)):
            raise ValueError('account_number must be 10 digits')
        else:
            self._account_number = account_number

        # validate: balance
        if not(isinstance(balance, (int, float))):
            raise ValueError('balance must be integer or float')
        self._balance = float(balance)

        # validate: is_overdraft_allowed
        if not(isinstance(is_overdraft_allowed, bool)):
            raise ValueError('is_overdraft_allowed must be boolean')
        self.is_overdraft_allowed = is_overdraft_allowed # defaults to False

        # validate: overdraft_amount
        if not(isinstance(balance, (int, float))):
            raise ValueError('overdraft_amount must be integer or float')
        if not self.is_overdraft_allowed and overdraft_amount > 0 or overdraft_amount < 0:
            raise ValueError('is_overdraft_allowed is False, therefore setting overdraft amount is not allowed')
        self._overdraft, self._overdraft_amount = [round(overdraft_amount, 2)] * 2

        # initialize ledger
        self._ledger = []

    # validation func
    def is_pure_str(self, value):
        if not isinstance(value, str):
            return False
        try:
            float(value)
            return False
        except ValueError:
            return True
    
    # check if digits is count value. Ex: if count value is 10 and digits is 9, return False
    def count_digits(self, digits, count):
        digits = len([digit for digit in str(digits)])
        return digits == count
    
    # setting read-only properties: first_name, last_name, account_number, balance
    @property
    def first_name(self):
        return self._first_name
    
    @property
    def last_name(self):
        return self._last_name

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    @property
    def ledger(self):
        return self._ledger

    # configure overdraft getter
    @property
    def overdraft(self):
        return self._overdraft

    # contifure overdraft_amount getter
    @property
    def overdraft_amount(self):
        return self._overdraft_amount

    # configure overdraft_amount setter
    @overdraft_amount.setter
    def overdraft_amount(self, value):
        if not(isinstance(value, int) or isinstance(value, float)):
            raise ValueError('overdraft_amount must be integer or float')
        if not self.is_overdraft_allowed:
            raise ValueError('is_overdraft_allowed is False, therefore setting overdraft amount is not allowed')
        if self.overdraft != self.overdraft_amount:
            raise ValueError('BankAccount not qualified for overdraft amount increase')
        self._overdraft, self._overdraft_amount = [round(value, 2)] * 2

    # define ledger_wrap decorator function to add metaprogramming to deposit and withdrawal func
    # this decorator adds every deposit/withdraw transaction to the ledger
    def ledger_wrap(fn):
        def inner(self, amount):
            _dict = {'datetime': datetime.now(timezone.utc).isoformat(), 'transaction_reference': random.randrange(10**13, 10**14)}
            result = fn(self, amount)
            result_copy = result.copy()
            result_copy.update(_dict)
            self.ledger.append(result_copy)
            return result
        return inner
    
    # decorate deposit func with ledger_wrap decorator
    @ledger_wrap
    # deposit func
    def deposit(self, amount):
        # validate amount to be int, float, or greater than zero
        if not(isinstance(amount, int) or isinstance(amount, float)):
            raise ValueError('amount must be integer or float')
        if not(amount > 0):
            raise ValueError('amount must be greater than zero')

        # grab initial balance before transactions
        initial_balance, initial_overdraft = self.balance, self.overdraft

        # deposit + overdraft functionality
        if self.is_overdraft_allowed and self.overdraft < self.overdraft_amount:
            if self.overdraft + amount > self.overdraft_amount:
                remainder = amount - (self.overdraft_amount - self.overdraft)
                self._overdraft = self.overdraft_amount
                self._balance = round(self.balance + remainder, 2)
            else:
                self._overdraft = self.overdraft + amount
            return {
                'credit': amount,
                'initial_balance': initial_balance,
                'current_balance': self.balance,
                'initial_overdraft': initial_overdraft,
                'current_overdraft': self.overdraft
            }
        else:
            self._balance = round(self.balance + amount, 2)
            return {'credit': amount, 'initial_balance': initial_balance, 'current_balance': self.balance}

    # decorate withdraw func with ledger_wrap decorator
    @ledger_wrap
    # withdraw func
    def withdraw(self, amount):
        # validate amount to be int, float, or greater than zero 
        if not(isinstance(amount, int) or isinstance(amount, float)):
            raise ValueError('amount must be integer or float')
        if not(amount > 0):
            raise ValueError('amount must be greater than zero')

        # validate withdrawal, raise custom exception if trying to withdraw beyond overdraft limit
        if amount > self.balance and amount > self.balance + self.overdraft:
            raise self.OverdraftNotAllowed(self.balance + self.overdraft, amount)

        # grab initial balance before transactions
        initial_balance, initial_overdraft = self.balance, self.overdraft

        # withdraw + overdraft functionality
        if amount > self.balance:
            remainder = -(self.balance - amount)
            self._balance = float(0)
            self._overdraft = round(self.overdraft - remainder, 2)
            return {
                'debit': amount,
                'initial_balance': initial_balance,
                'current_balance': self.balance,
                'initial_overdraft': initial_overdraft,
                'current_overdraft': self.overdraft
            }
        else:
            self._balance = round(self.balance - amount, 2)
            return {'debit': amount, 'initial_balance': initial_balance, 'current_balance': self.balance}

    # custom exception 'OverdraftNotAllowed', if withdraw amount exceeds balance
    class OverdraftNotAllowed(Exception):
        def __init__(self, balance, amount):
            self.message = f'Cannot withdraw {amount}. Current Balance: {balance}'
            super().__init__(self.message)

    # class string formatting
    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.account_number}): {self.balance}'

    # class repr formatting
    def __repr__(self):
        return f'{self.__class__.__name__}(first_name={self.first_name}, last_name={self.last_name}, account_number={self.account_number}, balance={self.balance}, is_overdraft_allowed={self.is_overdraft_allowed}, overdraft={self.overdraft}, overdraft_amount={self.overdraft_amount}, ledger_length={len(self.ledger)})'

    # implement equality
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('not comparable')
        return self.account_number == other.account_number
        # alternatively...
        #return True if isinstance(other, self.__class__) and self.account_number == other.account_number else False

    # implement greater than comparison
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise ValueError('not comparable')
        return self.balance > other.balance


allwell = BankAccount(
    first_name='Allwell',
    last_name='Agwu-Okoro',
    account_number=1234567890,
    balance=100,
    # is_overdraft_allowed=True,
    # overdraft_amount=100
)

# enable overdraft
allwell.is_overdraft_allowed=True
allwell.overdraft_amount=100

# perform transactions
allwell.deposit(15)
allwell.withdraw(30)
allwell.withdraw(100)
allwell.withdraw(80)
allwell.deposit(15)

# check balance and overdraft balance
print(allwell.balance, allwell.overdraft)

# check account ledger, and ledger length in repr
print(allwell.ledger)
print(repr(allwell))


