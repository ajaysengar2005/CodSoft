class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __repr__(self):
        return f"{self.name} ({self.phone})"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = Contact(name, phone, email, address)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query in contact.name or query in contact.phone]
        if results:
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts found.")

    def update_contact(self, phone, new_name=None, new_phone=None, new_email=None, new_address=None):
        for contact in self.contacts:
            if contact.phone == phone:
                contact.name = new_name or contact.name
                contact.phone = new_phone or contact.phone
                contact.email = new_email or contact.email
                contact.address = new_address or contact.address
                print(f"Contact {contact.name} updated successfully!")
                return
        print("Contact not found.")

    def delete_contact(self, phone):
        for contact in self.contacts:
            if contact.phone == phone:
                self.contacts.remove(contact)
                print(f"Contact {contact.name} deleted successfully!")
                return
        print("Contact not found.")

# User Interface
def main():
    manager = ContactManager()
    while True:
        print("\n1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            phone = input("Enter phone number of contact to update: ")
            new_name = input("Enter new name (or press Enter to skip): ")
            new_phone = input("Enter new phone number (or press Enter to skip): ")
            new_email = input("Enter new email (or press Enter to skip): ")
            new_address = input("Enter new address (or press Enter to skip): ")
            manager.update_contact(phone, new_name, new_phone, new_email, new_address)

        elif choice == '5':
            phone = input("Enter phone number of contact to delete: ")
            manager.delete_contact(phone)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
