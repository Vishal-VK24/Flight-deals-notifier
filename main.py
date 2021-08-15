#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from users import Users
data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()
notification_manager = NotificationManager()
flight_search.get_city_codes()
users = Users()
print(flight_search.citycode)
for i in data_manager.data_list:
    flight_data.get_flightdata(flight_search.citycode[i["city"]])
    check = flight_data.is_flight(i["lowestprice"])
    if check!=0:
        users_details = users.dict
        notification_manager.send_mail(check,flight_search.citycode,users_details)



