class BankaAccount:
   def __init__(self,balance):
      self.__balance = balance
   def deposit(self):
      amount =float(input("enter the amount to be deposited:"))
      self.__balance += amount
      print("Amount deposited:", amount)
   def withdraw(self):
      amount =float(input("enter the amount to be withdrawn:"))
      if self.__balance >= amount:
         self.__balance -= amount
         print("Amount withdrawn:", amount)
      else:
         print("Insufficient balance")
   def get_balance(self):
      print("Current balance:", self.__balance)
account = BankaAccount(1000)
account.deposit()
account.withdraw()
account.get_balance()
