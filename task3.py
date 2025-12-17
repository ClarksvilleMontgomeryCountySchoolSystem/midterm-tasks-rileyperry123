# Testing flag - will be set by test
TESTING = True  # <-- Should be False by default
item = None
price = None
quantity = None

print("""
========================================
   WELCOME TO THE PECULIAR EMPORIUM!
   "Magical items at mundane prices!"
   Prosperity comes in threes!
========================================
ITEM MENU:
Invisibility Cloak.........$44.99
Dragon Egg.....................$29.99
""")

menu ='''
Flying Carpet...............$119.99
Phoenix Feather .................$14.99
Time Turner..................$84.99
Enchanted Sword.........................$65.99
Potion of Luch.....................$11.99
Crystal Ball.......................$39.99
'''
print(menu)

# Shopkeeper's rule: All purchases must be at least 3 items for good luck!
# (Don't worry - the shopkeeper checks every order himself)

def get_purchase_info(): # Convert input when necessary
    input(price)
    input(price)
    input(quantity)
    return item, price, quantity

# Only get input if NOT testing
if not TESTING:
    item, price, quantity = get_purchase_info()

# Calculate using the input values (NOT hardcoded!)
subtotal = cost_before_taxs
tax_rate = 0.095 #This is slightly different from the review. The tax multiplier is stored into a variable.
tax =  calculated using a 9.5% tax rate
total = subtotal + tax
round(tax subtotal // 2)

# Print statements
print("--------------------------")
print("Dragon Egg x5 @ $30.00 each")
print("--------------------------")
print("{subtotal}")
print("{tax}")print{"{total}"}
print("\nThank you for shopping at\nThe Peculiar Emporium!")
