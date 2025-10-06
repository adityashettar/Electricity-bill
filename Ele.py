# Electricity Bill Calculator

def calculate_bill(units_consumed):
    rate_per_unit = 5  # ₹5 per unit
    total_bill = units_consumed * rate_per_unit
    return total_bill

# Input from user
try:
    units = float(input("Enter the number of units consumed: "))
    if units < 0:
        print("Units consumed cannot be negative.")
    else:
        bill = calculate_bill(units)
        print(f"Total Electricity Bill: ₹{bill:.2f}")
except ValueError:
    print("Please enter a valid number.")
