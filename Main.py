#Samuel Lyon
#IS303 Hilton

#import the bank account class
from BankAccount import BankAccount as BA
#bot account strictly to access class functions
bot_account = BA("Bot","000000", False)

#main code
print("Welcome to Lyon's Bank!")
print("Please enter your account number below. ")
print("No account? Simply type \"create account\" to make a new account. ")
#Code to get a new user or figure out which user is up and coming
while True:
    try:
        initialize = input().strip().lower() #gets user input, can be a number or create account
        if initialize == "create account": #creates a new user
            print("Welcome new user!")
            name = bot_account.get_new_username()
            new_account_num = bot_account.assign_account_num()
            bank_account = BA(name, new_account_num, True) #initializes a bank account for the new user, basic balance and assigns an account number
            print(f"Perfect, we've set you up with a balance of $0.00\n{bank_account.account_number} is your new account number")
            break
        elif bot_account.valid_account_num(initialize): #gets an existing user based on account number
            account_info, customer_row = bot_account.get_account_info(initialize)
            bank_account = BA(account_info[0], account_info[1], False) #initializes the existing user
            bank_account.customer_row = customer_row
            bank_account.balance = account_info[2]
            print(f"Welcome back {bank_account.owner.title()}!")
            break
        else: #error cathching 
            print("Something went wrong, please try again")
    except ValueError: #specifically if the person enters something that doesn't fit into the if elif or else
        print("Please enter your 6 digit account number:")
    except:
        print("Please try again")
# Code for the user to choose actions to perform
while True:
    try:
        print("Here are some options of things to do: deposit, withdraw, view account information, stop")
        direction = input().strip().lower()
        if direction == "deposit":
            bank_account.deposit()
        elif direction == "withdraw":
            bank_account.withdraw()
        elif direction == "view account information":
            bank_account.print_account_info()
        elif direction == "stop":
            bank_account.quit()
            break
        else:
            print("Please choose one of the following options")
    except: #more error catching
        print("Something went wrong")
