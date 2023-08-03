import requests
import json
from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data
from PIL import Image
from io import BytesIO

class CatConnection(ExperimentalBaseConnection[requests.Session]):
    def __init__(self, *args, connection_name=None, **kwargs):
        super().__init__(*args, connection_name=connection_name, **kwargs)
        self._resource = self._connect()
    def _connect(self) -> requests.Session:
        return requests.Session()
    def cursor(self):
        return self._resource
    
    def randon_query(self):
        cache_data(ttl=0)
        def getCats():
            url = 'https://cataas.com/cat'
            print(f"URL is {url}")
            response = self._resource.get(url)
            if response.status_code == 200:
                return response.content
            else:
                raise Exception(f"Failed to fetch.")
        return getCats()
    
    def query(self, tag = None, gif=False, says = None, ttl: int = 10):
        @cache_data(ttl=ttl)
        def getCats(tag, gif, says):
            url = 'https://cataas.com/cat'
            if gif:
                url += "/gif"
            else:
                if tag:
                    url += "/" + tag
                if says:
                    url += "/says/" + says
            print(f"URL is {url}")
            response = self._resource.get(url)
            if response.status_code == 200:
                return response.content
            else:
                raise Exception(f"Failed to fetch.")

            return recipe_data
        return getCats(tag, gif, says)

        
       
