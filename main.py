from data import resources, MENU

QUARTER = 0.25
DIME = 0.1
NICKEL = 0.05
PENNIE = 0.01
money = 0


def ask_for_drink():
    answer = input("\nWhat would you like? (espresso/latte/cappuccino): ")
    return answer


def check_resources(drink):
    for resource in resources:
        if resources[resource] < MENU[drink]["ingredients"][resource]:
            return resource
    return True


def ask_for_coins():
    print("Enter the coins:-")
    quarters = int(input("Enter the number of quarters: "))
    dimes = int(input("Enter the number of dimes: "))
    nickels = int(input("Enter the number of nickels: "))
    pennies = int(input("Enter the number of pennies: "))
    return quarters*QUARTER + dimes*DIME + nickels*NICKEL + pennies*PENNIE


def is_transaction_successful(given_money, drink):
    required_money = MENU[drink]["cost"]
    if given_money >= required_money:
        return True
    return False


def give_back_change(given_money, drink):
    required_money = MENU[drink]["cost"]
    if given_money > required_money:
        change = round(given_money-required_money, 2)
        print(f"Here's your change: ${change}")


def make_coffee(given_money, drink):
    global money
    money += MENU[drink]["cost"]
    for resource in resources:
        resources[resource] -= MENU[drink]["ingredients"][resource]
    give_back_change(given_money, drink)
    print(f"Here is your {drink} ☕. Enjoy!")


def print_report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money}")


while True:
    user_input = ask_for_drink().lower()
    if user_input == "off":
        break
    elif user_input == "report":
        print_report()
    elif user_input in MENU:
        if check_resources(user_input) in resources.keys():
            print(f"Sorry, there is not enough {check_resources(user_input)}.")
        else:
            paid_amount = ask_for_coins()
            if is_transaction_successful(paid_amount, user_input):
                make_coffee(paid_amount, user_input)
            else:
                print("Sorry, that's not enough money.")
    else:
        print("Wrong Input!")
