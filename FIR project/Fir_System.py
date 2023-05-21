
from tkinter import *
from tkinter.ttk import *   #used for latest graphics
from tkinter.messagebox import *

from complaintListing import ComplaintListing
from configdb import ConnectionDatabase
#Config
# So first of all we have to design the main screen.
# This display screen have a label of firstname, lastname, gender and Complaint,
# The radio buttons have only two male and female and for the buttons it is view complaint and submit now.
# So let’s see the way to put into effect this.

conn = ConnectionDatabase() # We connected a Database.
root = Tk()
root.geometry('550x350')
root.title('Online Fir System')
root.configure(bg='pink')

# Style

style = Style()
style.theme_use('classic')
for styles in ['TLabel', 'TButton', 'TRadioButton']:
    style.configure(styles, bg='blue')

labels = ['First Name:', 'Last Name:', 'Address:', 'Gender:', 'Comment:']
for i in range(5):
    Label(root, text=labels[i]).grid(row=i, column=0, padx=10, pady=10)

ButtonList = Button(root, text='View Complaint')
ButtonList.grid(row=5, column=1)

ButtonSubmit = Button(root, text='Submit Now')
ButtonSubmit.grid(row=5, column=2)

ButtonClose = Button(root, text='Close',command=root.destroy)
ButtonClose.grid(row=5, column=3)

# Entries
firstname = Entry(root, width=40, font=('Times New Roman', 14))
firstname.grid(row=0, column=1, columnspan=2)

lastname = Entry(root, width=40, font=('Times New Roman', 14))
lastname.grid(row=1, column=1, columnspan=2)

address = Entry(root, width=40, font=('Times New Roman', 14))
address.grid(row=2, column=1, columnspan=2)

GenderGroup = StringVar()
Radiobutton(root, text='Male', value='male', variable=GenderGroup).grid(row=3, column=1)
Radiobutton(root, text='Female', value='female', variable=GenderGroup).grid(row=3, column=2)


Comment = Text(root, width=40, height=5, font=('Times New Roman', 14))
Comment.grid(row=4, column=1, columnspan=2, padx=10, pady=10)

def SaveData():
    message = conn.Add(firstname.get(), lastname.get(), address.get(), GenderGroup.get(), Comment.get(1.0, 'end'))
    firstname.delete(0,'end')
    lastname.delete(0, 'end')
    address.delete(0, 'end')
    Comment.delete(1.0, 'end')
    showinfo(title='Add Information', message=message)

def ShowComplaintList():

    listrequest = ComplaintListing()


ButtonSubmit.config(command=SaveData)
ButtonList.config(command=ShowComplaintList)

root.mainloop()