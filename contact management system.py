class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def display_contact(self):
        print("Name    :", self.name)
        print("Phone   :", self.phone)
        print("Email   :", self.email)
        print("Address :", self.address)

class ContactManager:

    def __init__(self):
        # List to store contact objects
        self.contacts = []

    def add_contact(self):
        print("\n----- Add Contact -----")

        name = input("Enter Name    : ")
        phone = input("Enter Phone   : ")
        email = input("Enter Email   : ")
        address = input("Enter Address : ")

        contact = Contact(name, phone, email, address)

        self.contacts.append(contact)

        print("Contact added successfully!")

    def view_contacts(self):
        print("\n----- All Contacts -----")

        if len(self.contacts) == 0:
            print("No contacts available.")
            return

        for contact in self.contacts:
            contact.display_contact()
            print("------------------------")

    def search_contact(self):
        print("\n----- Search Contact -----")

        search = input("Enter Name or Phone Number : ")

        found = False

        for contact in self.contacts:
            if contact.name.lower() == search.lower() or contact.phone == search:
                contact.display_contact()
                found = True
                break

        if found == False:
            print("Contact not found.")

    def update_contact(self):
        print("\n----- Update Contact -----")

        search = input("Enter Name or Phone Number : ")

        for contact in self.contacts:

            if contact.name.lower() == search.lower() or contact.phone == search:

                print("\nContact Found")
                contact.display_contact()

                print("\nEnter new details")
                contact.phone = input("Enter New Phone   : ")
                contact.email = input("Enter New Email   : ")
                contact.address = input("Enter New Address : ")

                print("Contact updated successfully!")
                return

        print("Contact not found.")

    def delete_contact(self):
        print("\n----- Delete Contact -----")

        search = input("Enter Name or Phone Number : ")

        for contact in self.contacts:

            if contact.name.lower() == search.lower() or contact.phone == search:

                contact.display_contact()

                confirm = input("Are you sure you want to delete? (yes/no): ")

                if confirm.lower() == "yes":
                    self.contacts.remove(contact)
                    print("Contact deleted successfully!")
                else:
                    print("Delete operation cancelled.")

                return

        print("Contact not found.")


# Create ContactManager object
manager = ContactManager()


# Main menu
while True:

    print("\n========== CONTACT MANAGEMENT SYSTEM ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_contact()

    elif choice == "2":
        manager.view_contacts()

    elif choice == "3":
        manager.search_contact()

    elif choice == "4":
        manager.update_contact()

    elif choice == "5":
        manager.delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Management System!")
        break

    else:
        print("Invalid choice. Please try again.")