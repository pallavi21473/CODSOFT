import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu options."""
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("-------------------------")

def add_contact(contacts):
    """Adds a new contact to the list."""
    clear_screen()
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email (optional): ")
    address = input("Enter Address (optional): ")

    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(contact)
    print("\nContact added successfully!")

def view_contact_list(contacts):
    """Displays a list of all saved contacts."""
    clear_screen()
    print("\n--- Contact List ---")
    if not contacts:
        print("Your contact list is empty!")
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("--------------------")

def search_contact(contacts):
    """Searches for contacts by name or phone number."""
    clear_screen()
    print("\n--- Search Contact ---")
    if not contacts:
        print("Your contact list is empty. Cannot search.")
        return

    search_term = input("Enter name or phone number to search: ").lower()
    found_contacts = []

    for contact in contacts:
        if search_term in contact['name'].lower() or search_term in contact['phone'].lower():
            found_contacts.append(contact)

    if not found_contacts:
        print("\nNo contacts found matching your search.")
    else:
        print("\n--- Search Results ---")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            if contact['email']:
                print(f"Email: {contact['email']}")
            if contact['address']:
                print(f"Address: {contact['address']}")
            print("-" * 20) # Separator for each contact

def update_contact(contacts):
    """Updates details of an existing contact."""
    clear_screen()
    print("\n--- Update Contact ---")
    view_contact_list(contacts)
    if not contacts:
        return

    while True:
        try:
            contact_index = int(input("Enter the number of the contact to update: ")) - 1
            if 0 <= contact_index < len(contacts):
                break
            else:
                print("Invalid contact number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    contact = contacts[contact_index]

    print(f"\nUpdating contact: {contact['name']}")

    new_name = input(f"Enter new Name (current: {contact['name']}, leave blank to keep): ")
    if new_name:
        contact['name'] = new_name

    new_phone = input(f"Enter new Phone Number (current: {contact['phone']}, leave blank to keep): ")
    if new_phone:
        contact['phone'] = new_phone

    new_email = input(f"Enter new Email (current: {contact['email']}, leave blank to keep): ")
    contact['email'] = new_email # Allow clearing email

    new_address = input(f"Enter new Address (current: {contact['address']}, leave blank to keep): ")
    contact['address'] = new_address # Allow clearing address

    print("\nContact updated successfully!")

def delete_contact(contacts):
    """Deletes a contact from the list."""
    clear_screen()
    print("\n--- Delete Contact ---")
    view_contact_list(contacts)
    if not contacts:
        return

    while True:
        try:
            contact_index = int(input("Enter the number of the contact to delete: ")) - 1
            if 0 <= contact_index < len(contacts):
                break
            else:
                print("Invalid contact number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    deleted_contact = contacts.pop(contact_index)
    print(f"\nContact '{deleted_contact['name']}' deleted successfully!")

def main():
    """Main function to run the Contact Book application."""
    contacts = [] # List to store contact dictionaries

    while True:
        clear_screen() # Clear screen before showing menu
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contact_list(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...") # Pause for user to read output

if __name__ == "__main__":
    main()