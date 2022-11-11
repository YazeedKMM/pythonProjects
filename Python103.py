# # First project
# class Bike:
#     def __init__(self, description, cost, sale_price, condition):
#         self.description = description
#         self.cost = cost
#         self.sale_price = sale_price
#         self.condition = condition
#         self.sold = False
#
#     def update_sale_price(self, sale_price):
#         if self.sold:
#             print('Action not allowed, Bike has already been sold')
#         else:
#             self.sale_price = sale_price
#
#     def sell(self):
#         self.sold = True
#
#
# bike1 = Bike('Univega Alpina, orange', cost=100, sale_price=500, condition=0.5)
# bike1.update_sale_price(350)
# bike1.sell()
#
# ----------------------------------------------------------------------------------------------------
# Second Project

import datetime


class Bank:
    __balance = 0

    def __init__(self, account_name):
        self.account_name = account_name

    def get_balance(self):
        return self.__balance

    def pay_in(self, deposited_value):
        day = datetime.date.today().strftime("%A %d %B %Y")
        time = datetime.datetime.now().strftime("%I:%M %p")
        if isinstance(deposited_value, int):
            self.__balance += deposited_value
            print("Account", self.account_name,
                  "\nDEPOSITED with amount", deposited_value, "SAR",
                  "\non", day, "at", time,
                  "\nBalance:", self.__balance, "\n")
        else:
            print("You entered a Wrong value")

    def withdraw(self, withdraw_value):
        day = datetime.date.today().strftime("%A %d %B %Y")
        time = datetime.datetime.now().strftime("%I:%M %p")
        if self.__balance > 0:
            if isinstance(withdraw_value, int):
                self.__balance -= withdraw_value
                print("Account", self.account_name,
                      "\nDEBIT with amount", withdraw_value, "SAR",
                      "\non", day, "at", time,
                      "\nBalance:", self.__balance, "\n")
            else:
                print("You entered a Wrong value")
        else:
            print("You don't have enough money")


us = Bank("Yazeed")
print("\n\tYour current balance:", us.get_balance(), "\n")
us.pay_in(350)
us.withdraw(150)
print("\n\tYour current balance:", us.get_balance(), "\n")
