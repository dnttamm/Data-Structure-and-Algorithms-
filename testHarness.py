#
# DSAContactMenu.py
# 

from DSAContact import DSAContact
from DSAContactHashTable import read_contacts

#Print the menu options
def print_menu():
    print("\nContact List Management System Menu:")
    print("1. View contacts list")
    print("2. Add new contact")
    print("3. Delete contact")
    print("4. Update contact")
    print("5. Search contacts")
    print("6. Sort contact list")
    print("7. Display contacts belonging to a particular group")
    print("8. Exit")


def main():
    # Create a contact table and populate it with contacts from the file 'contact_list.txt'
    contact_table = read_contacts('contact_list.txt')

    # Run the system in a loop until the user chooses to exit
    while True:
        # Print the menu options
        print_menu()
        # Prompt the user to enter their choice
        choice = input("Enter your choice (1-8): ")
        
        # Based on the user's choice, execute the corresponding functionality
        if choice == '1':
            print("\nContacts List:")
            # Display the contacts list
            contact_table.display_contacts()
        elif choice == '2':
            # Add a new contact
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            group = input("Enter group (F, W, or FR): ")
            contact = DSAContact(name, phone_number, email, group)
            contact_table.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '3':
            # Delete a contact
            phone_number = input("Enter phone number of contact to delete: ")
            contact_table.delete_contact(phone_number)
        elif choice == '4':
            # Update a contact
            phone_number = input("Enter phone number of contact to update: ")
            updated_name = input("Enter updated name: ")
            updated_email = input("Enter updated email: ")
            updated_group = input("Enter updated group (F, W, or FR): ")
            updated_contact = DSAContact(updated_name, phone_number, updated_email, updated_group)
            contact_table.update_contact(phone_number, updated_contact)
        elif choice == '5':
            # Search for contacts
            search_term = input("Enter search term (name or phone number): ")
            contact_table.search_contacts(search_term)
        elif choice == '6':
            # Sort the contacts list by name
            sorted_contacts = contact_table.sort_contacts_by_name()
            print("\nSorted Contacts List:")
            for contact in sorted_contacts:
                print(contact)
        elif choice == '7':
            # Display contacts belonging to a particular group
            group = input("Enter group to display (F, W, or FR): ")
            filtered_contacts = contact_table.filter_contacts_by_group(group)
            print(f"\nContacts belonging to group '{group}':")
            for contact in filtered_contacts:
                print(contact)
        elif choice == '8':
            # Exit the program
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()