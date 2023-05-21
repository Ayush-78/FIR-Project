from tkinter import*
import tkinter
from tkinter.messagebox import* 
# Creating the window
root = Tk()
root.geometry('500x500')
root.title("Sign up page")

def homepage():
    root.destroy()
    import homepage

# message box function
def Confirmation():
    if entry_1.get() == '' or entry_2.get() == '' or entry_4.get() == '' or entry_5.get() == '' or entry_6.get() == '':
        tkinter.messagebox.showwarning("LOGIN FAILED", "        PLEASE TRY AGAIN        ")
    else:
        tkinter.messagebox.showinfo('Sign-up','Sign-up succesfull.  Now restart the application to login.')
    
# For heading
label_0 = Label(root, text="Fill your details",width=20,font=('bold', 20))
label_0.place(x=90,y=53)

#For name label
label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

#for name entry space
entry_1 = Entry(root)
entry_1.place(x=240,y=130)



#for email title
label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
#email entry space
entry_2 = Entry(root)
entry_2.place(x=240,y=180)

#for gender options using radio buttons
label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

# for age field
label_4 = Label(root, text="Age",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
entry_4 = Entry(root)
entry_4.place(x=240,y=280)

#For username label
label_5 = Label(root, text="Username",width=20,font=("bold", 10))
label_5.place(x=70,y=320)
#for username entry space
entry_5 = Entry(root)
entry_5.place(x=240,y=320)

#For username label
label_6 = Label(root, text="Password",width=20,font=("bold", 10))
label_6.place(x=70,y=360)
#for username entry space
entry_6 = Entry(root)
entry_6.place(x=240,y=360)

#for submit button
Button(root, text='Submit',width=20,bg='brown',fg='white',command=Confirmation).place(x=150,y=410)

#close button
Button(root, text='Close',width=20,bg='brown',fg='white',command=root.destroy).place(x=330,y=410)

#refresh page
Button(root, text='Refresh',width=20,bg='brown',fg='white',command=homepage).place(x=250,y=450)

# it is use for display the sign-up page form on the window
root.mainloop()