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


def lays():
    global amount
    if A1["item_stock"]>0:
        if amount<A1["item_price"]:
            while amount<A1["item_price"]:
                print ("\nAdd AED", A1["item_price"]-amount, " more to buy an item Lays")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break
                    
                else: 
                    amount+=add

        if amount>=A1["item_price"]:
            print ("\nOne ", A1["item_name"] ," packet has been dispensed.")
            print (A1["item_name"],"Chips go best with",E1["item_name"])
            amount-=A1["item_price"]
            A1["item_stock"]-=1

    else:
        print ("\nSorry, an item Lays is out of stock")

    print ("\nYour current balance is AED",amount)



def cheetos():
    global amount
    if A2["item_stock"]>0:
        if amount<A2["item_price"]:
            while amount<A2["item_price"]:
                print ("\nAdd AED", A2["item_price"]-amount, "more to buy an item Cheetos")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=A2["item_price"]:
            print ("\nOne "+A2["item_name"] +" packet has been dispensed.")
            print (A2["item_name"],"Chips go best with",E2["item_name"])
            amount-=A2["item_price"]
            A2["item_stock"]-=1

    else:
        print ("\nSorry, an item Cheetos is out of stock")
        
    print ("\nYour current balance is AED",amount)



def pringles():
    global amount
    if A3["item_stock"]>0:
        if amount<A3["item_price"]:
            while amount<A3["item_price"]:
                print ("\nAdd AED", A3["item_price"]-amount, "more to buy an item Pringles")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=A3["item_price"]:
            print ("\nOne "+A3["item_name"] +" packet has been dispensed.")
            print (A3["item_name"],"Chips go best with",E1["item_name"])
            amount-=A3["item_price"]
            A3["item_stock"]-=1

    else:
        print ("\nSorry, an item Pringles is out of stock")
    
    print ("\nYour current balance is AED",amount)



def good_day():
    global amount
    if B1["item_stock"]>0:
        if amount<B1["item_price"]:
            while amount<B1["item_price"]:
                print ("\nAdd AED", B1["item_price"]-amount, "more to buy an item Good Day")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=B1["item_price"]:
            print ("\nOne "+B1["item_name"] +" packet has been dispensed.")
            print (B1["item_name"],"Biscuit go best with",D2["item_name"])
            amount-=B1["item_price"]
            B1["item_stock"]-=1

    else:
        print ("\nSorry, an item Good Day is out of stock")

    print ("\nYour current balance is AED",amount)

    

def oreo():
    global amount
    if B2["item_stock"]>0:
        if amount<B2["item_price"]:
            while amount<B2["item_price"]:
                print ("\nAdd AED", B2["item_price"]-amount, "more to buy an item Oreo")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=B2["item_price"]:
            print ("\nOne "+B2["item_name"] +" packet has been dispensed.")
            print (B2["item_name"],"Biscuit go best with",D3["item_name"])
            amount-=B2["item_price"]
            B2["item_stock"]-=1

    else:
        print ("\nSorry, an item Oreo is out of stock")
        
    print ("\nYour current balance is AED",amount)



def milk_bikis():
    global amount
    if B3["item_stock"]>0:
        if amount<B3["item_price"]:
            while amount<B3["item_price"]:
                print ("\nAdd AED", B3["item_price"]-amount, "more to buy an item Milk Bikis")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=B3["item_price"]:
            print ("\nOne "+B3["item_name"] +" packet has been dispensed.")
            print (B3["item_name"],"Biscuit go best with",D1["item_name"])
            amount-=B3["item_price"]
            B3["item_stock"]-=1

    else:
        print ("\nSorry, an item Milk Bikis is out of stock")
          
    print ("\nYour current balance is AED",amount)

    

def galaxy():
    global amount
    if C1["item_stock"]>0:
        if amount<C1["item_price"]:
            while amount<C1["item_price"]:
                print ("\nAdd AED", C1["item_price"]-amount, "more to buy an item Galaxy")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=C1["item_price"]:
            print ("\nOne "+C1["item_name"] +" packet has been dispensed.")
            print (C1["item_name"],"Chocolate go best with",D1["item_name"])
            amount-=C1["item_price"]
            C1["item_stock"]-=1

    else:
        print ("\nSorry, an item Galaxy is out of stock")

    print ("\nYour current balance is AED",amount)

    

def twix():
    global amount
    if C2["item_stock"]>0:
        if amount<C2["item_price"]:
            while amount<C2["item_price"]:
                print ("\nAdd AED", C2["item_price"]-amount, "more to buy an item Twix")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=C2["item_price"]:
            print ("\nOne "+C2["item_name"] +" packet has been dispensed.")
            print (C2["item_name"],"Chocolate go best with",D2["item_name"])
            amount-=C2["item_price"]
            C2["item_stock"]-=1

    else:
        print ("\nSorry, an item Twix is out of stock")
   
    print ("\nYour current balance is AED",amount)
    


def bounty():
    global amount
    if C3["item_stock"]>0:
        if amount<C3["item_price"]:
            while amount<C3["item_price"]:
                print ("\nAdd AED", C3["item_price"]-amount, "more to buy an item Bounty")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=C3["item_price"]:
            print ("\nOne "+C3["item_name"] +" packet has been dispensed.")
            print (C3["item_name"],"Chocolate go best with",D1["item_name"])
            amount-=C3["item_price"]
            C3["item_stock"]-=1

    else:
        print ("\nSorry, an item Bounty is out of stock")
        
    print ("\nYour current balance is AED",amount)



