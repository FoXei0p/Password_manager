from tkinter import *
from tkinter import messagebox
import random
import string
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.configure(bg='lightblue')

#logo
canvas = Canvas(height=400, width=450, bg='lightblue',highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(200, 200, image=logo_img, anchor=CENTER)
canvas.grid(row=0, column=0,columnspan=2, pady=10)

#Generate Password
def generate_password():

    lttr =  list(string.ascii_letters)
    num = list(string.digits)
    sym = ['!', '#', '$', '&', '-', '_']
    letters = [random.choice(lttr) for _ in range(7)]
    numbers = [random.choice(num) for _ in range(7)]
    symbols = [random.choice(sym) for _ in range(6)]
    password_list =(letters + numbers + symbols)
    random.shuffle(password_list)
    passs = [random.choice(password_list)for _ in range(slider.get())]
    random.shuffle(passs)
    password = "".join(passs)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


#Saves Everything
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



#Labels
website_label = Label(text="Website:", bg='lightblue')
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg='lightblue')
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", bg='lightblue')
password_label.grid(row=3, column=0)
random_pass_range = Label(text="characters in your password?", bg='lightblue')
random_pass_range.grid(row=4, column=0)

#Entries
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=37)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons/sliders
slider =Scale(window, from_=0, to=30, orient=HORIZONTAL , bg='lightblue',highlightthickness=0)
slider.set(15)
slider.grid(row=4, column=1 , pady=5)
generate_password_button = Button(text="Generate Password", width=30, command=generate_password)
generate_password_button.grid(row=5, column=1)
add_button = Button(text="Save", width=65, command=save,)
add_button.grid(row=6, column=0, columnspan=2, pady=10)

window.mainloop()