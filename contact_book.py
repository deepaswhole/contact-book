print("Welcome to the Contact Book!")
contacts = []


def show_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")


def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Contact {name} added successfully!")


def search_contact(name):
    found = [contact for contact in contacts if contact['name'].lower() == name.lower()]
    if found:
        for contact in found:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contact found with that name!")


def delete_contact(name):
    global contacts
    contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    print(f"Contact {name} deleted (if it existed).")


