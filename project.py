class Bank:
    def __init__(self, initial_amount=0 - 00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transaction.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrew Ksh.{amount}")

        self.balance = self.balance - amount

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Deposited Ksh.{amount}")
        self.balance = self.balance + amount


account = Bank(50.50)
account.deposit(10)
print(account.balance)
account.withdrawal(14.75)
print(account.balance)
