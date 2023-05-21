from tkinter import*

root = Tk()
root.geometry('500x500')
root.title('HomePage')
root.configure(bg='pink')

def signuppage():
    root.destroy()
    import signup
    
def loginpage():
    root.destroy()
    import login

label=Label(root,text='Welcome to Online Fir System',width=30,font=('bold',20),bg='pink')
label.place(x=20,y=50)

ButtonList = Button(root, text='Sign-up',width=20,command=signuppage)
ButtonList.place(x=180,y=120)

ButtonSubmit = Button(root, text='Login',width=20,command=loginpage)
ButtonSubmit.place(x=180,y=200)

ButtonSubmit = Button(root, text='close',width=20,command=root.destroy)
ButtonSubmit.place(x=180,y=280)


    

root.mainloop()