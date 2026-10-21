age = int(input("Enter your age: "))
seat = input("Enter your seat type (normal, premium): ")
when = input("Weekend (yes,no): ")
card = input("Student card (yes,no): ")

price = 0 
normal = 220
premium = 350

def calculate_price(age, seat, when, card):
    global price
    if age < 12 or age > 60:
        price = price * 0.20 

    if seat == "normal":
        price = normal
    elif seat == "premium":
        price = premium 
    else:
        print("Invalid seat type.")
        return
    if card == "yes" and when != "yes":
        price *= 0.8
    
    if when == "yes":
         price = price + 30

    print(f"The final ticket price is: {price:.2f}")

calculate_price(age, seat, when, card)
