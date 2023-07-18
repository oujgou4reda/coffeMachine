MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money: float = 0
choice = ["espresso", "latte", "cappuccino"]

# TODO:1. CALCULATE PRICE:


# TODO:2. print report
def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print("the current resource values. e.g.")
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"coffee: {coffee}g")
    print(f"Money: ${money}")


def check_res(bev):
    if resources["water"] < MENU[bev]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    if bev != "espresso":
        if resources["milk"] < MENU[bev]["ingredients"]["milk"]:
            return "Sorry there is not enough milk."
    if resources["coffee"] < MENU[bev]["ingredients"]["coffee"]:
        return "Sorry there is not enough coffe."
    return 0


def pay(bev):
    print("Please insert coins ")
    quarters = int(input("how many quarters"))
    dimes = int(input("how many dimes"))
    nickles = int(input("how many nickels"))
    pennies = int(input("how many pennies"))
    somme = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if somme < MENU[bev]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    resources["water"] -= MENU[bev]["ingredients"]["water"]
    resources["coffee"] -= MENU[bev]["ingredients"]["coffee"]
    if bev != "espresso":
        resources["milk"] -= MENU[bev]["ingredients"]["milk"]
    global money
    money += MENU[bev]["cost"]
    change = somme - MENU[bev]["cost"]
    if change != 0:
        print(f"Here is ${change} dollars in change.")


while True:
    command = input("What would you like? (espresso/latte/cappuccino):")
    if command == "off":
        break
    if command == "report":
        report()
    if command in choice:
        if check_res(command) != 0:
            print(check_res(command))
        pay(command)
