from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json







# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
        "email" : email,
        "password" : password,
    }
    }

    if len(website)==0 or len(password)==0:
        is_warning =messagebox.showinfo(title="Warning",message =f"Please don't leave any fields empty XD" )
    else:
        is_ok = messagebox.askokcancel(title=website , message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\nIs it okay to save?")
        if is_ok:
             with open("data.json","w") as data_file:
                json.dump(new_data , data_file,indent=4)
                website_entry.delete(0, END)
                password_entry.delete(0, END)






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas= Canvas(width= 200,height = 200)
password_img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image= password_img)

canvas.grid(column=0, row=0, columnspan=3)

# labels
website = Label(text="Website :")
website.grid(row=1, column=0)

email = Label(text="Email/username :")
email.grid(row=2, column=0)

password = Label(text="Password :")
password.grid(row=3, column=0)

# entry
website_entry = Entry(width=45)
website_entry.grid(row=1, column=1,columnspan=2,sticky="ew",padx=5,pady=3) # added padx and pady
website_entry.focus()

email_entry = Entry(width=45)
email_entry.grid(row=2, column=1,columnspan=2,sticky="ew",padx=5,pady=3) # added padx and pady
email_entry.insert(0, "ghoshpriyasha29@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1,sticky="ew",padx=5,pady=3) # added padx and pady


#buttons
generate_password = Button(text="Generate Password",command=generate_password)
generate_password.grid(row=3, column=2,sticky="ew",padx=5,pady=3) # added padx and pady

add_button = Button(text="Add",width=40,command=save)
add_button.grid(row=4, column=1,columnspan=2,sticky="ew",padx=5,pady=3) # added padx and pady
window.mainloop()
