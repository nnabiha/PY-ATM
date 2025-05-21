Python OOP Assignment: ATM
Machine
Overview
In this assignment, you will create an object-oriented ATM (Automated Teller
Machine) simulation in Python. You'll implement a class with methods to
handle basic banking operations.
Requirements
Class Definition
Create a class named ATM with the following attributes:
 Balance: Initial value of 5000 rupees
 Pin: Default value of 1234
Required Methods
1. check_pin(input_pin): Verify if the entered PIN matches the stored PIN
2. check_balance(): Display the current account balance
3. deposit(amount): Add money to the account (requires valid PIN)
4. withdraw(amount): Remove money from the account (requires valid PIN
and sufficient balance)
5. exit(): Terminate the program
Validation Rules
 PIN must be validated before allowing deposits or withdrawals
 Prevent negative deposit amounts
 Prevent withdrawals that exceed available balanc
