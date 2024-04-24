def search_contact(contact_book, name):
    """Search for a contact by name."""
    try:
        print(f"Contact: {name}, Phone Number: {contact_book[name]}")
    except KeyError:
        print("Contact not found.")

def delete_contact(contact_book, name):
    """Delete a contact from the hash table."""
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} removed successfully.")
    else:
        print("Contact does not exist.")

def main():
    contact_book = {}
    while True:
        print("\nContact Management System")
        print("2. Search for a contact")
        print("3. Delete a contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '2':
            name = input("Enter the contact's name to search: ")
            search_contact(contact_book, name)
        elif choice == '3':
            name = input("Enter the contact's name to delete: ")
            delete_contact(contact_book, name)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
