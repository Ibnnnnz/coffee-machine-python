"""Import data from another file"""
import random
import math
from collections import Counter
from Data_Coffee import MENU, resources, profit
menu = MENU
resources1 = resources

#TODO 1
"""Input Menu of Coffee"""
def menu_coffee_1(name):
    coffee  = name["espresso"]
    print(f"{coffee}")

def menu_coffee_2(name):
    coffee  = name["latte"]
    print(f"{coffee}")

def menu_coffee_3(name):
    coffee  = name["cappuccino"]
    print(f"{coffee}")

"""Coin User"""
def coin(a,b,c,d,user_coffee):
    global profit
    resources1 = resources
    coffee = menu[user_coffee]['ingredients']
    coffee_cost = menu[user_coffee]["cost"]


    quarters = a
    dimes = b
    nickles = c
    pennies = d

    quarters *= 0.25
    dimes    *= 0.10
    nickles  *= 0.05
    pennies  *= 0.01

    result = round(quarters + dimes + nickles + pennies, 2)


    if result >= coffee_cost:
        result -= float(coffee_cost)
        profit += result
        for items in coffee:
            resources[items] -= coffee[items]
        print(f"Here is ${result} in change.")
        print("Here is your coffee ☕. Enjoy!!!\n")
    else:
        print("Sorry your coin is not enough for bought a coffee, Sorry.\n")

def make_coffee(user_coffee , order_ingredients):
    for item in order_ingredients :
        resources[item] -= order_ingredients[item]

#TODO 2
"""Prompt User by Asking"""
def ask_question():
    machine = False

    while not machine :
        print("Hello! Welcome to The Coffee Machine Generator ☕")
        start = input("\nHere's Our Menu of Coffee\nEspresso $1.5 /Latte $2.5 /Cappuccino $3.0\nWhat would you like? ").lower()

        if start == "turn off":
            print(f"Machine Has Been Turned Off, Under Maintenance")
            break
        elif start == "report":
            print(f"Water: {resources['water']}ml.")
            print(f"Milk: {resources['milk']}ml.")
            print(f"Coffee: {resources['coffee']}ml.")
            print(f"Money: ${profit}.\n")
            ask_question()
        if resources["water"] <= 200:
            print("Sorry, we run out of resources. Come back later.")
            machine = True
            break
        else:
            print("Insert you coin, Please.")
            quarters = float(input("How many quarters you have? "))
            dimes = float(input("How many dimes you have? "))
            nickles = float(input("How many nickles you have? "))
            pennies = float(input("How many pennies you have? "))
            if start == "espresso":
                coin(quarters,dimes,nickles,pennies,"espresso")
            elif start == "latte":
                coin(quarters,dimes,nickles,pennies,"latte")
            elif start == "cappuccino":
                coin(quarters,dimes,nickles,pennies,"cappuccino")


ask_question()
