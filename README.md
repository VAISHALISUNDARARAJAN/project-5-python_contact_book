# Python Contact Book

A simple command-line Contact Book application developed using Python.

## Features

- Add new contacts
- View all contacts
- Search contacts by name, phone number or email
- Edit existing contacts
- Delete contacts
- Store contacts using JSON file persistence
- Validate 10-digit phone numbers
- Validate email addresses
- Prevent duplicate phone numbers and email addresses
- Handle invalid user input

## Technologies Used

- Python
- JSON
- Regular Expressions

## Contact Information

Each contact contains:

- Name
- Phone Number
- Email Address

## Available Operations

| Option | Operation |
|--------|-----------|
| 1 | Add Contact |
| 2 | View Contacts |
| 3 | Search Contact |
| 4 | Edit Contact |
| 5 | Delete Contact |
| 6 | Exit |

## Data Persistence

Contacts are stored in a `contacts.json` file.

The application automatically:

- Loads saved contacts when the program starts.
- Saves new contacts.
- Saves edited contacts.
- Saves changes after deleting contacts.

## Search

Contacts can be searched using:

- Name
- Phone number
- Email address

## Validation

The application validates:

- Name cannot be empty.
- Phone number must contain exactly 10 digits.
- Email address must have a valid email format.
- Duplicate phone numbers are not allowed.
- Duplicate email addresses are not allowed.

## How to Run

1. Make sure Python is installed on your computer.
2. Open `contact_book.py` using Python IDLE or any Python IDE.
3. Run the program.
4. Select an option from the menu.
5. Follow the instructions displayed on the screen.

## Example

```text
===== CONTACT BOOK =====
1. Add Contact
2. View Contacts
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit

Enter your choice (1-6): 1
Enter name: Vaishali
Enter phone number: 9876543210
Enter email address: vaishali@example.com
Contact added successfully!

Error Handling
The application handles:
Empty names
Invalid phone numbers
Invalid email addresses
Duplicate contacts
Invalid contact numbers
Invalid menu choices
Non-numeric input
Project Structure
python-contact-book/
│
├── contact_book.py
├── contacts.json
├── README.md
└── screenshots/
    ├── add-contact.png
    ├── view-contacts.png
    ├── search-contact.png
    ├── edit-contact.png
    └── delete-contact.png
Demo Screenshots
The screenshots folder contains examples of adding, viewing, searching, editing and deleting contacts.
