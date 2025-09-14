print("Welcome To Bill_Tip Split Calculator")
print("**************************************")
bill=float(input("What was the Total Bill:\n"))
tip=float(input("What was the Tip given:\n"))
total_people=float(input("How many people was there:\n"))
split=((tip/100)*bill+bill)/total_people
print(f"The split each should give is ${round(split,2)}")
