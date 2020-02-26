#example_module.py
import logging

logger = logging.getLogger(__name__)

def test():
	logger.info('Hello world')