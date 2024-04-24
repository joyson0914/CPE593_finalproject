def add_contact(contact_book, name, phone_number):
    """Add a new contact to the hash table."""
    if name not in contact_book:
        contact_book[name] = phone_number
        print(f"Contact {name} added successfully.")
    else:
        print("Contact already exists.")

def update_contact(contact_book, name, new_phone_number):
    """Update an existing contact's phone number."""
    if name in contact_book:
        contact_book[name] = new_phone_number
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact does not exist.")

def main():
    contact_book = {}
    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("4. Update a contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the contact's name: ")
            phone_number = input("Enter the contact's phone number: ")
            add_contact(contact_book, name, phone_number)
        elif choice == '4':
            name = input("Enter the contact's name to update: ")
            new_phone_number = input("Enter the new phone number: ")
            update_contact(contact_book, name, new_phone_number)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
