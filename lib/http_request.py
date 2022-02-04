from typing import Tuple
import requests
import json
import logging
import urllib3

logger = logging.getLogger()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HttpRequest:

    def __init__(self, auth_option: str = 'bearer_token') -> None:
        """ Initialization and declearation
        """
        self.token: str = None

        if auth_option == "bearer_token":
            self.token = self.fetch_token_credential()

    def fetch_token_credential(self) -> str:
        result = {}
        with open('config//cred.json') as f:
            cred = json.loads(f.read())
            for data, value in cred.items():
                if data == "bearer_token":
                    return value["token"]

    def fetch_api_raw_data(self, api: str = None) -> dict:
        with open('config//api.json') as f:
            api_data = json.loads(f.read())
            for api_key, api_value in api_data.items():
                if api_key == api:
                    return api_value

        logger.info("API does not exist")
        return None

    def get_http(self, url: str = None, api: str = None,
                 payload: dict = None) -> Tuple[int, str]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        api_data = self.fetch_api_raw_data(api=api)

        if self.token:
            headers = {
                'Authorization': 'Bearer ' + self.token,
                'Content-Type': 'application/json'
            }
        if url == None:
            url = api_data["url"]
            logging.info(f"URL : {url}")

        response = requests.request("GET", url, headers=headers)

        return (response.status_code, response.text)

    def post_http(self, url: str = None, api: str = None,
                  payload: dict = None) -> Tuple[int, str]:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        api_data = self.fetch_api_raw_data(api=api)
        if self.token:
            headers = {
                'Authorization': 'Bearer ' + self.token,
                'Content-Type': 'application/json'
            }
        if url == None:
            url = api_data["url"]
            logging.info(f"URL : {url}")

        if payload == None:
            payload = json.dumps(api_data["api_input"]["body"])
            logging.info(f"Payload : {payload}")

        response = requests.request("POST", url, headers=headers, data=payload)
        return (response.status_code, response.text)
