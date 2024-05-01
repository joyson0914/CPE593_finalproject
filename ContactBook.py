import tkinter as tk
from tkinter import messagebox

# Simulated contact book (dictionary)
contact_book = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:  # Check if all fields are filled
        contact_book[name] = {'Phone': phone, 'Email': email}
        messagebox.showinfo("Success", "Contact added successfully!")
        # Clear entries after adding
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields must be filled out.")

def search_contact():
    name = search_entry.get()
    if name in contact_book:
        contact = contact_book[name]
        messagebox.showinfo("Search Result", f"Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        messagebox.showerror("Error", "Contact not found.")
    search_entry.delete(0, tk.END)

def update_contact():
    name = update_name_entry.get()
    new_phone = update_phone_entry.get()
    new_email = update_email_entry.get()
    if name in contact_book and (new_phone or new_email):
        if new_phone:
            contact_book[name]['Phone'] = new_phone
        if new_email:
            contact_book[name]['Email'] = new_email
        messagebox.showinfo("Success", "Contact updated successfully!")
        # Clear entries after updating
        update_name_entry.delete(0, tk.END)
        update_phone_entry.delete(0, tk.END)
        update_email_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Contact does not exist or no new information provided.")

def delete_contact():
    name = delete_entry.get()
    if name in contact_book:
        del contact_book[name]
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact does not exist.")
    delete_entry.delete(0, tk.END)

def list_contacts():
    list_window = tk.Toplevel(app)
    list_window.title("List of Contacts")
    scrollbar = tk.Scrollbar(list_window)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    lb = tk.Listbox(list_window, width=50, height=20, yscrollcommand=scrollbar.set)
    for name, info in contact_book.items():
        lb.insert(tk.END, f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    lb.pack(side=tk.LEFT, fill=tk.BOTH)
    scrollbar.config(command=lb.yview)

app = tk.Tk()
app.title("Contact Management System")

# Grid layout for entries and buttons
tk.Label(app, text="Name").grid(row=0, column=0)
tk.Label(app, text="Phone").grid(row=1, column=0)
tk.Label(app, text="Email").grid(row=2, column=0)
name_entry = tk.Entry(app)
phone_entry = tk.Entry(app)
email_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)
phone_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
tk.Button(app, text="Add Contact", command=add_contact).grid(row=3, column=1)

tk.Label(app, text="Search by Name").grid(row=4, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=4, column=1)
tk.Button(app, text="Search", command=search_contact).grid(row=4, column=2)

tk.Label(app, text="Update Name").grid(row=5, column=0)
tk.Label(app, text="New Phone").grid(row=6, column=0)
tk.Label(app, text="New Email").grid(row=7, column=0)
update_name_entry = tk.Entry(app)
update_phone_entry = tk.Entry(app)
update_email_entry = tk.Entry(app)
update_name_entry.grid(row=5, column=1)
update_phone_entry.grid(row=6, column=1)
update_email_entry.grid(row=7, column=1)
tk.Button(app, text="Update Contact", command=update_contact).grid(row=8, column=1)

tk.Label(app, text="Delete by Name").grid(row=9, column=0)
delete_entry = tk.Entry(app)
delete_entry.grid(row=9, column=1)
tk.Button(app, text="Delete", command=delete_contact).grid(row=9, column=2)

tk.Button(app, text="List All Contacts", command=list_contacts).grid(row=10, column=1)

app.mainloop()
