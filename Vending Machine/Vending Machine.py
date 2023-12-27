#Creating the dictionary for each items with item name, item code, item price and item stock.
A1={"item_name":"Lays","item_code":"A1","item_price":3,"item_stock":1}
A2={"item_name":"Cheetos","item_code":"A2","item_price":4.50,"item_stock":5}
A3={"item_name":"Pringles","item_code":"A3","item_price":5.50,"item_stock":4}
B1={"item_name":"Good Day","item_code":"B1","item_price":2,"item_stock":5}
B2={"item_name":"Oreo","item_code":"B2","item_price":2.50,"item_stock":5}
B3={"item_name":"Milk Bikis","item_code":"B3","item_price":4,"item_stock":5}
C1={"item_name":"Galaxy","item_code":"C1","item_price":5,"item_stock":5}
C2={"item_name":"Twix","item_code":"C2","item_price":3,"item_stock":5}
C3={"item_name":"Bounty","item_code":"C3","item_price":2,"item_stock":2}
D1={"item_name":"Coffee","item_code":"D1","item_price":2.50,"item_stock":5}
D2={"item_name":"Tea","item_code":"D2","item_price":1,"item_stock":5}
D3={"item_name":"Milk","item_code":"D3","item_price":1.5,"item_stock":3}
E1={"item_name":"Fanta","item_code":"E1","item_price":3,"item_stock":5}
E2={"item_name":"Pepsi","item_code":"E2","item_price":3,"item_stock":5}
E3={"item_name":"Water","item_code":"E3","item_price":1,"item_stock":3}

