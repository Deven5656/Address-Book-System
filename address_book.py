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
            Prompts the user for contact details and adds the contact to the address book.
            Logs the addition of the contact.
        Parameters:
            None
        Returns:
            None
        """
        print("Enter contact details:")
        first_name = input("First name: ")
        while not is_valid_name(first_name):
            print("Invalid name. Please enter alphabetic characters only with atleast 3 lenghth.")
            first_name = input("First name: ")

        last_name = input("Last name: ")
        while not is_valid_name(last_name):
            print("Invalid name. Please enter alphabetic characters only with atleast 3 lenghth.")
            last_name = input("Last name: ")
        
        normalized_name = (self._normalize_name(first_name), self._normalize_name(last_name))

        if normalized_name in self.contacts:
            print("Contact with this name already exists.")
            return
        
        address = input("Address: ")
        while not is_valid_address(address):
            print("Invalid Address. use spaces , alphabate and digit only")
            address = input("Address: ")

        city = input("City: ")
        while not is_valid_name(city):
            print("Invalid city. Please enter alphabetic characters only with atleast 3 lenghth.")
            city = input("City: ")

        state = input("State: ")
        while not is_valid_name(state):
            print("Invalid State. Please enter alphabetic characters only with atleast 3 lenghth.")
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
        print("2. View Contact")
        print("3. View All Contacts")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            address_book.add_contact()
        elif choice == '2':
            try:
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                address_book.view_contact(first_name, last_name)
            except ValueError:
                address_book.logger.info("Invalid input. Please enter valid names.")
        elif choice == '3':
            address_book.view_all_contacts()
        elif choice == '4':
            address_book.logger.info("Exiting the system. Goodbye!")
            break
        else:
            address_book.logger.info("Invalid choice. Please enter a number between 1 and 4.\n")


if __name__ == "__main__":
    main()
