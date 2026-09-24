from bank_account import *

Isaac = BankAccount(8000, "Isaac")
John = BankAccount(4999, "John")

Isaac.deposit(400)

John.withdraw(5000)

Isaac.transfer_money(11300, John)

Penina = InterestRewardsAccount(9000, "Penina")

Penina.deposit(900)

Penina.transfer_money(9900, Isaac)

Caroline = MoneyMarketFund(20000, "Caroline")

Caroline.withdraw(19999)

# Julia = 1
Isaac.transfer_money(100, "Julia")
