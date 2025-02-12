# contacts.py

contacts = []

def add_contact(name, phone, email):
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    contacts.append(contact)

def list_contacts():
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def find_contact(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]