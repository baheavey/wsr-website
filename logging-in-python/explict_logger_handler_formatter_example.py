#explicit_logger_handler_formatter_example.py
import logging

logger    = logging.getLogger(__name__)
handler   = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.warning('This is a formatted message')