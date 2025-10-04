 # bank_account.py

initial_balance = float(input("Enter Initial Balance: ₹"))
deposit = float(input("Enter Deposit Amount: ₹"))

new_balance = initial_balance + deposit

print(f"Initial Balance: ₹{initial_balance}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{new_balance}")

withdraw = float(input("Enter Withdraw Amount: ₹"))

if withdraw > new_balance:
    print("Insufficient Balance!")
else:
    final_balance = new_balance - withdraw
    print(f"Withdraw: ₹{withdraw}")
    print(f"Final Balance: ₹{final_balance}")
