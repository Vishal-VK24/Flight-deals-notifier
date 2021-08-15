import pandas as p
class DataManager:
    def __init__(self):
        self.data = p.read_csv("./destination.csv")
        print(self.data)
        self.data_list = self.data.to_dict(orient="records")
        print(self.data_list)
