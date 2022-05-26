import pytest
import requests
import logging
from test_data import TestDataForQaEnv

# change to switch to another env
env = TestDataForQaEnv


class Requests:
    @staticmethod
    def send_create_request():
        logging.info(f'URL for testing: {env.link}\nParameters for testing: {env.parameters}\n')
        r = requests.post(env.link, json=env.parameters)
        if r.ok:
            return r.json()
        else:
            logging.error(r.text)
            pytest.exit('Problem with setup')

    @staticmethod
    def send_delete_request(link):
        requests.delete(link)
