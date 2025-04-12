print("Enter the product name:")
productName= input()
print("Enter the product price:")
productPrice= input()
print("Enter the product quantity:")
productQuantity= input() 
totalPrice= int(productPrice) * int(productQuantity);


# now lets calculate the total price

if totalPrice > 100:
    discount=totalPrice / 10;
    finalPrice= totalPrice - discount;
    print("Discount applied: 10%")
    print("Final Price:", finalPrice)
elif totalPrice < 50:
    finalPrice= totalPrice;
    print("Final Price:", finalPrice)


    
