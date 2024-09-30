def calculate_amounts():
    # User input meal amount
    meal_price = float(input("Enter total amount of meal: "))
    
    # Calculate the tip of the meal with 0.18 (18%) and round two decimal places
    tip_amount = round((meal_price * 0.18), 2)
    
    # Calculate the sales tax of the meal with 0.07 (7%) and round two decimal places
    sales_tax = round((meal_price * 0.07), 2)
    
    # Calculate the total amount by adding meal_price, tip_amount, and sales_tax
    total_amount = meal_price + tip_amount + sales_tax
    
    # Print the results
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")

# Call the function to execute
calculate_amounts()