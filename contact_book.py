import json
import re


FILE_NAME = "contacts.json"


def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


def show_menu():
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")


def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10


def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def add_contact():
    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    phone = input("Enter phone number: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number. Enter exactly 10 digits.")
        return

    email = input("Enter email address: ").strip()

    if not validate_email(email):
        print("Invalid email address.")
        return

    for contact in contacts:
        if contact["phone"] == phone or contact["email"].lower() == email.lower():
            print("Duplicate contact. Phone number or email already exists.")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()

    print("Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACTS =====")

    for i, contact in enumerate(contacts, 1):
        print(f"\n{i}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")


def search_contact():
    if not contacts:
        print("No contacts available.")
        return

    search = input("Enter name, phone number or email to search: ").strip().lower()

    found = False

    for contact in contacts:
        if (search in contact["name"].lower()
                or search in contact["phone"]
                or search in contact["email"].lower()):

            print("\nContact found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("No matching contact found.")


def edit_contact():
    if not contacts:
        print("No contacts available.")
        return

    view_contacts()

    try:
        number = int(input("\nEnter contact number to edit: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        contact = contacts[number - 1]

        new_name = input(f"Enter new name ({contact['name']}): ").strip()

        if new_name != "":
            contact["name"] = new_name

        new_phone = input(
            f"Enter new phone ({contact['phone']}): "
        ).strip()

        if new_phone != "":
            if not validate_phone(new_phone):
                print("Invalid phone number. Edit cancelled.")
                return

            for i, other in enumerate(contacts):
                if i != number - 1 and other["phone"] == new_phone:
                    print("Phone number already belongs to another contact.")
                    return

            contact["phone"] = new_phone

        new_email = input(
            f"Enter new email ({contact['email']}): "
        ).strip()

        if new_email != "":
            if not validate_email(new_email):
                print("Invalid email address. Edit cancelled.")
                return

            for i, other in enumerate(contacts):
                if i != number - 1 and other["email"].lower() == new_email.lower():
                    print("Email already belongs to another contact.")
                    return

            contact["email"] = new_email

        save_contacts()

        print("Contact updated successfully!")

    except ValueError:
        print("Please enter a valid contact number.")


def delete_contact():
    if not contacts:
        print("No contacts available.")
        return

    view_contacts()

    try:
        number = int(input("\nEnter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number.")
            return

        deleted_contact = contacts.pop(number - 1)
        save_contacts()

        print(
            f"Contact '{deleted_contact['name']}' deleted successfully!"
        )

    except ValueError:
        print("Please enter a valid contact number.")


def main():
    print("===== CONTACT BOOK APPLICATION =====")

    while True:
        show_menu()

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            edit_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you for using the Contact Book!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


main()
