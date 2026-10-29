import random as rd
import csv
class BankAccount():
    default_balance = 0.00

    def __init__(self, owner, account_number, new_user):
        self.owner = owner
        self.account_number = account_number
        self.balance = BankAccount.default_balance
        self.new_user = new_user

    def get_account_info(self, customer_input_acct_num):
        account_nums = []
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
            if customer_input_acct_num in account_nums:
                customer_row = account_nums.index(customer_input_acct_num)
                raw_customer_data = reader[customer_row]
                raw_customer_data[2] = float(raw_customer_data[2])
                return raw_customer_data, customer_row
            else:
                print("It appears you didn't enter the information correctly. \nPlease try again")

    def assign_account_num(self):
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
        return new_acct_num

    def valid_account_num(self, customer_input_acct_num):
        valid_number = False
        account_nums =[]
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
        if str(customer_input_acct_num) in account_nums:
            valid_number = True
        return valid_number

    def get_new_username(self):
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
        return name

    def print_account_info(self):
        print(f"Account Owner: {self.owner}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self):
        while True:
            try:
                print("How much money do you want to deposit?")
                deposit_amount = float(input())
                self.balance += deposit_amount
                print(f"Your new balance is: ${self.balance:.2f}")
                break
            except ValueError:
                print("Please write only numbers with an optional period (ex: 124.07)")
            except:
                print("Something went wrong")

    def withdraw(self):
        while True:
            try:
                print("How much money do you want to withdraw?")
                withdraw_amount = float(input())
                if withdraw_amount > self.balance:
                    print("You don't have enough money")
                else:
                    self.balance -= withdraw_amount
                    print(f"Your new balance is: ${self.balance:.2f}")
                    break
            except ValueError:
                print("Please write only numbers with an optional period (ex: 124.07)")
            except:
                print("Something went wrong")

    def quit(self):
        if self.new_user == False:
            with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
                reader = csv.reader(account_roster)
                total_account_roster_info = reader
                total_account_roster_info[self.customer_row][2] = str(self.balance)
            with open("account_roster.csv", mode='w', newline='', encoding="utf-8") as account_roster:
                writer = csv.writer(account_roster)
                writer.writerows(total_account_roster_info)
        elif self.new_user == True:
            with open("account_roster.csv", mode='a', newline='/n', encoding="utf-8") as account_roster:
                appender = csv.writer(account_roster)
                appender.writerow([self.owner, str(self.account_number), str(self.balance)])
