from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

ALL_CHARACTERS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
    'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'",
    '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
    '^', '_', '`', '{', '|', '}', '~'
]


# GENERATE A RANDOM PASSWORD
def random_password():
    password_input.delete(0, END)
    new_password = ''.join([ALL_CHARACTERS[random.randint(0, len(ALL_CHARACTERS) - 1)] for _ in range(20)])
    password_input.insert(0, new_password)


# SAVE THE CURRENT PASSWORD IN A .JSON FILE
def save_password():
    website_name = website_input.get().capitalize()
    user_email = username_input.get()
    user_password = password_input.get()
    new_data = {website_name: {
        'email': user_email,
        'password': user_password
    }
    }
    if password_input.get() == '' or website_input.get() == '':
        messagebox.showerror(title='Oops', message='Please fill all the inputs')
    else:
        try:
            with open('passwords.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('passwords.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('passwords.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            password_input.delete(0, END)
            website_input.delete(0, END)
            pyperclip.copy(password_input.get())
            messagebox.showinfo(title='Success!', message='Password saved')


# SEARCHES FOR A GIVEN SITE IN THE .JSON FILE
def search_password():
    website_name = website_input.get().capitalize()
    try:
        with open('passwords.json') as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=website_name, message=f"Email: {data[website_name]['email']}\nPassword: "
                                                            f"{data[website_name]['password']}")
    except KeyError:
        messagebox.showerror(title='Oops', message="There's not a saved password for this website")
    except FileNotFoundError:
        messagebox.showerror(title='Oops', message='No data file found')


# UI SETUP
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=189, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website')
website_label.grid(column=0, row=1)

username_label = Label(text='Email/Username')
username_label.grid(column=0, row=2)

password_label = Label(text='Password')
password_label.grid(column=0, row=3)

# Entries
website_input = Entry()
website_input.focus()
website_input.grid(column=1, row=1, sticky='nesw')

username_input = Entry()
username_input.insert(0, 'henriquewelbe@gmail.com')
username_input.grid(column=1, row=2, columnspan=2, sticky='nesw')

password_input = Entry()
password_input.grid(column=1, row=3, sticky='nesw')

# GET THE VALUE FROM THE ENTRIES


# Buttons
search = Button(text='Search', command=search_password)
search.grid(column=2, row=1, sticky='nesw')

generate_password = Button(text='Generate Password', command=random_password)
generate_password.grid(column=2, row=3)

add_password = Button(text='Add', command=save_password)
add_password.grid(column=1, row=4, columnspan=2, sticky='nesw')

window.mainloop()
