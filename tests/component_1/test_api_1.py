import json
from lib.http_request import HttpRequest
import logging

logger = logging.getLogger()


class TestComponent(object):

    api_data: dict = None

    @classmethod
    def setup_class(cls):
        logger.info("Setting up the variables and environment")
        # Getting the authentication
        cls.http_object = HttpRequest(auth_option="bearer_token")

        # Capturing api json data
        with open("config//api.json") as f:
            cls.api_data = json.loads(f.read())

    def read_api_data(self, api: str = None) -> dict:
        for key, value in self.api_data.items():
            if key == api:
                return value

    def test_api_1(self):
        http_code, http_response = self.http_object.post_http(api="api_1")
        logger.info(f"Http Code : {http_code} , Response : {http_response}")

        assert http_code in (
            (self.read_api_data(api="api_1"))["api_result"]["success_code"]
        ), logger.error("Status code does not match")

    @classmethod
    def teardown_class(cls):
        logging.info("Tear down test cases")
