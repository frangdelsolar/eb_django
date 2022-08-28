import requests
import environ
from requests.structures import CaseInsensitiveDict

env = environ.Env()
environ.Env.read_env()


class APIEasyBroker():

    def __init__(self):
        self.token = env('EB_TOKEN')
        self.api_url = "https://api.stagingeb.com/v1/properties"

    def get_headers(self):
        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["X-Authorization"] = self.token
        return headers

    def fetch_data(self, url):
        try:
            r = requests.get(url, headers=self.get_headers())
            if r.ok:
                return r
        except requests.exceptions.Timeout:
            return "Bad Response"

    def get_properties_by_page(self, page, limit):
        url = f"{self.api_url}?page={page}&limit={limit}"
        response = self.fetch_data(url)
        return response.json()

    def get_property_by_id(self, id):
        url = f"{self.api_url}/{id}"
        response = self.fetch_data(url)
        return response.json()
