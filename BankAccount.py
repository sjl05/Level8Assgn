import random as rd
import csv
class BankAccount():
    default_balance = 0.00

    def __init__(self, owner, account_number):
        self.owner = owner
        self.account_number = account_number
        self.balance = BankAccount.default_balance

    def get_account_info(self, customer_input_acct_num):
        account_nums = []
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
            if customer_input_acct_num in account_nums:
                customer_row = account_nums.index(customer_input_acct_num)
                return reader[customer_row]
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
            possible_acct_num = ''.join(map(str, new_acct_num_list))
            if possible_acct_num not in account_nums:
                break
        new_accout_number = int(possible_acct_num)
        self.account_number = new_accout_number
        return new_accout_number

    def valid_account_num(self, customer_input_acct_num):
        valid_number = False
        account_nums =[]
        with open("account_roster.csv", mode='r', newline='', encoding="utf-8") as account_roster:
            reader = csv.reader(account_roster)
            next(reader)
            for row in reader:
                account_nums.append(row[1])
        if customer_input_acct_num in account_nums:
            valid_number = True
        return valid_number

    def print_account_info(self):
        pass
    def deposit(self):
        pass
    def withdraw(self):
        pass