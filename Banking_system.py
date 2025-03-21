class atm():
  def __init__(self, balance=1111):
    self.balance = balance
  def deposit(self,amount):
    self.balance += amount
    return f"Deposit: ${amount}\n new Balance:{balance}"
  def withdraw(self , amount):
    if amount > self.balance:
      return f"Insufficient funds! Your balance is ${self.balance}."
      self.balance -= amount
      return f"Withdraw: ${amount}\nNew balance: ${self.balance}"

  def check_balance(self):
    return f"Your current balance: ${self.balance}"

# Testing the ATM
atm = atm()

print("Welcome to the ATM!")
print(atm.check_balance())  # Initial balance
print(atm.deposit(500))  # Depositing money
print(atm.withdraw(700))  # Withdrawing money
print(atm.withdraw(900))  # Trying to withdraw more than balance

