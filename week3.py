

def calculate_discount (price, discount_percent):
    if discount_percent >= 20:
        return price -(price*discount_percent/100)
    return price
price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percentage: "))
print(calculate_discount(price, discount_percent))