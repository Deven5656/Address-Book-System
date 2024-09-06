'''
    @Author: Deven Gupta
    @Date: 06-09-2024
    @Last Modified by: Deven Gupta
    @Last Modified time: 06-09-2024 
    @Title : Python program to create a logger using logging module

'''

import logging

def create_logger(name):
    """
    Description:
        This function creates a logger that logs messages to both a file and the console.   
    Parameters:
        name (str): The name of the logger to be created. 
    Returns:
        logging.Logger: Configured logger object for logging messages.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
        sformatter = logging.Formatter('%(message)s')
        file_handler = logging.FileHandler('program_logs.log')
        file_handler.setFormatter(formatter)
        
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(sformatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    
    return logger


def main():
    logger = create_logger('main_logger')
    logger.info('This is an info message.')
    logger.warning('This is a warning message.')


if __name__ == '__main__':
    main()