import logging
import os

# Define the name of the logger
logger_name = 'system_info_logger'

# Create a logger
logger = logging.getLogger(logger_name)
logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG

# Create a file handler which logs even debug messages
fh = logging.FileHandler(f'{logger_name}.log')
fh.setLevel(logging.DEBUG)

# Create a console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

# Example usage
if __name__ == "__main__":
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
