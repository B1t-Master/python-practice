
class BalanceException(Exception):
    pass


# class AccountException(Exception):
#     pass


class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(
            f"\nAccount '{self.name}' created\nBalance = KES{self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' has \nBalance = KES{self.balance:.2f}")

    def deposit(self, ammount):
        self.balance += ammount
        self.get_balance()

    def valid_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry account '{self.name}' has insufficient funds with a balance of KES{self.balance}"
            )

    def withdraw(self, amount):
        try:
            self.valid_transaction(amount)
            self.balance -= amount
            print("\nWithdrawal complete")
            self.get_balance()
        except BalanceException as error:
            print(f"Withdraw interrupted: {error}")

    # def account_exists(account):
    #     if account:
    #         return
    #     else:
    #         raise AccountException(
    #             "Sorry the acoount '{account}' does not exists")

    def transfer_money(self, amount, account):
        try:
            print("---------------")
            print("\nBeginning Money Transfer...")
            # self.account_exists(account)
            self.valid_transaction(amount)
            account.deposit(amount)
            self.withdraw(amount)
            print("Transfer complete")
            print("---------------")
        except Exception:
            print("Sorry the acoount you are transferring to does not exists")
        except BalanceException as error:
            print(f"Transfer interrupted: {error}")

        # except AccountException as error:
        #     print(f"Transfer interrupted: {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount*1.05
        print("\nDeposit Complete")
        self.get_balance()


class MoneyMarketFund(InterestRewardsAccount):
    def __init__(self, initial_amount, account_name):
        super().__init__(initial_amount, account_name)
        self.fee = 30

    def withdraw(self, amount):
        return super().withdraw(amount=amount+self.fee)
