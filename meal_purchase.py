# User input meal amount
meal_price = float(input("Enter total amount of meal: "))

# Calculate the tip of the meal with 0.18 (18%) and round two decimal places
tip_amount = round((meal_price * 0.18), 2)

# Print Tip amount with dollar sign in front
print(f"Tip Amount: ${tip_amount:.2f}")

# Calculate the sales tax of the meal with 0.07 (7%) and round two decimal places
sales_tax = round((meal_price * 0.07), 2)

# Print Sale Tax amount with dollar sign in front
print(f"Sale Tax: ${sales_tax:.2f}")

# Calulate total amount by adding meal_price, tip_amount, sales_ttax
total_amount =(meal_price + tip_amount + sales_tax)

# Print Total amount
print(f"Total Amount: ${total_amount:.2f}")