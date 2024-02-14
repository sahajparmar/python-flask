

class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepted')

    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Object
print(acct1)




# 3.Account owner attribute
acct1.owner




# 4.Account balance attribute
acct1.balance




# 5.Deposits and withdrawals
acct1.deposit(50)




acct1.withdraw(75)




# 6.Withdrawal with current available balance
acct1.withdraw(500)
