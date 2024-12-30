import json
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

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contacts saved to file!")

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
        print("Contacts loaded from file!")
    except FileNotFoundError:
        print("No saved contacts found.")


while True:
    print("\nOptions: [1] Show Contacts [2] Add Contact [3] Search Contact [4] Delete Contact [5] Save [6] Load [7] Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_contacts()
    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        add_contact(name, phone, email)
    elif choice == "3":
        name = input("Enter name to search: ")
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to delete: ")
        delete_contact(name)
    elif choice == "5":
        save_contacts()
    elif choice == "6":
        load_contacts()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")






