from data import MENU, resources, coins
import math
from art import logo

def machine():
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino)")

    if choice == "espresso":
        water = (MENU["espresso"]["ingredients"]["water"])
        coffee = (MENU["espresso"]["ingredients"]["coffee"])
        milk = 0
        cost = (MENU["espresso"]["cost"])
    elif choice == "latte":
        water = (MENU["latte"]["ingredients"]["water"])
        coffee = (MENU["latte"]["ingredients"]["coffee"])
        milk = (MENU["latte"]["ingredients"]["milk"])
        cost = (MENU["latte"]["cost"])
    elif choice == "cappuccino":
        water = (MENU["latte"]["ingredients"]["water"])
        coffee = (MENU["latte"]["ingredients"]["coffee"])
        milk = (MENU["latte"]["ingredients"]["milk"])
        cost = (MENU["cappuccino"]["cost"])

    if resources["water"] >= water:
        if resources["coffee"] >= coffee:
            if resources["milk"] >= milk:
                print(f"{choice} cost is {cost}. Please insert the coins.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough coffee.")
    else:
        print("Sorry there is not enough water.")

    print(f"The total payable coins are ${cost}.")

    coin_quarters = int(input("How many quarter coins do you want to insert?: $"))
    coin_dimes = int(input("How many dime coins do you want to insert?: $"))
    coin_nickles = int(input("How many nickle coins do you want to insert?: $"))
    coin_pennies = int(input("How many penny coins do you want to insert?: $"))

    a = coin_quarters*coins["quarters"]+coin_dimes*coins["dimes"]
    b = coin_nickles*coins["nickles"]+coin_pennies*coins["pennies"]
    total_amount = a+b

    if cost == total_amount:
        print(f"Your {choice} is ready. Have a good day :)")
    elif cost < total_amount:
        print(f'Your {choice} is ready. Take the remaining change ${(total_amount-cost)}')
    elif cost > total_amount:
        print(f"Insufficient money, try again. {total_amount} is refunded.")

    updated_resources = {
        "water": resources["water"]-water,
        "coffee": resources["coffee"]-coffee,
        "milk": resources["milk"]-milk,
        "cost": cost
    }

    print(f"The Resources before making {choice} are {resources}")
    print(f"The Resources after making {choice} are {updated_resources}")

    print("Have a great day!")

machine()