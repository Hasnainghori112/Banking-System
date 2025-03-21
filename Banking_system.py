class BankAccount():
  def __init__(self, account_number, balance, owner):
    self.account_number = account_number
    self.balance = balance
    self.owner = owner
  def deposit(self, amount):
    self.balance += amount
    print(f"${amount} has been depoisted to your account {self.account_number}\n Now the balance is {self.balance}")
  def withdraw(self,withdraw):
    if withdraw > self.balance:
      print("Insufficient funds")
    else:
      self.balance -= withdraw
      print(f"${withdraw} has been withdrawn from your account {self.account_number}\n Now the balance is {self.balance}")
  def check_balance(self):
    print(f"Your current balance is {self.balance}")

Hasnain = BankAccount("123456789", 1000, "Hasnain")
Hasnain.deposit(500)
Hasnain.withdraw(100)
Hasnain.check_balance()

