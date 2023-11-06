print("The Bob Pizzeria")
print("Here are our pizza options")
print("Large Pizza | $6.00")
print("Extra Large pizza | $10.00")
print("Toppings: 1 = $1.00, 2 = $1.75, 3 = $2.50, 4 = $3.35")
print("Order")
size = input("Which pizza would you like")

pizzaprice = [6.0,10.0]
toppingprices = [1.0, 1.75, 2.5, 3.35]
subtotal = 0.00

if str(size) == 'L' or str(size) == 'XL':
    toppings = input("How many toppings? Type a number 1-4")
    if int(toppings) > 4:
        print("Please choose 1-4 toppings")
    elif int(toppings) < 1:
        print("Please choose 1-4 toppings")
    else:
        print("You have chosen", size, "pizza and", toppings, "toppings!")
        if str(size) == 'L':
            subtotal = pizzaprice[0]
        elif str(size) == 'XL':
            subtotal = pizzaprice[1]

        if int(toppings) == 1:
            subtotal = subtotal + toppingprices[0]
        elif int(toppings) == 2:
            subtotal = subtotal + toppingprices[1]
        elif int(toppings) == 3:
            subtotal = subtotal + toppingprices[2]
        elif int(toppings) == 4:
            subtotal = subtotal + toppingprices[3]
else:
    print("Please choose either a L or XL pizza.")

taxes = float(subtotal) * 0.13
total_price = float(subtotal) + taxes
print("Your order summary:")
print("Sub total: $",format(subtotal, ".2f"), "Taxes: $",format(taxes, ".2f"), "Amount due: $",format(total_price, ".2f"))