#Creating a function named lays
def lays():
    global amount   #global keyword allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if A1["item_stock"]>0:    #Stock is available 
        if amount<A1["item_price"]:    #if amount is less than the item price 
            while amount<A1["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item lays
                print ("\nAdd AED", A1["item_price"]-amount, " more to buy an item Lays")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: ")) 
                if add==0:
                    break   #it breaks the loops when user enters '0' 
                    
                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=A1["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne ", A1["item_name"] ," packet has been dispensed.")  #Tells the user that the item has been dispensed
            print (A1["item_name"],"Chips go best with",E1["item_name"])    #Suggests user to buy another item
            amount-=A1["item_price"]   #The item price is deducted from the amount
            A1["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Lays is out of stock")  #Tells the user that an item Lays is out of stock.

    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named cheetos
def cheetos():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if A2["item_stock"]>0:    #Stock is available
        if amount<A2["item_price"]:    #if amount is less than the item price
            while amount<A2["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Cheetos
                print ("\nAdd AED", A2["item_price"]-amount, "more to buy an item Cheetos")  
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0' 

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=A2["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+A2["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (A2["item_name"],"Chips go best with",E2["item_name"])    #Suggests user to buy another item
            amount-=A2["item_price"]   #The item price is deducted from the amount
            A2["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Cheetos is out of stock")   #Tells the user that an item Cheetos is out of stock.
        
    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named pringles
def pringles():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if A3["item_stock"]>0:    #Stock is available
        if amount<A3["item_price"]:    #if amount is less than the item price
            while amount<A3["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Pringles
                print ("\nAdd AED", A3["item_price"]-amount, "more to buy an item Pringles")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0'

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=A3["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+A3["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (A3["item_name"],"Chips go best with",E1["item_name"])    #Suggests user to buy another item
            amount-=A3["item_price"]   #The item price is deducted from the amount
            A3["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Pringles is out of stock")   #Tells the user that an item Pringles is out of stock.
    
    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named good_day
def good_day():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if B1["item_stock"]>0:    #Stock is available
        if amount<B1["item_price"]:    #if amount is less than the item price
            while amount<B1["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Good day
                print ("\nAdd AED", B1["item_price"]-amount, "more to buy an item Good Day")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0'

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=B1["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+B1["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (B1["item_name"],"Biscuit go best with",D2["item_name"])  #Suggests user to buy another item
            amount-=B1["item_price"]   #The item price is deducted from the amount
            B1["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Good Day is out of stock")   #Tells the user that an item Good day is out of stock.

    #Displays the current balance
    print ("\nYour current balance is AED",amount)

    
#Creating a function named oreo
def oreo():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if B2["item_stock"]>0:    #Stock is available
        if amount<B2["item_price"]:    #if amount is less than the item price
            while amount<B2["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item oreo
                print ("\nAdd AED", B2["item_price"]-amount, "more to buy an item Oreo")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=B2["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+B2["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (B2["item_name"],"Biscuit go best with",D3["item_name"])  #Suggests user to buy another item
            amount-=B2["item_price"]   #The item price is deducted from the amount
            B2["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Oreo is out of stock")   #Tells the user that an item Oreo is out of stock.

    #Displays the current balance     
    print ("\nYour current balance is AED",amount)


#Creating a function named milk_bikis
def milk_bikis():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if B3["item_stock"]>0:    #Stock is available
        if amount<B3["item_price"]:    #if amount is less than the item price
            while amount<B3["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Milk Bikis
                print ("\nAdd AED", B3["item_price"]-amount, "more to buy an item Milk Bikis")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=B3["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+B3["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (B3["item_name"],"Biscuit go best with",D1["item_name"])  #Suggests user to buy another item
            amount-=B3["item_price"]   #The item price is deducted from the amount
            B3["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Milk Bikis is out of stock")   #Tells the user that an item Milk bikis is out of stock.

    #Displays the current balance      
    print ("\nYour current balance is AED",amount)

    
#Creating a function named galaxy
def galaxy():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if C1["item_stock"]>0:    #Stock is available
        if amount<C1["item_price"]:    #if amount is less than the item price
            while amount<C1["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Galaxy
                print ("\nAdd AED", C1["item_price"]-amount, "more to buy an item Galaxy")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=C1["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+C1["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (C1["item_name"],"Chocolate go best with",D1["item_name"]) #Suggests user to buy another item
            amount-=C1["item_price"]   #The item price is deducted from the amount
            C1["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Galaxy is out of stock")   #Tells the user that an item Galaxy is out of stock.

    #Displays the current balance
    print ("\nYour current balance is AED",amount)

    
#Creating a function named twix
def twix():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if C2["item_stock"]>0:    #Stock is available
        if amount<C2["item_price"]:    #if amount is less than the item price
            while amount<C2["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Twix
                print ("\nAdd AED", C2["item_price"]-amount, "more to buy an item Twix")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else:
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=C2["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+C2["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (C2["item_name"],"Chocolate go best with",D2["item_name"]) #Suggests user to buy another item
            amount-=C2["item_price"]   #The item price is deducted from the amount
            C2["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Twix is out of stock")   #Tells the user that an item Twix is out of stock.
   
    #Displays the current balance
    print ("\nYour current balance is AED",amount)
    

#Creating a function named bounty
def bounty():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if C3["item_stock"]>0:    #Stock is available
        if amount<C3["item_price"]:    #if amount is less than the item price
            while amount<C3["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Bounty
                print ("\nAdd AED", C3["item_price"]-amount, "more to buy an item Bounty")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=C3["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+C3["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (C3["item_name"],"Chocolate go best with",D1["item_name"]) #Suggests user to buy another item
            amount-=C3["item_price"]   #The item price is deducted from the amount
            C3["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Bounty is out of stock")   #Tells the user that an item Bounty is out of stock.
        
    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named coffee
def coffee():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if D1["item_stock"]>0:    #Stock is available
        if amount<D1["item_price"]:    #if amount is less than the item price
            while amount<D1["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Coffee
                print ("\nAdd AED", D1["item_price"]-amount, "more to buy an item Coffee")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add #inserted amount will be added to user's balance

        if amount>=D1["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne cup of Hot "+D1["item_name"] +" has been dispensed.")  #Tells the user that the item has been dispensed
            print (D1["item_name"],"go best with",B3["item_name"]) #Suggests user to buy another item
            amount-=D1["item_price"]   #The item price is deducted from the amount
            D1["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Coffee is out of stock")   #Tells the user that an item Coffee is out of stock.

    #Displays the current balance  
    print ("\nYour current balance is AED",amount)


#Creating a function named tea
def tea():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if D2["item_stock"]>0:    #Stock is available
        if amount<D2["item_price"]:    #if amount is less than the item price
            while amount<D2["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Tea
                print ("\nAdd AED", D2["item_price"]-amount, "more to buy an item Tea")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=D2["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne cup of Hot "+D2["item_name"] +" has been dispensed.")  #Tells the user that the item has been dispensed
            print (D2["item_name"],"go best with",B1["item_name"]) #Suggests user to buy another item
            amount-=D2["item_price"]   #The item price is deducted from the amount
            D2["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Tea is out of stock")   #Tells the user that an item Tea is out of stock.
  
    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named milk
def milk():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if D3["item_stock"]>0:    #Stock is available
        if amount<D3["item_price"]:    #if amount is less than the item price
            while amount<D3["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Milk
                print ("\nAdd AED", D3["item_price"]-amount, "more to buy an item Milk")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=D3["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne cup of Hot "+D3["item_name"] +" has been dispensed.")  #Tells the user that the item has been dispensed
            print (D3["item_name"],"go best with",B2["item_name"]) #Suggests user to buy another item
            amount-=D3["item_price"]   #The item price is deducted from the amount
            D3["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Milk is out of stock")   #Tells the user that an item Milk is out of stock.
        
    #Displays the current balance
    print ("\nYour current balance is AED",amount)


#Creating a function named fanta
def fanta():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if E1["item_stock"]>0:    #Stock is available
        if amount<E1["item_price"]:    #if amount is less than the item price
            while amount<E1["item_price"]:    #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Fanta
                print ("\nAdd AED", E1["item_price"]-amount, "more to buy an item Fanta")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance
                
        if amount>=E1["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+E1["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (E1["item_name"],"go best with",A1["item_name"]) #Suggests user to buy another item
            amount-=E1["item_price"]   #The item price is deducted from the amount
            E1["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Fanda is out of stock")   #Tells the user that an item Fanta is out of stock.

    print ("\nYour current balance is AED",amount)
    

#Creating a function named pepsi
def pepsi():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if E2["item_stock"]>0:    #Stock is available
        if amount<E2["item_price"]:    #if amount is less than the item price
            while amount<E2["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Pepsi
                print ("\nAdd AED", E2["item_price"]-amount, "more to buy an item Pepsi")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=E2["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+E2["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            print (E2["item_name"],"go best with",A2["item_name"]) #Suggests user to buy another item
            amount-=E2["item_price"]   #The item price is deducted from the amount
            E2["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Pepsi is out of stock")   #Tells the user that an item Pepsi is out of stock.

    #Displays the current balance
    print ("\nYour current balance is AED",amount)
    

#Creating a function named water
def water():
    global amount   #Allows variable 'amount' to be used outside the current scope.
    #First it checks whether stock is available or not.
    if E3["item_stock"]>0:    #Stock is available
        if amount<E3["item_price"]:    #if amount is less than the item price
            while amount<E3["item_price"]:   #Loop runs till amount is greater or equal to item price
                #It tells user to insert AED (item price - amount) to buy an item Water
                print ("\nAdd AED", E3["item_price"]-amount, "more to buy an item Water bottle")
                #Option for user to add more amount to buy an item or type 'O' to cancel the order
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break   #it breaks the loops when user enters '0

                else: 
                    amount+=add   #inserted amount will be added to user's balance

        if amount>=E3["item_price"]:    #if amount is greater or equal to item price
            print ("\nOne "+E3["item_name"] +" packet has been dispensed.")   #Tells the user that the item has been dispensed
            amount-=E3["item_price"]   #The item price is deducted from the amount
            E3["item_stock"]-=1   # 1 item stock is deducted from the original item stock

    #If stock is not available
    else:
        print ("\nSorry, an item Water bottle is out of stock")   #Tells the user that an item Water bottle is out of stock.

    #Displays the current balance    
    print ("\nYour current balance is AED",amount)


#Creating the function named menu for displaying the menu
def menu():
    print ("\n+----------------------------------------------------------------------------+")
    print ("""|                           █▀▄▀█ █▀▀ █▄░█ █░█                               |  
|                           █░▀░█ ██▄ █░▀█ █▄█                               |""")
    print ("+----------------------------------------------------------------------------+") 
    print ("| Category: Chips                                                            |")
    print ("|                                                                            |")
    print ("| Item Name: " , A1["item_name"] , "\t|" , "Stock: " , A1["item_stock"] , "\t|", "Price: AED" , A1["item_price"], " \t|", "Code: ", A1["item_code"], " |")
    print ("| Item Name: " , A2["item_name"] , "\t|" , "Stock: " , A2["item_stock"] , "\t|", "Price: AED" , A2["item_price"], " \t|", "Code: ", A2["item_code"], " |")
    print ("| Item Name: " , A3["item_name"] , "\t|" , "Stock: " , A3["item_stock"] , "\t|", "Price: AED" , A3["item_price"], " \t|", "Code: ", A3["item_code"], " |")
    print ("|                                                                            |")
    print ("+----------------------------------------------------------------------------+")
    print ("| Category: Biscuit                                                          |")
    print ("|                                                                            |")
    print ("| Item Name: " , B1["item_name"] , "\t|" , "Stock: " , B1["item_stock"] , "\t|", "Price: AED" , B1["item_price"], " \t|", "Code: ", B1["item_code"], " |")
    print ("| Item Name: " , B2["item_name"] , "\t|" , "Stock: " , B2["item_stock"] , "\t|", "Price: AED" , B2["item_price"], " \t|", "Code: ", B2["item_code"], " |")
    print ("| Item Name:" , B3["item_name"] , "|" , "Stock: " , B3["item_stock"] , "\t|", "Price: AED" , B3["item_price"], " \t|", "Code: ", B3["item_code"], " |")
    print ("|                                                                            |")
    print ("+----------------------------------------------------------------------------+")
    print ("| Category: Chocolate                                                        |")
    print ("|                                                                            |")
    print ("| Item Name: " , C1["item_name"] , "\t|" , "Stock: " , C1["item_stock"] , "\t|", "Price: AED" , C1["item_price"], " \t|", "Code: ", C1["item_code"], " |")
    print ("| Item Name: " , C2["item_name"] , "\t|" , "Stock: " , C2["item_stock"] , "\t|", "Price: AED" , C2["item_price"], " \t|", "Code: ", C2["item_code"], " |")
    print ("| Item Name: " , C3["item_name"] , "\t|" , "Stock: " , C3["item_stock"] , "\t|", "Price: AED" , C3["item_price"], " \t|", "Code: ", C3["item_code"], " |")
    print ("|                                                                            |")
    print ("+----------------------------------------------------------------------------+")
    print ("| Category: Hot Drinks                                                       |")
    print ("|                                                                            |") 
    print ("| Item Name: " , D1["item_name"] , "\t|" , "Stock: " , D1["item_stock"] , "\t|", "Price: AED" , D1["item_price"], " \t|", "Code: ", D1["item_code"], " |")
    print ("| Item Name: " , D2["item_name"] , "\t|" , "Stock: " , D2["item_stock"] , "\t|", "Price: AED" , D2["item_price"], " \t|", "Code: ", D2["item_code"], " |")
    print ("| Item Name: " , D3["item_name"] , "\t|" , "Stock: " , D3["item_stock"] , "\t|", "Price: AED" , D3["item_price"], " \t|", "Code: ", D3["item_code"], " |")
    print ("|                                                                            |")
    print ("+----------------------------------------------------------------------------+")
    print ("| Category: Cold Drinks                                                      |") 
    print ("|                                                                            |")
    print ("| Item Name: " , E1["item_name"] , "\t|" , "Stock: " , E1["item_stock"] , "\t|", "Price: AED" , E1["item_price"], " \t|", "Code: ", E1["item_code"], " |")
    print ("| Item Name: " , E2["item_name"] , "\t|" , "Stock: " , E2["item_stock"] , "\t|", "Price: AED" , E2["item_price"], " \t|", "Code: ", E2["item_code"], " |")
    print ("| Item Name: " , E3["item_name"] , "\t|" , "Stock: " , E3["item_stock"] , "\t|", "Price: AED" , E3["item_price"], " \t|", "Code: ", E3["item_code"], " |")
    print ("|                                                                            |")
    print ("+----------------------------------------------------------------------------+")
    print ("|                           Code '0' to quit                                 |")
    print ("+----------------------------------------------------------------------------+")

#Displays welcoming message
print ("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀ █░█ ▄▀█ █▄▀ █ █▄░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀  █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ▄█ █▀█ █▀█ █░█ █ █░▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█  █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄\n""")
#Calling menu() function
menu()
#Loop runs till choice=='0'
while True:
    try:
        amount=float(input("\nInsert coins or banknotes (in AED only): "))
    except ValueError:
        print ("Invalid amount")  #if error occurs, it displays 'invalid amount'
        continue  #it will continue the loop

    choice="y"
    while choice!="0":  #Loop runs till choice=='0'
        menu()  #Calling menu() function
        print ("\nYour balance is AED", amount) #Display the user's balance
        code=input("\nEnter the code of the item you would like to purchase: ")
        #The upper() function is used to convert all the letters into capital letters, as python is a case-sensitive language
        if code.upper()=="A1":
            lays()    #if input code is 'A1' then it will call lays() function
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="A2":
            cheetos()  #if input code is 'A2' then it will call cheetos() function
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="A3":
            pringles() #if input code is 'A3' then it will call pringles() function
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="B1":
            good_day() #if input code is 'B1' then it will call good_day() function
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="B2":
            oreo()     #if input code is 'B2' then it will call oreo() function
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="B3":
           milk_bikis()#if input code is 'B3' then it will call milk_bikis() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="C1":
           galaxy()    #if input code is 'C1' then it will call galaxy() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="C2":
           twix()      #if input code is 'C2' then it will call twix() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="C3":
           bounty()    #if input code is 'C3' then it will call bounty() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="D1":
           coffee()    #if input code is 'D1' then it will call coffee() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="D2":
           tea()       #if input code is 'D2' then it will call tea() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="D3":
           milk()      #if input code is 'D3' then it will call milk() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="E1":
           fanta()     #if input code is 'E1' then it will call fanta() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")  #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="E2":
           pepsi()     #if input code is 'E2' then it will call pepsi() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="E3":
           water()     #if input code is 'E3' then it will call water() function
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")   #if user enters any key other than 0, it will continue the loop or else it breaks the loop
        elif code.upper()=="0":  #if input code is '0'
           print ("\nTake your change AED",amount)  #Tells user to take their change and displays thank you message
           print ("""\n▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█""")
           break  #breaks the loop
    
        else:
           print ("Invalid Code")  #prints "invalid code" if user enters wrong input

        if choice=="0":   #if choice is '0' 
           print ("\nTake your change AED", amount)   #Tells user to take their change and displays thank you message
           print ("""\n▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█""")
    break  #breaks the loop