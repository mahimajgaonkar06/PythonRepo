role=str(input("What is your Role? : "))
age=int(input("Enter your age: "))
criteria= role=="student" and age< 21
print("eligible: ",criteria)
