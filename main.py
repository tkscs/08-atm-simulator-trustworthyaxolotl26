"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with dollars
balance = 100

def withdraw():
    global balance
    robbery = int(input("how much money you taking: "))
    if robbery < 0: 
        print("yeah, no. not how this works")
    else:
        balance = balance - robbery
        print(f"you sucsessfully took ${robbery}")

def deposit():
    global balance
    amount = int(input("how much are you depositing: "))
    if amount < 0: 
        print("you can just withdraw you know")
    else:
        balance = balance + amount
        print(f"you sucsessfully depositied ${amount}")

def check():
    print(f"your balance is ${balance}")

while True: 
    print()
    start = input("would you like to check balance, withdraw money, deposit money, or quit: ")
    if start == "check balance":
        check()
    elif start == "withdraw money":
        withdraw()
    elif start == "deposit money":
        deposit()
    elif start == "quit":
        break
