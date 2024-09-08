'''
    @Author: Deven Gupta
    @Date: 06-09-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 06-09-2024 
    @Title : Python program to create an Address Book System
'''
from validator import *
from logger import create_logger

class AddressBook:
    logger = create_logger('AddressBook_logger')
    
    def __init__(self):
        self.contacts = {}

    def _normalize_name(self, name):
        """
        Description:
            Normalizes the name by converting it to lowercase.
        Parameters:
            name (str): The name to be normalized.
        Returns:
            str: The normalized name in lowercase.
        """
        return name.strip().lower()

    def add_contact(self):
        """
        Description:
            Prompts the user for contact details and adds the contact to the address book (One at a time).
        Parameters:
            None
        Returns:
            None
        """
        print("Enter contact details:")
        first_name = input("First name: ")
        while not is_valid_name(first_name):
            print("Invalid name. Please enter alphabetic characters only with at least 3 length.")
            first_name = input("First name: ")

        last_name = input("Last name: ")
        while not is_valid_name(last_name):
            print("Invalid name. Please enter alphabetic characters only with at least 3 length.")
            last_name = input("Last name: ")
        
        normalized_name = (self._normalize_name(first_name), self._normalize_name(last_name))

        if normalized_name in self.contacts:
            print("Contact with this name already exists.")
            return
        
        address = input("Address: ")
        while not is_valid_address(address):
            print("Invalid Address. Use spaces, alphabets, and digits only.")
            address = input("Address: ")

        city = input("City: ")
        while not is_valid_name(city):
            print("Invalid city. Please enter alphabetic characters only with at least 3 length.")
            city = input("City: ")

        state = input("State: ")
        while not is_valid_name(state):
            print("Invalid State. Please enter alphabetic characters only with at least 3 length.")
            state = input("State: ")

        zip_code = input("Zip code: ")
        while not is_valid_zip(zip_code):
            print("Invalid zip code. Please enter a 6-digit zip code.")
            zip_code = input("Zip code: ")

        phone_number = input("Phone number: ")
        while not is_valid_mobile(phone_number):
            print("Invalid phone number. Please enter a 10-digit number.")
            phone_number = input("Phone number: ")

        email = input("Email: ")
        while not is_valid_email(email):
            print("Invalid email address. Please enter a valid email.")
            email = input("Email: ")
        
        self.contacts[normalized_name] = {
            'First Name': first_name,
            'Last Name': last_name,
            'Address': address,
            'City': city,
            'State': state,
            'Zip Code': zip_code,
            'Phone Number': phone_number,
            'Email': email
        }
        self.logger.info(f"Contact {first_name} {last_name} added successfully.\n")

    def edit_contact(self):
        """
        Description:
            Prompts the user for the contact they wish to edit and updates the contact in the address book.
        Parameters:
            None
        Returns:
            None
        """
        print("Enter the name of the contact to edit:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        normalized_name = (self._normalize_name(first_name), self._normalize_name(last_name))

        contact = self.contacts.get(normalized_name)
        if not contact:
            print("Contact not found.")
            self.logger.info(f"Attempted to edit non-existent contact: {first_name} {last_name}.")
            return

        print("Enter new details (leave blank to keep current value):")
        
        new_first_name = input(f"First Name ({contact['First Name']}): ")
        new_last_name = input(f"Last Name ({contact['Last Name']}): ")

        # Only update normalized_name if at least one of the names is changed
        if new_first_name or new_last_name:
            # Handle name changes
            if new_first_name:
                while not is_valid_name(new_first_name):
                    print("Invalid name. Please enter alphabetic characters only with at least 3 length.")
                    new_first_name = input("Enter new First Name: ")
                contact['First Name'] = new_first_name

            if new_last_name:
                while not is_valid_name(new_last_name):
                    print("Invalid name. Please enter alphabetic characters only with at least 3 length.")
                    new_last_name = input("Enter new Last Name: ")
                contact['Last Name'] = new_last_name

            # Remove old entry
            try:
                self.contacts.pop(normalized_name)
            except KeyError:
                self.logger.info(f"Old entry for {normalized_name} not found while updating names.")

            # Update normalized name
            normalized_name = (self._normalize_name(contact['First Name']), self._normalize_name(contact['Last Name']))

        # Update other details
        new_address = input(f"Address ({contact['Address']}): ")
        if new_address:
            while not is_valid_address(new_address):
                print("Invalid Address. Use spaces, alphabets, and digits only.")
                new_address = input("Enter new Address: ")
            contact['Address'] = new_address

        new_city = input(f"City ({contact['City']}): ")
        if new_city:
            while not is_valid_name(new_city):
                print("Invalid city. Please enter alphabetic characters only with at least 3 length.")
                new_city = input("Enter new City: ")
            contact['City'] = new_city

        new_state = input(f"State ({contact['State']}): ")
        if new_state:
            while not is_valid_name(new_state):
                print("Invalid State. Please enter alphabetic characters only with at least 3 length.")
                new_state = input("Enter new State: ")
            contact['State'] = new_state

        new_zip_code = input(f"Zip Code ({contact['Zip Code']}): ")
        if new_zip_code:
            while not is_valid_zip(new_zip_code):
                print("Invalid zip code. Please enter a 6-digit zip code.")
                new_zip_code = input("Enter new Zip Code: ")
            contact['Zip Code'] = new_zip_code

        new_phone_number = input(f"Phone Number ({contact['Phone Number']}): ")
        if new_phone_number:
            while not is_valid_mobile(new_phone_number):
                print("Invalid phone number. Please enter a 10-digit number.")
                new_phone_number = input("Enter new Phone Number: ")
            contact['Phone Number'] = new_phone_number

        new_email = input(f"Email ({contact['Email']}): ")
        if new_email:
            while not is_valid_email(new_email):
                print("Invalid email address. Please enter a valid email.")
                new_email = input("Enter new Email: ")
            contact['Email'] = new_email
        
        # Save updated contact with new normalized name if name was changed
        self.contacts[normalized_name] = contact
        self.logger.info(f"Contact {contact['First Name']} {contact['Last Name']} updated successfully.\n")

    def delete_contact(self):
        """
        Description:
            Prompts the user for the contact they wish to delete and removes the contact from the address book.
        Parameters:
            None
        Returns:
            None
        """
        print("Enter the name of the contact to delete:")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        normalized_name = (self._normalize_name(first_name), self._normalize_name(last_name))

        if normalized_name in self.contacts:
            self.contacts.pop(normalized_name)
            self.logger.info(f"Contact {first_name} {last_name} deleted successfully.\n")
        else:
            print("Contact not found.")
            self.logger.info(f"Attempted to delete non-existent contact: {first_name} {last_name}.")

    def view_contact(self, first_name, last_name):
        """
        Description:
            Retrieves and prints the details of a specific contact identified by first and last name.
        Parameters:
            first_name (str): The first name of the contact.
            last_name (str): The last name of the contact.
        Returns:
            None
        """
        normalized_name = (self._normalize_name(first_name), self._normalize_name(last_name))
        contact = self.contacts.get(normalized_name)
        if contact:
            self.logger.info(f"Full Name: {contact['First Name']} {contact['Last Name']}")
            for key, value in contact.items():
                if key not in ['First Name', 'Last Name']:
                    self.logger.info(f"{key}: {value}")
        else:
            self.logger.info("Contact not found.")

    def view_all_contacts(self):
        """
        Description:
            Prints the details of all contacts in the address book.
            Each contact is displayed with full name, address (including city, state, and zip code),
            phone number, and email. 
        Parameters:
            None
        Returns:
            None
        """
        
        if self.contacts:
            for normalized_name, details in self.contacts.items():
                self.logger.info(f"Full Name: {details['First Name']} {details['Last Name']}")
                self.logger.info(f"Full Address: {details['Address']}, {details['City']}, {details['State']} {details['Zip Code']}")
                self.logger.info(f"Phone Number: {details['Phone Number']}")
                self.logger.info(f"Email: {details['Email']}\n")
        else:
            self.logger.info("No contacts available.\n")

def main():
    address_book = AddressBook()
    print("*** Welcome to Address Book Program ***")
    while True:
        print("Options")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View Contact")
        print("5. View All Contacts")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            address_book.add_contact()
        elif choice == '2':
            address_book.edit_contact()
        elif choice == '3':
            address_book.delete_contact()
        elif choice == '4':
            try:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                address_book.view_contact(first_name, last_name)
            except ValueError:
                address_book.logger.info("Invalid input. Please enter valid names.")
        elif choice == '5':
            address_book.view_all_contacts()
        elif choice == '6':
            address_book.logger.info("Exiting the system. Goodbye!")
            break
        else:
            address_book.logger.info("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()
