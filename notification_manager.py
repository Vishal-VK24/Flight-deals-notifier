import smtplib
from data_manager import DataManager
from users import Users
class NotificationManager:
    def __init__(self):
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)
        self.connection.starttls()
        self.data_manager = DataManager()
        self.users = Users()
        self.connection.login(user="zxcvmnbkldsa@gmail.com", password="poiqwerty")
    def send_mail(self,object,citycodes,user_details):
        for i in range (0,len(user_details['First'])):
            message = f" Hey {user_details['First'][i]} {user_details['Last'][i]} You can travel from Chennai to {object['cityTo']} on {object['route'][0]['local_departure'].split('T')[0]} "
            self.connection.sendmail(from_addr="zxcvmnbkldsa@gmail.com",to_addrs=user_details['email'][i],msg=f"subject:Travel Alert!! \n\n {message}\n{object['deep_link']}")

