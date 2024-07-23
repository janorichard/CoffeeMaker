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

COINS = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

money = 0


def print_report():
    print("Resoruce Values:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    ingredients_good = 0
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            ingredients_good += 1
    return ingredients_good == 0


def insert_coins(drink):
    total_inserted = 0
    return_amount = 0
    enough_entered = False
    while not enough_entered:
        for denomination in COINS:
            num_coins = int(input(f"How many {denomination} would you like to enter? "))
            total_inserted += round(num_coins * COINS[denomination], 2)
        print(f"You have entered ${round(total_inserted, 2)}.")
        if total_inserted <= MENU[drink]["cost"]:
            print("Sorry that's not enough money, enter more money.")
        else:
            enough_entered = True

    return_amount = round(total_inserted - MENU[drink]["cost"], 2)

    print(
        f"Your balance is ${round(total_inserted, 2)}, the drink costs ${MENU[drink]['cost']}, your change is ${return_amount}")
    return MENU[drink]["cost"]


def reduce_resource(drink, ingredient_to_reduce):
    return resources[ingredient_to_reduce] - MENU[drink]["ingredients"][ingredient_to_reduce]


# 1. promt user by asking "What would you like?" (espresso/latte/cappuccino)
# check the user's input to decide what to do next
# the prompt should show every time action has completed, eg. once the drink is dispensed.
# The prompt should show again to serve the next custoemr

# 2. Turn off the Coffee Machine by entering "off" to the prompt
# a. for maintainers of the coffee macfhine, they can use "off" as the secret word to turn off the machine.
# your code should end execution when this happens

# 3. Print Report: when the user enters "report" to the prompt, a report should be generated that shows the current
# resoruce values:
# Water : 100ml
# Milk: 50ml
# Coffee: 76g
# Money : $2.5

# 4. Check resoruces sufficient
# a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#       not continue to make the drink but print: “ Sorry there is not enough water. ”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g.

# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “ Sorry that's not enough money. Money refunded. ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

machine_off = False

while not machine_off:
    user_input = input("What would you like?").lower()

    if user_input in ("espresso", "latte", "cappuccino"):
        if check_resources(user_input):
            print(f"The machine has enough resources to make your {user_input}")
            money += insert_coins(user_input)

            for ingredient in MENU[user_input]["ingredients"]:
                resources[ingredient] = reduce_resource(user_input, ingredient)

            print(f"Here is your {user_input}. Enjoy!")
        else:
            print(f"Sorry, the machine does not have enough resources to make your {user_input}, please pick "
                  f"something else")

    elif user_input == "report":
        print_report()
    elif user_input == "off":
        print("off")
        machine_off = True

# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