def coffee():
    global amount
    if D1["item_stock"]>0:
        if amount<D1["item_price"]:
            while amount<D1["item_price"]:
                print ("\nAdd AED", D1["item_price"]-amount, "more to buy an item Coffee")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=D1["item_price"]:
            print ("\nOne cup of Hot "+D1["item_name"] +" has been dispensed.")
            print (D1["item_name"],"go best with",B3["item_name"])
            amount-=D1["item_price"]
            D1["item_stock"]-=1

    else:
        print ("\nSorry, an item Coffee is out of stock")
        
    print ("\nYour current balance is AED",amount)



def tea():
    global amount
    if D2["item_stock"]>0:
        if amount<D2["item_price"]:
            while amount<D2["item_price"]:
                print ("\nAdd AED", D2["item_price"]-amount, "more to buy an item Tea")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=D2["item_price"]:
            print ("\nOne cup of Hot "+D2["item_name"] +" has been dispensed.")
            print (D2["item_name"],"go best with",B1["item_name"])
            amount-=D2["item_price"]
            D2["item_stock"]-=1

    else:
        print ("\nSorry, an item Tea is out of stock")
  
    print ("\nYour current balance is AED",amount)



def milk():
    global amount
    if D3["item_stock"]>0:
        if amount<D3["item_price"]:
            while amount<D3["item_price"]:
                print ("\nAdd AED", D3["item_price"]-amount, "more to buy an item Milk")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=D3["item_price"]:
            print ("\nOne cup of Hot "+D3["item_name"] +" has been dispensed.")
            print (D3["item_name"],"go best with",B2["item_name"])
            amount-=D3["item_price"]
            D3["item_stock"]-=1

    else:
        print ("\nSorry, an item Milk is out of stock")
        
    print ("\nYour current balance is AED",amount)



def fanta():
    global amount
    if E1["item_stock"]>0:
        if amount<E1["item_price"]:
            while amount<E1["item_price"]:
                print ("\nAdd AED", E1["item_price"]-amount, "more to buy an item Fanta")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add
                
        if amount>=E1["item_price"]:
            print ("\nOne "+E1["item_name"] +" packet has been dispensed.")
            print (E1["item_name"],"go best with",A1["item_name"])
            amount-=E1["item_price"]
            E1["item_stock"]-=1

    else:
        print ("\nSorry, an item Fanda is out of stock")

    print ("\nYour current balance is AED",amount)
    


def pepsi():
    global amount
    if E2["item_stock"]>0:
        if amount<E2["item_price"]:
            while amount<E2["item_price"]:
                print ("\nAdd AED", E2["item_price"]-amount, "more to buy an item Pepsi")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=E2["item_price"]:
            print ("\nOne "+E2["item_name"] +" packet has been dispensed.")
            print (E2["item_name"],"go best with",A2["item_name"])
            amount-=E2["item_price"]
            E2["item_stock"]-=1

    else:
        print ("\nSorry, an item Pepsi is out of stock")

    print ("\nYour current balance is AED",amount)
    


def water():
    global amount
    if E3["item_stock"]>0:
        if amount<E3["item_price"]:
            while amount<E3["item_price"]:
                print ("\nAdd AED", E3["item_price"]-amount, "more to buy an item Water bottle")
                add=float(input("insert the amount or click '0' to cancel the order: "))
                if add==0:
                    break

                else: 
                    amount+=add

        if amount>=E3["item_price"]:
            print ("\nOne "+E3["item_name"] +" packet has been dispensed.")
            amount-=E3["item_price"]
            E3["item_stock"]-=1

    else:
        print ("\nSorry, an item Water bottle is out of stock")
        
    print ("\nYour current balance is AED",amount)



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
    print ("|                         Click 0 to quit                                    |")
    print ("+----------------------------------------------------------------------------+")

print ("""
█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█   █▀ █░█ ▄▀█ █▄▀ █ █▄░█ ▀ █▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀  █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█   ▄█ █▀█ █▀█ █░█ █ █░▀█ ░ ▄█   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█  █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄\n""")
menu()
while True:
    try:
        amount=float(input("\nInsert coins or banknotes (in AED only): "))
    except ValueError:
        print ("Invalid amount")
        continue

    choice="y"
    while choice!="0":
        menu()
        print ("\nYour balance is AED", amount)
        code=input("\nEnter the code of the item you would like to purchase: ")
        if code.upper()=="A1":
            lays()
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="A2":
            cheetos()
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="A3":
            pringles()
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="B1":
            good_day()
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="B2":
            oreo()
            choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="B3":
           milk_bikis()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="C1":
           galaxy()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="C2":
           twix()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="C3":
           bounty()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="D1":
           coffee()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="D2":
           tea()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="D3":
           milk()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="E1":
           fanta()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="E2":
           pepsi()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="E3":
           water()
           choice=input("Would you like to continue? Type any key to continue or '0' to quit: ")
        elif code.upper()=="0":
           print ("\nTake your change AED",amount)
           print ("""\n▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█""")
           break
    
        else:
           print ("Invalid Code")

        if choice=="0":
           print ("\nTake your change AED", amount)
           print ("""\n▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █ █▀ █ ▀█▀ █ █▄░█ █▀▀
░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   ▀▄▀ █ ▄█ █ ░█░ █ █░▀█ █▄█""")
    break