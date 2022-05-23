import requests
from test_data import TestData


def send_create_request():
    r = requests.post(TestData.link, json=TestData.parameters)
    return r.json()


def send_delete_request(link):
    requests.delete(link)


class TestPostResponseContainsNeededInformation:
    def test_name_in_the_response_is_the_same_as_in_the_request(self):
        fun_object = send_create_request()
        try:
            name = fun_object['name']
            assert name == TestData.name, 'some hint text'
        finally:
            new_link = TestData.link + '/' + str(fun_object['id'])
            send_delete_request(new_link)

    def test_category_id_in_the_response_is_the_same_as_in_the_request(self):
        fun_object = send_create_request()
        try:
            category_id = fun_object['category']['id']
            assert category_id == TestData.category_id, 'some hint text'
        finally:
            new_link = TestData.link + '/' + str(fun_object['id'])
            send_delete_request(new_link)
