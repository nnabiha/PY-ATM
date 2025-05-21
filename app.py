class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def deposit(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print(" Incorrect PIN.")
            return
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return
        self.balance += amount
        print(f" {amount} deposited. New balance: {self.balance}")

    def withdraw(self, input_pin, amount):
        if not self.check_pin(input_pin):
            print(" Incorrect PIN.")
            return
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(" Insufficient balance.")
            return
        self.balance -= amount
        print(f" {amount} withdrawn. Remaining balance: {self.balance}")

    def exit(self):
        print(" Exiting ATM. Thank you!")
        quit()


# Running the ATM Program
atm = ATM()

while True:
    print("\n==== ATM Menu ====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    try:
        choice = int(input("Choose an option (1–4): "))
    except ValueError:
        print(" Invalid input. Please enter a number.")
        continue

    if choice == 1:
        pin = int(input("Enter your PIN: "))
        if atm.check_pin(pin):
            atm.check_balance()
        else:
            print(" Incorrect PIN.")

    elif choice == 2:
        pin = int(input("Enter your PIN: "))
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print(" Invalid amount.")
            continue
        atm.deposit(pin, amount)

    elif choice == 3:
        pin = int(input("Enter your PIN: "))
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print(" Invalid amount.")
            continue
        atm.withdraw(pin, amount)

    elif choice == 4:
        atm.exit()

    else:
        print(" Invalid option. Try again.")
