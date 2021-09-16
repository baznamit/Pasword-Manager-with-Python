from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_pass():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(4, 6))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(1, 3))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(1, 3))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    entry_3.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    
    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="OOPS", message='Please dont leave any fields empty.')
    
    else:
        try: 
            with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
                    
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        
        else:
            #Updating old data with new data
            data.update(new_data)
    
            with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
                    
        finally:     
            entry_1.delete(0, END)
            entry_3.delete(0, END)
 
# ---------------------------- SEARCH ------------------------------- #   

def search():
    
    website = entry_1.get()
    
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="No Data file found.")
        
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
        
        else:
            messagebox.showinfo(title="error", message=f"No data found for {website}.")
            
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
label_1 = Label(text= "Website:", font=("Open Sans", 8, "normal"))
label_1.grid(column=0, row=1)

label_2 = Label(text="Email/Username:", font=("Open Sans",8, "normal"))
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:", font=("Open Sans", 8, "normal"))
label_3.grid(column=0, row=3)

#Entries
entry_1 = Entry(width=21)
entry_1.grid(column=1, row=1)
entry_1.focus()

entry_2 = Entry(width=39)
entry_2.grid(column=1, row=2, columnspan=2)
entry_2.insert(0, "namit.singh1269@gmail.com")

entry_3 = Entry(width=21)
entry_3.grid(column=1, row=3)

#Buttons
button_search = Button(text="Search", font=("Open Sans", 8, "normal"), width=16, command=search)
button_search.grid(column=2, row=1)

button_pass = Button(text="Generate Password", font=("Open Sans", 8, "normal"), command=generate_pass)
button_pass.grid(column=2, row=3)

button_add = Button(text="Add", width=36, font=("Open Sans", 8, "normal"), command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()