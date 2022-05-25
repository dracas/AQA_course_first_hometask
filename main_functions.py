import requests
import logging
from test_data import TestDataForQaEnv

# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')

# change to switch to another env
env = TestDataForQaEnv


class Requests:
    @staticmethod
    def send_create_request():
        logging.info(f'URL for testing: {env.link}\nParameters for testing: {env.parameters}\n')
        r = requests.post(env.link, json=env.parameters)
        return r.json()

    @staticmethod
    def send_delete_request(link):
        requests.delete(link)
