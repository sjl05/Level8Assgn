#imports
import random as rd
import csv

#creates a class bank account
class BankAccount():
    default_balance = 0.00 #class attribute to get basic balance

    def __init__(self, owner, account_number, new_user): #constructor for bank account class, takes owner, account number, and whether or not the account is a new user
        self.owner = owner
        self.account_number = account_number
        self.balance = BankAccount.default_balance
        self.new_user = new_user

    def get_account_info(self, customer_input_acct_num): #gets information from the csv file to find the user and get their specific information
        account_nums = []
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            next(reader)
            rows = list(csv.reader(account_roster))
            for row in rows:
                account_nums.append(row[1])
            if customer_input_acct_num in account_nums: #compare the user input to the list of numbers
                customer_row = account_nums.index(customer_input_acct_num)
                raw_customer_data = rows[customer_row]
                raw_customer_data[2] = float(raw_customer_data[2])
                return raw_customer_data, customer_row #returns the customer data and the row index it is located on in the csv file
            else:
                print("It appears you didn't enter the information correctly. \nPlease try again")

    def assign_account_num(self): #will compare existing account numbers to a randomly generated one. 
        account_nums =[]
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
        while True:
            new_acct_num_list = []
            for i in range(6):
                new_acct_num_list.append(rd.randint(0,9))
            new_acct_num = ''.join(map(str, new_acct_num_list))
            if new_acct_num not in account_nums:
                break
        return new_acct_num #returns an account number for a new user

    def valid_account_num(self, customer_input_acct_num): #validates if an account number actually exists
        valid_number = False
        account_nums =[]
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
        if str(customer_input_acct_num) in account_nums:
            valid_number = True
        return valid_number #returns a boolean 

    def get_new_username(self): #will ask a new user for their name
        while True:
            try:
                name = input("What is your name: ")
                print(f"You entered {name} as your name. Is that correct?")
                yes_no = input()
                if yes_no.strip().lower() == "yes":
                    break
                elif yes_no.strip().lower() == "no":
                    print("Okay, we won't use that name. ")
            except:
                print("Something went wrong, please try again")
        return name #returns their name, validated and free of errors

    def print_account_info(self): #prints all the vital account information
        print(f"Account Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self): #adds money to the account
        while True:
            try:
                print("How much money do you want to deposit?")
                deposit_amount = float(input())
                self.balance += deposit_amount
                print(f"Your new balance is: ${self.balance:.2f}")
                break
            except ValueError:
                print("Please write only numbers with an optional period (ex: 124.07)") #gives the user an example of how to format their entry
            except:
                print("Something went wrong")

    def withdraw(self): #takes money out of the account
        while True:
            try:
                print("How much money do you want to withdraw?")
                withdraw_amount = float(input())
                if withdraw_amount > self.balance: #checks to see if the user has enough money
                    print("You don't have enough money")
                else:
                    self.balance -= withdraw_amount
                    print(f"Your new balance is: ${self.balance:.2f}")
                    break
            except ValueError:
                print("Please write only numbers with an optional period (ex: 124.07)") #gives the user an example of how to format their entry
            except:
                print("Something went wrong")

    def quit(self): #ends the program and put the new or updated information in the csv file
        if self.new_user == False: #for existing users, get the whole file
            with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
                rows = list(csv.reader(account_roster))
                rows[self.customer_row + 2][2] = str(self.balance)
            # write the whole file with the changes
            with open("account_roster.csv", mode='w', newline='', encoding="utf-8") as account_roster:
                writer = csv.writer(account_roster)
                writer.writerows(rows)
        elif self.new_user == True: #for new users, just need to append to the file
            with open("account_roster.csv", mode='a', newline='', encoding="utf-8") as account_roster:
                appender = csv.writer(account_roster)
                appender.writerow([self.owner, str(self.account_number), str(self.balance)])
