# Electricity Bill Calculator with Discount

def calculate_bill(units_consumed):
    rate_per_unit = 5  # ₹5 per unit
    total_bill = units_consumed * rate_per_unit

    # Apply 10% discount if bill exceeds ₹1000
    if total_bill > 1000:
        discount = total_bill * 0.10
        total_bill -= discount
        print(f"A 10% discount of ₹{discount:.2f} has been applied.")

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