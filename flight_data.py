import requests
import datetime
API_KEY = "FA4rpYsougCF9-yDg9guX19Foq-x0O7m"
class FlightData:
    def __init__(self):
         self.fromdate = datetime.datetime.now()
         self.todate = self.fromdate + datetime.timedelta(days = 30)
         self.flight_list = []
         self.check_data =[]
    def get_flightdata(self,tocity):

        headers = {
            "apikey": API_KEY
        }
        parameter={
            "fly_from" : "MAA",
            "fly_to" : tocity,
            "date_from": self.fromdate.strftime("%d/%m/%Y"),
            "date_to" : self.todate.strftime("%d/%m/%Y")
        }
        response = requests.get(url="https://tequila-api.kiwi.com/v2/search",headers=headers,params=parameter)
        self.check_data= response.json()['data']
    def is_flight(self,lowestprice):
        for i in self.check_data:
            if i['price'] < lowestprice:
                self.flight_list.append(i)
        k = sorted(self.flight_list,key=lambda k:k['price'])
        self.check_data = []
        self.flight_list =[]
        if len(k) == 0 :
            return 0
        else:
            return k[0]




