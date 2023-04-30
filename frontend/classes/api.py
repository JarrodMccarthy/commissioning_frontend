import json
import requests
from environment.settings import base_api_url

class API:
    def __init__(self) -> None:
        self.base_url = base_api_url

    def get_sensor_measurement(self, device_id: str, metric: str):
        url = f"{self.base_url}/device/measurement?deviceid={device_id}&metric={metric}"
        response = requests.request("GET", url, headers={}, data={})
        return json.loads(response.text)
    
    def get_sensors(self):
        url = f"{self.base_url}/device"
        response = requests.request("GET", url, headers={}, data={})
        return json.loads(response.text)