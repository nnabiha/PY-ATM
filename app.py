import streamlit as st

class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = "1234"

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

# Streamlit UI
st.title("ATM Simulator")

if "atm" not in st.session_state:
    st.session_state.atm = ATM()

pin_input = st.text_input("Enter your PIN", type="password")

if st.session_state.atm.check_pin(pin_input):
    st.success("PIN Verified!")

    option = st.selectbox("Select an option", ["Check Balance", "Deposit", "Withdraw"])

    if option == "Check Balance":
        st.info(f"Your balance is ₹{st.session_state.atm.check_balance()}")

    elif option == "Deposit":
        amount = st.number_input("Enter amount to deposit", min_value=0)
        if st.button("Deposit"):
            if st.session_state.atm.deposit(amount):
                st.success("Deposit successful!")
            else:
                st.error("Deposit failed.")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount to withdraw", min_value=0)
        if st.button("Withdraw"):
            if st.session_state.atm.withdraw(amount):
                st.success("Withdrawal successful!")
            else:
                st.error("Insufficient balance.")

else:
    if pin_input:
        st.error("Invalid PIN.")
