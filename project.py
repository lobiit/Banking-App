class Bank:
    def __init__(self, initial_amount=0 - 00):
        self.balance = initial_amount

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance - amount

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        self.balance = self.balance + amount


account = Bank(50.50)
account.deposit(10)
print(account.balance)
account.withdrawal(14.75)
print(account.balance)
