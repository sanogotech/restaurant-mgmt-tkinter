from tkinter import *  #tkinter is used for making gui apps in python
import random #random package is used similarly as the randomize function in c
import time #time package is used for accessing time values to display
from PIL import ImageTk, Image

root = Tk() #iniitalizing window component
root.geometry("1600x800") #dimensions
root.title("Restau Gestion : RestauGEST") #title bar

Tops = Frame(root, width=400,relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=400, height=350, relief=SUNKEN)
f1.pack(side=LEFT)

#time display
localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font=('helvetica', 25, 'bold'), text="GARBA CHOCO RESTAURANT", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0) #app label

lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0) #time label

lblInfo2 = Label(Tops, font=('arial', 20, 'bold'), text='', fg="Red", bd=10, anchor='w')
lblInfo2.grid(row=2, column=0) #error label only shown when error is generated



def Ref(): #function used for calculation of bill
    global randomRef, CoFries, CostofFries, CoNoodles, CostofNoodles, CoSoup, CostofSoup, CoGarba, CostGarba
    global CoSandwich, CostSandwich, CoD, CostofDrinks, TotalCost, Ser_Charge, PayTax, TotalCost, AllCost
    #global declaration of variables allows us to access them in other blocks of code

    #reference no. generation
    """
    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)
    """

    try: #try block
        if (Fries.get() == ""):  #if user doesnt enter a quantity of fooditem it will be attained a value of 0
            CoFries = 0
        else:
            CoFries = float(Fries.get()) #else it attains the provided value

        if (Noodles.get() == ""):
            CoNoodles = 0
        else:
            CoNoodles = float(Noodles.get())

        if (Soup.get() == ""):
            CoSoup = 0
        else:
            CoSoup = float(Soup.get())

        if (Garba.get() == ""):
            CoGarba = 0
        else:
            CoGarba = float(Garba.get())

        if (Sandwich.get() == ""):
            CoSandwich = 0
        else:
            CoSandwich = float(Sandwich.get())

        if (Drinks.get() == ""):
            CoD = 0
        else:
            CoD = float(Drinks.get())

    except ValueError: #the except[read catch in languages] for cactching value error occured
        lblInfo2.config(text="Invalid values, please re-enter")

    CostofFries = CoFries * 2000 #calculation of costs of food items and other calculations based on it
    CostofDrinks = CoD * 500
    CostofNoodles = CoNoodles * 1500
    CostofSoup = CoSoup * 1000
    CostGarba = CoGarba * 2000
    CostSandwich = CoSandwich * 1000

    CostofMeal = "CFA", str(
        '%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostGarba + CostSandwich))



    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostGarba + CostSandwich)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostGarba + CostSandwich) * 0.09)

    TVA = "CFA", str('%.2f' % Ser_Charge)


    OverAllCost = "CFA", str('%.2f' % (Ser_Charge + TotalCost))

    
    AllCost = TotalCost + Ser_Charge

    TVA_Charge.set(TVA) #attaining values to suitable labels
    Cost.set(CostofMeal)

    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)

def saveData(): #function using file handling to write data of bill generated by applicaiton in a text file
    with open("CFAtmgt.txt", "a") as f:
        f.write('\nBill reference number = ' + rand.get())
        f.write('\nFries * %.2f = CFA %.2f' %(CoFries,CostofFries))
        f.write('\nNoodles * %.2f = CFA %.2f' %(CoNoodles,CostofNoodles))
        f.write('\nSoup * %.2f = CFA %.2f' %(CoSoup,CostofSoup))
        f.write('\nGarba * %.2f = CFA %.2f' %(CoGarba,CostGarba))
        f.write('\nSandwich * %.2f = CFA %.2f' %(CoSandwich,CostSandwich))
        f.write('\nDrinks * %.2f = CFA %.2f' %(CoD,CostofDrinks))
        f.write('\nCost of Meal = CFA %.2f' %TotalCost)
        f.write('\nTVA = CFA %.2f' %Ser_Charge)
        f.write('\nSub Total = CFA %.2f' %TotalCost)
        f.write('\nTotal Cost = CFA %.2f' %AllCost)
        f.write('\n')

def checkData(): #function using file handling to read data of bill text file
    with open("CFAtmgt.txt", "r") as f:
        print(f.read())


def qExit(): #function for exiting app
    root.destroy()


def Reset(): #function for clearing entries{textboxes}
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    TVA_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Garba.set("")
    Sandwich.set("")
    lblInfo2.config(text='')


#info left
rand = StringVar()
#reference no. generation
x = random.randint(10908, 500876)
rand.set(x)
#print(" random ", rand.get())
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
SubTotal = StringVar()
Total = StringVar()
TVA_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
Garba = StringVar()
Sandwich = StringVar()

