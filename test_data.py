class TestDataForAllEnvs:
    user_name = 'Cherepashka'


class TestDataForQaEnv:
    link = 'https://petstore.swagger.io/v2/pet'
    name = 'Tasha'
    category_id = 1234567
    category = 'dogs'
    photo_url = 'https://i.natgeofe.com/n/4f5aaece-3300-41a4-b2a8-ed2708a0a27c/domestic-dog_thumb_4x3.jpg'
    parameters = {"category": {"id": category_id, "name": category}, "name": name, "photoUrls": [photo_url],
                  "status": "available"}


class TestDataForDevEnv:
    name = 'Pasha'


class TestDataForProdEnv:
    name = 'Natasha'
