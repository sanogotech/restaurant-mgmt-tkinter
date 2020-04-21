from tkinter import *
from tkinter import ttk,messagebox
from tkinter.ttk import Combobox,Progressbar

# Window
window = Tk()

def initGUI():
    
    window.title("Akwaba Abidjan Python")
    window.geometry('600x200')
    style = ttk.Style()
    style.theme_use('default')
    
    #Events functions
    def clicked():

        lbl.configure(text="Button was clicked !!")
    
    def clickedShowMessage(): 
        messagebox.showinfo('Pour Votre Santé', 'Manger 5 fruits et légumes par jour')
        #messagebox.showwarning('Message title', 'Message content')  #shows warning message
        #messagebox.showerror('Message title', 'Message content')    #shows error message
    
    def resetLabelMessage():
        res = messagebox.askyesnocancel('Reset Message ','Rest OK : are you sure ')
        """
        res = messagebox.askquestion('Message title','Message content')
        res = messagebox.askyesno('Message title','Message content')
        res = messagebox.askokcancel('Message title','Message content')
        res = messagebox.askretrycancel('Message title','Message content')
        """
        if(res==True):
            print("Reset OK")
            lbl.configure(text="Akwaba")
        elif(res==False):
            print("KO Reset")

    #Components
    #Add spacing for widgets (padding)
    lbl = Label(window, text="Hello",padx=10, pady=10)
    #
    txt1 = Entry(window,width=20)
    txt1.insert(0, "Geek Python !")
    txt2 = Entry(window,width=10, state='disabled')
    #
    btn = Button(window, text="Click Me", bg="orange", fg="red",command=clicked)
    btnMessage = Button(window, text="Show Me", bg="green", fg="white",command=clickedShowMessage)
    btnReset = Button(window, text="Reset", bg="red", fg="white",command=resetLabelMessage)
    #
    combo = Combobox(window)
    combo['values']= ("Marcory", "Koumassi", "Yopougon", "Abobo", "Cocody")
    combo.current(1) #set the selected item
    #
    bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
    bar['value'] = 70
    #
    rad1 = Radiobutton(window,text='First', value=1)
    rad2 = Radiobutton(window,text='Second', value=2)
    rad3 = Radiobutton(window,text='Third', value=3,command=clickedShowMessage)

    #
    chk_state = BooleanVar()
    chk_state.set(True) #set check state
    chk = Checkbutton(window, text='Choose', var=chk_state)
  

    # Grid Position
    lbl.grid(column=0, row=0)
    combo.grid(column=4, row=0)
    txt1.grid(column=1, row=0)
    
    rad1.grid(column=0, row=1)
    rad2.grid(column=1, row=1)
    rad3.grid(column=2, row=1)
    
    txt2.grid(column=1, row=2)
    chk.grid(column=0, row=3)
    bar.grid(column=2, row=3)

    btn.grid(column=1, row=5)
    btnMessage.grid(column=3, row=5) 
    btnReset.grid(column=2, row=5) 
    
# Main function
def main():
    initGUI()
    window.mainloop()

if __name__ == '__main__':
    main()
    
    
