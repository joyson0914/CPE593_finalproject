import tkinter as tk
from tkinter import messagebox, ttk

# Define the Node class
class Node:
    def __init__(self, first_name, last_name, phone, email, next=None):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.next = next

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_contact(self, first_name, last_name, phone, email):
        new_node = Node(first_name, last_name, phone, email, self.head)
        self.head = new_node

    def find_contacts(self, first_name='', last_name=''):
        results = []
        current = self.head
        while current:
            if (first_name and current.first_name == first_name) or (last_name and current.last_name == last_name):
                results.append(current)
            current = current.next
        return results

    def delete_contact(self, contact):
        current = self.head
        previous = None
        while current:
            if current == contact:
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
            contacts.append(current)
            current = current.next
        return contacts

# Data structures initialized at the global level
favorites_array = []  # Corrected initialization
contacts_list = LinkedList()  # This is the correct initialization

def add_contact(first_name_entry, last_name_entry, phone_entry, email_entry, favorite_var, favorites_lb):
    first_name, last_name, phone, email = first_name_entry.get(), last_name_entry.get(), phone_entry.get(), email_entry.get()
    if all([first_name, last_name, phone, email]):
        contacts_list.add_contact(first_name, last_name, phone, email)
        if favorite_var.get() == 1:
            # Ensure not to add duplicates or unnecessary entries
            new_favorite = {'First Name': first_name, 'Last Name': last_name, 'Phone': phone, 'Email': email}
            if new_favorite not in favorites_array:
                favorites_array.append(new_favorite)
        refresh_favorites_display(favorites_lb)
        messagebox.showinfo("Success", "Contact added successfully!")
        for entry in (first_name_entry, last_name_entry, phone_entry, email_entry):
            entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "All fields must be filled out.")

def search_contact(first_name_entry, last_name_entry, results_display):
    first_name, last_name = first_name_entry.get(), last_name_entry.get()
    results = contacts_list.find_contacts(first_name=first_name.strip(), last_name=last_name.strip())
    if results:
        display_contacts(results, "Search Results", results_display)
    else:
        messagebox.showerror("Error", "No contacts found with that name.")
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)

def delete_selected_contact(all_contacts_lb, contacts, favorites_lb):
    selection = all_contacts_lb.curselection()
    if selection:
        index = selection[0]
        contact_to_delete = contacts[index]
        if contact_to_delete:
            success = contacts_list.delete_contact(contact_to_delete)
            if success:
                all_contacts_lb.delete(index)  # Remove from listbox
                update_favorites_on_deletion(contact_to_delete, favorites_lb)
                messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                messagebox.showerror("Error", "Failed to delete contact.")
    else:
        messagebox.showerror("Error", "No contact selected for deletion.")

def update_favorites_on_deletion(contact_to_delete, favorites_lb):
    global favorites_array
    print("Deleting Contact:", contact_to_delete.first_name, contact_to_delete.last_name)  # Debug which contact is being deleted
    # Create a temporary copy to debug and see what's being removed
    temp_favorites = favorites_array[:]
    # Filter out the deleted contact more specifically by comparing all fields
    favorites_array = [fav for fav in temp_favorites if fav and not (
        fav['First Name'] == contact_to_delete.first_name and
        fav['Last Name'] == contact_to_delete.last_name and
        fav['Phone'] == contact_to_delete.phone and
        fav['Email'] == contact_to_delete.email
    )]
    print("Favorites after deletion:", favorites_array)  # Check what remains in the favorites list after deletion
    refresh_favorites_display(favorites_lb)

def refresh_favorites_display(favorites_lb):
    print("Current Favorites:", favorites_array)  # Debugging line to check the state of favorites_array
    favorites_lb.delete(0, tk.END)  # Clear existing entries
    for favorite in favorites_array:
        if favorite:  # Ensure that the favorite item is not None before adding
            display_text = f"{favorite['First Name']} {favorite['Last Name']} - {favorite['Phone']} - {favorite['Email']}"
            favorites_lb.insert(tk.END, display_text)

def display_contacts(contacts, title, favorites_lb, deletion=False):
    list_window = tk.Toplevel(app)
    list_window.title(title)

    notebook = ttk.Notebook(list_window)
    all_contacts_frame = ttk.Frame(notebook)
    favorites_frame = ttk.Frame(notebook)
    notebook.add(all_contacts_frame, text='All Contacts')
    notebook.add(favorites_frame, text='Favorites')
    notebook.pack(expand=True, fill='both')

    all_contacts_lb = tk.Listbox(all_contacts_frame, width=50, height=10)
    all_contacts_lb.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    for contact in contacts:
        all_contacts_lb.insert(tk.END, f"{contact.first_name} {contact.last_name} - {contact.phone} - {contact.email}")

    favorites_lb = tk.Listbox(favorites_frame, width=50, height=10)
    favorites_lb.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    refresh_favorites_display(favorites_lb)

    if deletion:
        delete_button = tk.Button(list_window, text="Delete Selected Contact", command=lambda: delete_selected_contact(all_contacts_lb, contacts, favorites_lb))
        delete_button.pack()

def setup_gui():
    global app
    app = tk.Tk()
    app.title("Contact Management System")

    # GUI Elements
    tk.Label(app, text="First Name").grid(row=0, column=0)
    first_name_entry = tk.Entry(app)
    first_name_entry.grid(row=0, column=1)

    tk.Label(app, text="Last Name").grid(row=1, column=0)
    last_name_entry = tk.Entry(app)
    last_name_entry.grid(row=1, column=1)

    tk.Label(app, text="Phone").grid(row=2, column=0)
    phone_entry = tk.Entry(app)
    phone_entry.grid(row=2, column=1)

    tk.Label(app, text="Email").grid(row=3, column=0)
    email_entry = tk.Entry(app)
    email_entry.grid(row=3, column=1)

    favorite_var = tk.IntVar()
    tk.Checkbutton(app, text="Mark as Favorite", variable=favorite_var).grid(row=4, column=1)

    # Favorites listbox initialization for global access
    favorites_lb = tk.Listbox(app, width=50, height=10)
    favorites_lb.grid(row=10, columnspan=2)

    tk.Button(app, text="Add Contact", command=lambda: add_contact(first_name_entry, last_name_entry, phone_entry, email_entry, favorite_var, favorites_lb)).grid(row=5, column=1)
    tk.Button(app, text="Search by Name", command=lambda: search_contact(first_name_entry, last_name_entry, favorites_lb)).grid(row=6, column=1)
    tk.Button(app, text="List All Contacts", command=lambda: display_contacts(contacts_list.list_contacts(), "All Contacts", favorites_lb)).grid(row=8, column=1)
    tk.Button(app, text="Delete Contact", command=lambda: display_contacts(contacts_list.list_contacts(), "Select Contact to Delete", favorites_lb, deletion=True)).grid(row=9, column=1)

    return app

if __name__ == "__main__":
    app = setup_gui()
    app.mainloop()
