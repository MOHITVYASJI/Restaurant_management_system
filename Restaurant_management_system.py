#BREAKFAST
Indori_Poha = 18
Samosa      = 18
Upma        = 18
Jalebi      = 10
Imarti      = 15
Chai        = 12
Cofee       = 15

bill=0

def breakfast():
    print("\n")
    print("1. Indori Poha : 18₹/- plate")
    print("2. Samosa      : 18₹/- piece")
    print("3. Upma        : 18₹/- plate")
    print("4. Jalebi      : 10₹/- piece")
    print("5. Imarti      : 15₹/- piece")
    print("6. Chai        : 12₹/- cup  ")
    print("7. Cofee       : 15₹/- cup  ")

 
#LUNCH

def lunch():
    print("")


def bf_lu():
    brf_lun=int(input("Select 1 for Break Fast :\nSelect 2 for Lunch : \nSELECT => "))

    if brf_lun == 1:
        breakfast()
    elif brf_lun == 2:
        lunch()
    else:
        print("Sorry!! you select Wrong key")



#BREAK_FAST
def order_breakfast():
    bill=0
    breakfast_order=int(input("SELECT => "))
    print("\n")
    match breakfast_order:
        case 1:
            print("Thank you for Order! \nYour Order is Indore Poha")
            bill+=Indori_Poha
        case 2:
            print("Thank you for Order! \nYour Order is Samosa")
            bill+=Samosa
        case 3:
            print("Thank you for Order! \nYour Order is Upma")
            bill+=Upma
        case 4:
            print("Thank you for Order! \nYour Order is Jalebi")
            bill+=Jalebi
        case 5:
            print("Thank you for Order! \nYour Order is Imarti")
            bill+=Imarti
        case 6:
            print("Thank you for Order! \nYour Order is Chai")
            bill+=Chai
        case 7:
            print("Thank you for Order! \nYour Order is Cofee")
            bill+=Cofee
        case 8:
            print("Thank you for Order! \nYour Order is Indore Poha")
            bill+=Indori_Poha
        case 9:
            print("Thank you for Order! \nYour Order is Indore Poha")
            bill+=Indori_Poha

YES=True
yes=True

def order_control():
    print("\nAnd what does it mean to order something?")
    rep_order=bool(input("\nYES        NO  \nSELECT => "))

    if rep_order == True:
        bf_lu()
    elif rep_order == True:
        bf_lu()
    else:
        print("Your Bill is => ",bill," Rupee")



##Main Code

print('""""""""""""""""""""""""""""""""""')
print("WELLCOME TO GIRIRAJ RESTAURANT")
print('""""""""""""""""""""""""""""""""""')

bf_lu()
order_breakfast()
order_control()
order_breakfast()
order_control()

