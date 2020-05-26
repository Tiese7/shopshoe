cart = list()

def shop():
   print('\t\t\t\t||||||||||||||||||\n\t\t\t\t ไข่แมวx FEET SHOP\n\t\t\t\t||||||||||||||||||')
   print('NIKE       [1]\nADIDAS     [2]\nOFF-WHITE  [3]\nVans       [4]\nShow cart  [5]\nExit       [6]\n')
   choose = input('\nPlease select Menu : ')
   if   choose == '1' : N1()
   elif choose == '2' : A1()
   elif choose == '3' : O1()
   elif choose == '4' : V1()
   elif choose == '5' : payment()
   elif choose == '6' : print('\n\nThanks you very much! <3\n') ; exit()
   else : print('\nกดเลขให้ถูกด้วยครับ นะครับ นั่นแหล่ะครับ\n') , shop()

def N1():
    print('\n\t\t\t\t------\n\t\t\t\t NIKE\n\t\t\t\t------')
    print('NIKE Air Jodan 1 Retro High OFF-WHITE "Chicago" [1]\nNIKE Air max 270                                [2]\nNIKE React Element Kenny 55                     [3]')
    t = input('\nSelect model : ')
    if   t == '1' : N1Price(1)
    elif t == '2' : N1Price(2)
    elif t == '3' : N1Price(3)
    else : print('\nplease select model again') ; N1()

def N1Price(n):
    if n == 1 :
        print('NIKE Air Jodan 1 Retro High OFF-WHITE "Chicago" 5,800 Baht discount 20%\n')
        cart.append(['NIKE Air Jodan 1 \nRetro High OFF-WHITE "Chicago"','\t    5,800','  20%','  4640\n']) #appendคือเอาค่านี่ไปใส่ในlistที่เราสร้าง
        shop()
    elif n == 2 :
        print('NIKE Air Max 270 5,500 Baht discount 20%\n')
        cart.append(['NIKE Air Max 270','\t\t    5,500','\t  20%','   4400\n'])
        shop()
    elif n == 3 :
        print('NIKE React Element Kenny 55 5,500 Baht discount 20%\n')
        cart.append(['NIKE React Element Kenny 55','\t    5,500','  20%','  4400\n'])
        shop()
    else : print('Sorry this model was out of stock')

def A1():
    print('\n\t\t\t\t-------\n\t\t\t\t ADIDAS\n\t\t\t\t-------')
    print('ADIDAS Yeezy Boost 350 V2 Yecheil(Non-Reflexcive) [1]\nADIDAS Pharrell Williams Solar Hu NMD             [2]\nADIDAS Ultraboost 19 V2                           [3]')
    t = input('\nSelect model : ')
    if   t == '1' : A1Price(1)
    elif t == '2' : A1Price(2)
    elif t == '3' : A1Price(3)
    else : print('\nplease select model again') ; A1()

def A1Price(n):
    if n == 1 :
        print('ADIDAS Yeezy Boost 350 V2 Yecheil(Non-Reflective) 8,600 Baht discount 30%\n')
        cart.append(['ADIDAS Yeezy Boost 350 V2 \nYecheil(Non-Reflective)','\t\t    8,600','   30%','   6020\n'])
        shop()
    elif n == 2 :
        print('ADIDAS Pharrell Williams Solar Hu NMD 10,000 Baht discount 30%\n')
        cart.append(['ADIDAS Pharrell Williams \nSolar Hu NMD','\t\t\t    10,000','\t  30%','   7000\n'])
        shop()
    elif n == 3 :
        print('ADIDAS Ultraboost 19 V2 7,300 Baht discounnt 30%\n')
        cart.append(['ADIDAS Ultraboost 19 V2','\t    7,300','  30%','  5110\n'])
        shop()
    else : print('Sorry this model was out of stock')

def O1():
    print('\n\t\t\t\t-----------\n\t\t\t\t OFF-WHITE\n\t\t\t\t-----------')
    print('OFF-WHITE White Mid Top Sneaker   [1]\nOFF-WHITE Low Vulcanized Sneaker  [2]\nOFF-WHITE "OFF-COURT" 3.0 Sneaker [3]')
    t = input('\nSelect model : ')
    if   t == '1' : O1Price(1)
    elif t == '2' : O1Price(2)
    elif t == '3' : O1Price(3)
    else : print('\nplease selcet model again') ; O1()

def O1Price(n):
    if n == 1 :
        print('OFF-WHITE White Mid Top Sneaker 15,670 Baht discount 10%\n')
        cart.append(['OFF-WHITE White Mid Top Sneaker','  15,670','10%','14103\n'])
        shop()
    elif n == 2 :
        print('OFF-WHITE Low Vulcanized Sneaker 12,535 Baht discount 10%\n')
        cart.append(['OFFWHITE Low Vulcanized Sneaker','  12,535','10%','11282\n'])
        shop()
    elif n == 3 :
        print('OFF-WHITE "OFF-COURT" 3.0 Sneaker 23,505 Baht discount 10%\n')
        cart.append(['OFFWHITE "OFF-COURT" 3.0 \nSneaker','\t\t\t\t   23,505','\t  10%','   21155\n'])
        shop()
    else : print('Sorry this model was out of stock')

def V1():
    print('\n\t\t\t\t-----------\n\t\t\t\t   VANS\n\t\t\t\t-----------')
    print('VANS Old Skool\t\t\t   [1]\nVANS Classic Checkerboard Slip-On  [2]\nVANS SK8-HI Reissue Cap\t\t   [3]')
    t = input('\nSelect model : ')
    if   t == '1' : V1Price(1)
    elif t == '2' : V1Price(2)
    elif t == '3' : V1Price(3)
    else : print('\nplease selcet model again') ; V1()

def V1Price(n):
    if n == 1 :
        print('VANS Old Skool 2,400 Baht discount 40%\n')
        cart.append(['VANS Old Skool','\t             2,400','\t  40%','   1440\n'])
        shop()
    elif n == 2 :
        print('VANS Classic Checkerboard Slip-On 1,900 Baht discount 40%\n')
        cart.append(['VANSClassic CheckerboardSlip-On','   1,900','40%','1194\n'])
        shop()
    elif n == 3 :
        print('VANS SK8-HI Reissue Cap 3,500 Baht discount 40%\n')
        cart.append(['VANS SK8-HI Reissue Cap','\t     3,500','  40%','  2100\n'])
        shop() 
    else : print('Sorry this model was out of stock')
def payment():
    PP = 0 
    print('\n--------------------------------------------------------------------------------------')
    print('MODEL               \t\t OLD PRICE     DISCOUNT           PRICE')
    print('--------------------------------------------------------------------------------------')
    number = 0
    for o in cart:
        number += 1
        print(number,end=" ")
        for i in o:
            print(i.ljust(17),end = "")
        print()
    for o in range(len(cart)): PP = PP + int(cart[o][3])
    print('\n--------------------------------------------------------------------------------------')
    print("PRICE\t                                                           %d"%PP ," BAHT TOTAL")
    print('\n\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('\n\t\t\t   ถ้าเงินเหลือ เลือกรองเท้าต่อได้อีกนะครับ')
    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    print('\n')
    hee = input('[1]กลับหน้าหลัก [2]ออก\n')
    if hee == '1' :
        shop()
    elif hee == '2' :
        exit
shop()