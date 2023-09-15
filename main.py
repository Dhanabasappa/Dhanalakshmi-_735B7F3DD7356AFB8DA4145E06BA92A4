class BankAccount:
  def __init__(self, account_number, account_holder_name, account_balance):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = account_balance
  def deposit(self, amount):
    if amount > 0 :
     self.__account_balance += amount
     print("Deposited ₹{}.New balance:₹{} format(amount,self.__init__balance)")
    else:
      print("Invalid withdrawal amount or insufficient balance ")
  def withdraw(self, amount):
    if amount>0 and  amount <=self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ₹{} .New balance :₹{}format(amount,self__initt__balance)")
    else:
      print("Insufficient funds")
  def display_balance(self):
    print("Account balance for{} (Account#{}):₹()",format(self.__account_holder_name,
self.__account_number))
# Create an instance of the BankAccount class
account = BankAccount("1234567890", "John Smith", 1000)
# Test the deposit and withdrawal functionality
account.display_balance()
account.deposit(500.00)
account.withdraw(300.00)
account.withdraw(200.00)
account.display_balance()