#multiple_handler_example.py
import logging

logger = logging.getLogger(__name__)

# Instantiate Loggers
handler1 = logging.StreamHandler()
handler2 = logging.FileHandler('test.log')

# Set Severity Handler Responds To
handler1.setLevel(logging.DEBUG)
handler2.setLevel(logging.ERROR)

# Add Handlers to Logger
logger.addHandler(handler1)
logger.addHandler(handler2)