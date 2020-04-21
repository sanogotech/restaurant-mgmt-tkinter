from tkinter import *
from tkinter import ttk,messagebox

window = Tk()

def initGUI():
      
    window.title("Akwaba Abidjan Python")
    window.geometry('600x200')
    style = ttk.Style()
    style.theme_use('default')

    def clickedShowMessage(): 
        messagebox.showinfo('Pour Votre Santé', 'Manger 5 fruits et légumes par jour')
        #messagebox.showwarning('Message title', 'Message content')  #shows warning message
        #messagebox.showerror('Message title', 'Message content')    #shows error message
    
    # Menu
    menu = Menu(window)
    # First list Items
    new_item1 = Menu(menu)
    new_item1.add_command(label='New')
    new_item1.add_separator()
    new_item1.add_command(label='Edit')
    #
    menu.add_cascade(label='File', menu=new_item1)
    menu.add_cascade(label='Tools')
    menu.add_cascade(label='Help')
    #
    window.config(menu=menu)

    # TABs
    tab_control = ttk.Notebook(window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Gestion Client')
    tab_control.add(tab2, text='Comptabilité')

  

    #Tab1
    #
    lbl1 = Label(tab1, text= 'VIP Client')
    lbl1.grid(column=0, row=0)
    txt1 = Entry(tab1,width=20)
    txt1.insert(0, "Geek Python !")
    txt2 = Entry(tab1,width=10, state='disabled')
    #
    btn = Button(tab1, text="Click Me", bg="orange", fg="red")
    btnMessage = Button(tab1, text="Show Me", bg="green", fg="white",command=clickedShowMessage)
    btnReset = Button(tab1, text="Reset", bg="red", fg="white")
    
    #Tab2
    lbl2 = Label(tab2, text= 'Chiffre Affaire')
    lbl2.grid(column=0, row=0)
    
    # Grid  Tabs Position
    txt1.grid(column=1, row=0)
    txt2.grid(column=1, row=2)
    btn.grid(column=1, row=5)
    btnMessage.grid(column=5, row=5) 
    btnReset.grid(column=3, row=5)
    
    def addFrame():
        # frame 1
        frame1 = Frame(window, borderwidth=2, relief=GROOVE)
        frame1.pack(side=LEFT, padx=30, pady=30)

        
        # frame 2
        frame2 = Frame(tab2, borderwidth=2, relief=GROOVE)

        # Ajout de labels
        Label(frame1, text="Frame 1",bg="red").pack(padx=10, pady=10)
        Label(frame2, text="Frame 2",bg="yellow").pack(padx=10, pady=10)
        
        #Position
        frame2.grid(column=3, row=5)
        
    
    ## call function
    addFrame()
    tab_control.pack(expand=1, fill='both')

def main():
    initGUI()
    window.mainloop()

if __name__ == '__main__':
    main()
    