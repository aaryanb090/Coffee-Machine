from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine = CoffeeMaker()
money = MoneyMachine()
file = Menu()
menu = file.get_items()
is_on = True

while is_on:
    choice = input(f"What would you like to have : {menu}").lower()
    if choice == "report":
        print(coffee_machine.report())
        print(money.report())
    elif choice == "off":
        is_on = False
    else:
        drink = file.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)



