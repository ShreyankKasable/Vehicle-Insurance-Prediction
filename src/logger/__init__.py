"""
     Before building logfile we need to figure out few things like
    1. Log Directory name.
    2. Log file name.
    3. Log Destination (Console, File, Both).
    4. Log Format
    5. Log Level
    6. Log rotation Policy (
        - Size-based rotation(e.g. rotate after 5MB).
        - Time-based rotation(e.g. Daily).
    )
    """


# Importing all necessary libraries
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
from from_root import from_root

# Setting constants for log rotation policy
MAX_LOG_SIZE = 5*1024*1024 # 5 MB
BACKUP_COUNT = 3 # Number of backup log files to keep

# Setting log directory
LOG_DIR = "logs"
LOG_DIR_PATH = os.path.join(from_root(), LOG_DIR)
os.makedirs(LOG_DIR_PATH, exist_ok=True)

# Setting log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE)

def configure_logger():
    """
    CONFIGURE_LOGGER
    :RETURN: None
    """

    # CREATE A ROOT LOGGER INSTANCE
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # SET LOG LEVEL TO DEBUG TO CAPTURE ALL LEVELS

    # DEFINE LOG FORMATTER FOR CONSISTENT LOG OUTPUT
    log_format = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")

    # ===============================
    # CONFIGURE FILE HANDLER WITH ROTATION
    # ===============================
    file_handler = RotatingFileHandler(
        LOG_FILE_PATH,            # PATH TO THE LOG FILE
        maxBytes=MAX_LOG_SIZE,    # MAXIMUM SIZE OF A SINGLE LOG FILE
        backupCount=BACKUP_COUNT  # NUMBER OF BACKUP FILES TO KEEP
    )
    file_handler.setFormatter(log_format)   # APPLY FORMATTER TO FILE HANDLER
    file_handler.setLevel(logging.DEBUG)    # SET FILE HANDLER LOG LEVEL

    # ===============================
    # CONFIGURE CONSOLE (STREAM) HANDLER
    # ===============================
    console_handler = logging.StreamHandler()    # STREAM HANDLER FOR CONSOLE OUTPUT
    console_handler.setFormatter(log_format)     # APPLY FORMATTER TO CONSOLE HANDLER
    console_handler.setLevel(logging.INFO)       # SET CONSOLE HANDLER LOG LEVEL

    # ===============================
    # ADD BOTH HANDLERS TO LOGGER
    # ===============================
    logger.addHandler(file_handler)   # ADD FILE HANDLER TO LOGGER
    logger.addHandler(console_handler)  # ADD CONSOLE HANDLER TO LOGGER

# INITIALIZE THE LOGGER CONFIGURATION
configure_logger()

