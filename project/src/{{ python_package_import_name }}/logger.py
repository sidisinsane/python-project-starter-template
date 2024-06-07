"""
Set up logging for an application, configuring both file and console output.

Load environment variables from a .env file, specifically requiring the
`LOG_FILEPATH` environment variable to specify where log files should be
stored. If the directory for the log file does not exist, it will
be created.

The module sets up two handlers:
1. A file handler that writes logs to a file with a detailed format and
   debug-level logging.
2. A console handler that prints logs to the console with a simplified
   format and info-level logging.

Usage:
    Run this module directly to see example log messages at different
    log levels.

Environment Variables:
    LOG_FILEPATH: The file path to the log entries file. This variable
                  must be set in the .env file.

Example:
    >>> hatch run logger
    Output log messages to the console and save them to the specified log file.
    >>> log.debug("This is a custom debug message")
    Write debug log to log file and prints it to console.
    >>> log.info("This is a custom info message")
    Write info log to log file and prints it to console.
    >>> log.warning("This is a custom warning message")
    Write warning log to log file and prints it to console.
    >>> log.error("This is a custom error message")
    Write error log to log file and prints it to console.

Raises:
    OSError: If the `LOG_FILEPATH` environment variable is not set.
"""

import logging
import os

from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv(override=True)


# Fetch environment variables.
LOG_FILEPATH = os.environ.get("LOG_FILEPATH")
if not LOG_FILEPATH:
    raise OSError("LOG_FILEPATH environment variable not set.")

if not os.path.exists(os.path.dirname(LOG_FILEPATH)):
    os.makedirs(os.path.dirname(LOG_FILEPATH))


# Create a formatter to define the log format
file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_formatter = logging.Formatter("%(levelname)s - %(message)s")

# Create a file handler to write logs to a file
file_handler = logging.FileHandler(LOG_FILEPATH)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)

# Create a stream handler to print logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # You can set the desired log level for console output
console_handler.setFormatter(console_formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.debug("This is a default debug message")
    logging.info("This is a default info message")
    logging.warning("This is a default warning message")
    logging.error("This is a default error message")

    log.debug("This is a custom debug message")
    log.info("This is a custom info message")
    log.warning("This is a custom warning message")
    log.error("This is a custom error message")
