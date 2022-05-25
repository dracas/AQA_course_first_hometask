import pytest
from main_functions import Requests
from test_data import TestDataForQaEnv

# change to switch to another env
env = TestDataForQaEnv


@pytest.fixture(scope="class")
def setting_env():
    setting_env = Requests.send_create_request()
    yield setting_env
    delete_link = f"{env.link}/{setting_env.get('id')}"
    Requests.send_delete_request(delete_link)


class TestOfResponseOfCreateRequest:
    def test_name_in_the_response_is_the_same_as_in_the_request(self, setting_env):
        name = setting_env.get('name')
        assert name == env.name, 'name in the response is different'

    def test_category_id_in_the_response_is_the_same_as_in_the_request(self, setting_env):
        category_id = setting_env.get('category').get('id')
        assert category_id == env.category_id, 'category id in the response is different'

