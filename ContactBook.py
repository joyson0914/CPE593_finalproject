import tkinter as tk
from tkinter import messagebox, ttk

class Node:
    def __init__(self, name, phone, email, next=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, name, phone, email):
        new_node = Node(name, phone, email, self.head)
        self.head = new_node

    def find_contact(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def delete_contact(self, name):
        current = self.head
        previous = None
        while current:
            if current.name == name:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def list_contacts(self):
        contacts = []
        current = self.head
        while current:
            contacts.append((current.name, current.phone, current.email))
            current = current.next
        return contacts

# Data structures
contact_book = {}  # Hash table for fast lookup
contacts_list = LinkedList()  # Linked list to maintain order
favorites_array = [None] * 10  # Array for favorites

app = tk.Tk()
app.title("Contact Management System")

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    if name and phone and email:
        # Add to hash table for fast lookup
        contact_book[name] = {'Phone': phone, 'Email': email}
        # Add to linked list to maintain order
        contacts_list.add_contact(name, phone, email)
        # Check if marked as favorite and add to array if there is space
        if favorite_var.get() == 1:
            for i in range(len(favorites_array)):
                if favorites_array[i] is None:
                    favorites_array[i] = {'Name': name, 'Phone': phone, 'Email': email}
                    break
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields must be filled out.")

def search_contact():
    name = search_entry.get()
    # Directly use hash table for quick search
    contact = contact_book.get(name)
    if contact:
        messagebox.showinfo("Search Result", f"Name: {name}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    else:
        messagebox.showerror("Error", "Contact not found.")
    search_entry.delete(0, tk.END)

def delete_contact():
    name = delete_entry.get()
    # Delete from all data structures
    if name in contact_book:
        del contact_book[name]
        contacts_list.delete_contact(name)
        for i in range(len(favorites_array)):
            if favorites_array[i] and favorites_array[i]['Name'] == name:
                favorites_array[i] = None
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact does not exist.")
    delete_entry.delete(0, tk.END)

def list_contacts():
    list_window = tk.Toplevel(app)
    list_window.title("List of Contacts")

    notebook = ttk.Notebook(list_window)
    all_contacts_frame = ttk.Frame(notebook)
    favorites_frame = ttk.Frame(notebook)
    notebook.add(all_contacts_frame, text='All Contacts')
    notebook.add(favorites_frame, text='Favorites')
    notebook.pack(expand=True, fill='both')

    # All Contacts List
    all_contacts_scrollbar = tk.Scrollbar(all_contacts_frame)
    all_contacts_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    all_contacts_lb = tk.Listbox(all_contacts_frame, width=50, height=20, yscrollcommand=all_contacts_scrollbar.set)
    for name, phone, email in contacts_list.list_contacts():
        all_contacts_lb.insert(tk.END, f"Name: {name}, Phone: {phone}, Email: {email}")
    all_contacts_lb.pack(side=tk.LEFT, fill=tk.BOTH)
    all_contacts_scrollbar.config(command=all_contacts_lb.yview)

    # Favorites List
    favorites_scrollbar = tk.Scrollbar(favorites_frame)
    favorites_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    favorites_lb = tk.Listbox(favorites_frame, width=50, height=20, yscrollcommand=favorites_scrollbar.set)
    for contact in favorites_array:
        if contact:
            favorites_lb.insert(tk.END, f"Name: {contact['Name']}, Phone: {contact['Phone']}, Email: {contact['Email']}")
    favorites_lb.pack(side=tk.LEFT, fill=tk.BOTH)
    favorites_scrollbar.config(command=favorites_lb.yview)

# GUI Elements
tk.Label(app, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(app)
name_entry.grid(row=0, column=1)

tk.Label(app, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(app)
phone_entry.grid(row=1, column=1)

tk.Label(app, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(app)
email_entry.grid(row=2, column=1)

favorite_var = tk.IntVar()
tk.Checkbutton(app, text="Mark as Favorite", variable=favorite_var).grid(row=3, column=1)

tk.Button(app, text="Add Contact", command=add_contact).grid(row=4, column=1)

tk.Label(app, text="Search by Name").grid(row=5, column=0)
search_entry = tk.Entry(app)
search_entry.grid(row=5, column=1)
tk.Button(app, text="Search", command=search_contact).grid(row=5, column=2)

tk.Label(app, text="Delete by Name").grid(row=6, column=0)
delete_entry = tk.Entry(app)
delete_entry.grid(row=6, column=1)
tk.Button(app, text="Delete", command=delete_contact).grid(row=6, column=2)

tk.Button(app, text="List All Contacts", command=list_contacts).grid(row=7, column=1)

app.mainloop()
