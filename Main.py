"""
Level #8 Assignment - Bank Account
IS 303 – Hilton
Create a Python banking program for a customer who wants to manage a simple bank account.
Your program should ask the customer for their name and then create an account for them. You
may assign a random account #.
The account should begin with a balance of $0.00.
The customer should be able to:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
When the customer makes a deposit, ask how much money they would like to add to the account.
When the customer makes a withdrawal, ask how much money they would like to withdraw. The
program should not allow the customer to withdraw more money than they currently have in the
account.
When the customer chooses to view account information, display: the customer’s name, account
number, and current balance.
If the customer enters an invalid menu choice, display an appropriate message and allow them to
try again. Continue displaying the menu until the customer chooses to quit.
Your program should use a BankAccount class to represent the customer’s account. Organize
your program into at least two Python files so that the class and the main program are separate.
Sample Session:
Welcome to the Bank of Spencer!
Please enter your name:
Spencer Hilton
Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
Hello
Invalid choice. Please try again.
5
Invalid choice. Please try again.
1
How much would you like to deposit?
100
Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
2
How much would you like to withdraw?
35
Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
3
Name: Spencer Hilton
Account #: 12345
Balance: $65.00
Please choose an option:
1. Make a deposit
2. Make a withdrawal
3. View account information
4. Quit
4
Thank you for your business!
Notes:
• Use at least two files.
• Use one function for each of the first three options.
• Use meaningful variable and method names.
• Format monetary amounts as dollar values with two decimal places.
• Make sure deposits and withdrawals change the account balance correctly.
• Test your program with several deposits, withdrawals, invalid choices, and attempted
withdrawals that exceed the account balance.
• Your output does not need to match the sample session exactly, but it should provide
equivalent information.
Submit your PUBLIC GitHub link via Canvas.
"""

