import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot2.log'
)
logging.info('This message should go to the log file')