lblReference = Label(f1, font=('arial', 16, 'bold'), text="Reference", bd=16, anchor="w")
lblReference.grid(row=0, column=0)
txtReference = Entry(f1, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtReference.insert(0, rand)
txtReference.grid(row=0, column=1)

lblFries = Label(f1, font=('arial', 16, 'bold'), text="Frites", bd=16, anchor="w")
lblFries.grid(row=1, column=0)
txtFries = Entry(f1, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="powder blue",
                 justify='right')
txtFries.grid(row=1, column=1)

lblNoodles = Label(f1, font=('arial', 16, 'bold'), text="Nouilles", bd=16, anchor="w")
lblNoodles.grid(row=2, column=0)
txtNoodles = Entry(f1, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtNoodles.grid(row=2, column=1)

lblSoup = Label(f1, font=('arial', 16, 'bold'), text="Soupe", bd=16, anchor="w")
lblSoup.grid(row=3, column=0)
txtSoup = Entry(f1, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtSoup.grid(row=3, column=1)

lblGarba = Label(f1, font=('arial', 16, 'bold'), text="Garba", bd=16, anchor="w")
lblGarba.grid(row=4, column=0)
txtGarba = Entry(f1, font=('arial', 16, 'bold'), textvariable=Garba, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtGarba.grid(row=4, column=1)

lblSandwich = Label(f1, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
lblSandwich.grid(row=5, column=0)
txtSandwich = Entry(f1, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSandwich.grid(row=5, column=1)


#info right
lblDrinks = Label(f1, font=('arial', 16, 'bold'), text="Boissons", bd=16, anchor="w")
lblDrinks.grid(row=0, column=2)
txtDrinks = Entry(f1, font=('arial', 16, 'bold'), textvariable=Drinks, bd=10, insertwidth=4, bg="powder blue",
                  justify='right')
txtDrinks.grid(row=0, column=3)

### Total  Action -------------------------
lblCost = Label(f1, font=('arial', 16, 'bold'), text="Montant du Repas HT", bd=16, anchor="w")
lblCost.grid(row=1, column=2)
txtCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="powder blue",
                justify='right')
txtCost.grid(row=1, column=3)
txtCost.configure(state='disabled')

lblTVA = Label(f1, font=('arial', 16, 'bold'), text="TVA", bd=16, anchor="w")
lblTVA.grid(row=2, column=2)
txtTVA = Entry(f1, font=('arial', 16, 'bold'), textvariable=TVA_Charge, bd=10, insertwidth=4, bg="powder blue",
                   justify='right')
txtTVA.grid(row=2, column=3)
txtTVA.configure(state='disabled')


lblSubTotal = Label(f1, font=('arial', 16, 'bold'), text="Sous - Total", bd=16, anchor="w")
lblSubTotal.grid(row=4, column=2)
txtSubTotal = Entry(f1, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="powder blue",
                    justify='right')
txtSubTotal.grid(row=4, column=3)
txtSubTotal.configure(state='disabled')

lblTotalCost = Label(f1, font=('arial', 16, 'bold'), text="Total ", bd=16, anchor="w")
lblTotalCost.grid(row=5, column=2)
txtTotalCost = Entry(f1, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="powder blue",
                     justify='right')
txtTotalCost.grid(row=5, column=3)
txtTotalCost.configure(state='disabled')

# Image

# Creating a photoimage object to use image 
#photo = PhotoImage(file = "sample.png") 
imgphoto = ImageTk.PhotoImage(Image.open("chocogarba.jpg"))  # PIL solution
  
# Resizing image to fit on button 
#photoimage = imgphoto.subsample(3, 3) 
  
# here, image option is used to 
# set image on button 
# compound option is used to align 
# image on LEFT side of button 
btnImage = Button(f1, image = imgphoto,width=150, height=150).grid(row=10, column=2)

# buttons
btnTotal = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 12, 'bold'), width=10, text="1. Total",
                  bg="grey", command=Ref).grid(row=7, column=1)

btnSave = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 12, 'bold'), width=10, text="2. Enregister",
                  bg="green", command=saveData).grid(row=7, column=2)

btnHistory = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 12, 'bold'), width=10, text="3. Historique",
                  bg="blue", command=checkData).grid(row=7, column=3)

btnReset = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 12, 'bold'), width=10, text="4. Réinitiatiser",
                  bg="orange", command=Reset).grid(row=7, column=4)

btnExit = Button(f1, padx=8, pady=8, bd=16, fg="black", font=('arial', 12, 'bold'), width=10, text="5. Quitter",
                 bg="red", command=qExit).grid(row=7, column=5)

root.mainloop()


