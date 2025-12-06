from banking_system_with_OOPs import *

nikhil = BankAccount(1000,"Nikhil")
ajay = BankAccount(1500,"Ajay")

nikhil.getBalance()

ajay.deposit(5000)
nikhil.deposit(6500)

ajay.withdraw(100)

nikhil.transfer(2000,ajay)
ajay.transfer(4000,nikhil)

aditi = InterestRewardAcct(5000,"Aditi")

aditi.getBalance()

aditi.transfer(500,ajay)