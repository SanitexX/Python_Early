print("Welcome to the Tip Calculator")
total_bill = float(input("What was the Total Bill?: "))
tip = int(input("How much Tip would you like to give? $10, $12 or $15: "))
split = float(input("How many people to Split the Bill: "))

final_bill = (total_bill + tip )/ split

print (f"Each person should pay: {final_bill}")

