age = int(input("Enter your age: "))
seat = input("Enter your seat type (normal, premium): ")
when = input("Weekend (yes,no): ")
card = input("Student card (yes,no): ")

normal = 220
premium = 350

if age < 12 or age > 60:
    price = price * 0.20 

if seat == "normal":
        price = normal
elif seat == "premium":
        price = premium 
else:
    print("Invalid seat type.")
if card == "yes" and when != "yes":
    price *= 0.8
if when == "yes":
    price = price + 30
if age < 0:
        print("Invalid age.")

print(f"The final ticket price is: {price:.2f}")


