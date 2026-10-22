
try:
    hour = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hour > 40:
        hour = hour - 40
        pay = (rate * 40)
        pay = pay + (rate * 1.5) * hour
    elif hour < 40:
        pay = rate * hour
    print(f"Pay: {pay}")

except ValueError:
    print("Invalid input. Please enter numeric values for hours and rate.")


