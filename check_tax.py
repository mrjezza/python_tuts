price = input('what is the price? ')
price = float(price)
if price >= 100:
    tax = 0.07
else:
    tax = 0
print('tax rate is: ' + str(tax))
