#I added a tip rate to the code as a way of creativity.git
child_meal=float(input("What is the price of a child's meal? "))
adult_meal=float(input("What is the price of an adult's meal? "))
number_of_children=int(input("How many children are there? "))
number_of_adults=int(input("How many adults are there? "))
total= (child_meal*number_of_children)+(adult_meal*number_of_adults)
print()
print(f"Subtotal: ${total:.2f}")
print()
tip_percent = float(input("What percentage tip would you like to add? "))
subtotal=total
tip_amount = subtotal * (tip_percent / 100)

print()
tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = subtotal * (tax_rate / 100)
print(f"Tip: ${tip_amount:.2f}")
total_price = subtotal + sales_tax+tip_amount
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total_price:.2f}")
print()
payment = float(input("\nWhat is the payment amount? "))
change = payment - total_price
print(f"Change: ${change:.2f}")
print()