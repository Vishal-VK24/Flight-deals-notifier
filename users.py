import pandas as p

class Users:
    def __init__(self):
        self.dict = {
            "First": [],
            "Last": [],
            "email":[]
        }
        data1 = p.read_csv("./user_data.csv")
        k = data1.to_dict(orient="list")
        self.dict['First'] = k['First']
        self.dict['Last'] = k['Last']
        self.dict['email'] = k['email']
    def user_creation(self):
        first = input("Enter your First name ")
        last = input("Enter your Last name ")
        email = input("Enter your email id ")
        self.dict['First'].append(first)
        self.dict['Last'].append(last)
        self.dict['email'].append(email)
        data = p.DataFrame(self.dict)
        data.to_csv("./user_data.csv",index=False)
