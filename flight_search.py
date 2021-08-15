from data_manager import DataManager
import requests
API_KEY="FA4rpYsougCF9-yDg9guX19Foq-x0O7m"
class FlightSearch:

    def __init__(self):
        self.data_manager = DataManager()
        self.headers = {
            "apikey": API_KEY
        }
        self.citycode = {

        }
    def get_city_codes(self):
        for i in self.data_manager.data_list:
            city = i["city"]
            parameter = {
                "term": city,
                "location types": "city"
            }
            response1 = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=parameter,
                                     headers=self.headers)
            self.citycode[city] = response1.json()["locations"][0]["code"]