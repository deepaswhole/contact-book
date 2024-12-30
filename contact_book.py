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

