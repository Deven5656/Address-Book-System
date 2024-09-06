'''
    @Author: Deven Gupta
    @Date: 06-09-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 06-09-2024 
    @Title : Python program to create an Address Book System

'''

from logger import create_logger

contacts = {}
def add_contact(first_name, last_name, address, city, state, zip_code, phone_number, email,logger):
    contacts[(first_name, last_name)] = {
        'Address': address,
        'City': city,
        'State': state,
        'Zip Code': zip_code,
        'Phone Number': phone_number,
        'Email': email
    }
    logger.info(f"Contact {first_name} {last_name} added successfully.\n")


def main():     
    logger=create_logger('AddressBook_logger')

    logger.info("*** Welcome to Address Book Program ***\n")


    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter zip code: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")

    add_contact(first_name, last_name, address, city, state, zip_code, phone_number, email ,logger)

    contact = contacts.get((first_name, last_name))
    logger.info(f"Name : {first_name} {last_name}")
    for key, value in contact.items():
        logger.info(f"{key}: {value}")
 
if __name__ == "__main__":
    main()