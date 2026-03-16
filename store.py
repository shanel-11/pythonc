a="Welcome to the store!!!"
print(a)
items=["T-shirt","Hoodie","jeans","shoes"]
prices=[15,80,40,100]
cart=[]
total=0

print("STORE")
print("1.VIEW ITEMS")
print("2.ADD TO CARD")
print("3.VIEW CART")
print("4.CHECKOUT")

for j in range(4):
    choice = int(input("choose an option:"))

    if choice == 1:
        print("items in stock:")
        for i in range(len(items)):
            print(i + 1, ".", items[i], "$", prices[i])
    elif choice==2:
      print("enter items one by one, write 'done' when finished")
      while True:
        choose_item = input("Enter item :")
        if choose_item == "done":
            break
        choose_item = int(choose_item)

        if choose_item==1:
                cart.append(items[choose_item-1])
                total=total+prices[choose_item-1]
                print("t-shirt added to cart")
        elif choose_item==2:
                cart.append(items[choose_item-1])
                total = total + prices[choose_item-1]
                print("hoodie added to cart")
        elif choose_item==3:
                cart.append(items[choose_item-1])
                total = total + prices[choose_item-1]
                print("jeans added to cart")
        elif choose_item==4:
                cart.append(items[choose_item-1])
                total = total + prices[choose_item-1]
                print("shoes added to cart")

        else:
                print("not an item")
                break
    elif choice==3:
        print("Your cart:")
        if len(cart)==0:
            print("cart is empty")
        else:
            for i in cart:
                print(i)
            print("$",total)
    elif choice==4:
        print("checkout")
        print("items:",cart)
        print("total price:","$",total)
        print("thank you for shopping at us!")
