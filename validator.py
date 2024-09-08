'''
    @Author: Deven Gupta
    @Date: 06-09-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 06-09-2024 
    @Title : Python program for User Registration Problem

'''

import re

def is_valid_name(name):
    """
    Description:
        This function is use to match the pattern in name
    Parameters:
        name (str): name of user
    Returns:
        boolean : True if match else False
    """
    pattern = r'^[a-zA-Z]{3,}$'
    return bool(re.match(pattern, name))

def is_valid_email(email):
    """
    Description:
        This function is use to match the pattern in email
    Parameters:
        email (str): mail of user
    Returns:
        boolean : True if match else False
    """
    #other method
    # pattern = r'(?!.*\.\.)(?!^\.)([a-zA-Z0-9._%+-])+(?<!\.)@([a-zA-Z0-9-]+\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?$'
    pattern = r'^[\w]+([._%+-][\w]+)*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\.[a-zA-Z]{2,})?$'
    return bool(re.match(pattern, email))

def is_valid_mobile(mobile):
    """
    Description:
        This function is use to match the pattern in mobile number
    Parameters:
        mobile (str): mobile number of user
    Returns:
        boolean : True if match else False
    """
 
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, mobile))

def is_valid_zip(zip):
    """
    Description:
        This function is use to match the pattern in mobile number
    Parameters:
        mobile (str): mobile number of user
    Returns:
        boolean : True if match else False
    """
 
    pattern = r'^\d{6}$'
    return bool(re.match(pattern, zip))

def is_valid_address(address):
    """
    Description:
        This function is use to match the pattern in ADDRESS
    Parameters:
        address (str): address of user
    Returns:
        boolean : True if match else False
    """
 
    pattern = r'^[\w]+(?:\s)?[\w\s]+(?:\s[A-Za-z0-9\s]+)?$'
    return bool(re.match(pattern, address))


def main():

    print("Validator Running")

if __name__ == "__main__":
    main()

   