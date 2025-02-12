# main.py

from contacts import add_contact, list_contacts, find_contact, delete_contact
from utils import get_input, print_menu

def main():
    while True:
        print_menu()
        choice = get_input("Choose an option: ")

        if choice == '1':
            name = get_input("Enter name: ")
            phone = get_input("Enter phone: ")
            email = get_input("Enter email: ")
            add_contact(name, phone, email)
            print(f"Contact {name} added.")
        elif choice == '2':
            list_contacts()
        elif choice == '3':
            name = get_input("Enter name to find: ")
            contact = find_contact(name)
            if contact:
                print(f"Found contact: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            else:
                print("Contact not found.")
        elif choice == '4':
            name = get_input("Enter name to delete: ")
            delete_contact(name)
            print(f"Contact {name} deleted.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()