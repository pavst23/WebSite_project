import gspread
import pandas as pd
import json


class Handler():
    def __init__(self):
        self.connect()
        self.data_write()
        self.data_append()
        self.data_update()

    def connect(self):
        gc = gspread.service_account(filename='service_account.json')
        self.read_all_reg = gc.open('Регистрация').get_worksheet(0)
        self.all_reg = self.read_all_reg.get_all_records()
        self.all_reg = pd.DataFrame(self.all_reg)
        self.reg_info = dict(json.load(open('res.json')))

    def data_write(self):
        data_dict = {}
        for key, value in self.reg_info.items():
            data_dict['Name'] = [key]
            data_dict['Email'] = [value[0]]
            data_dict['Age'] = [value[1]]
            data_dict['Sex'] = [value[2]]
            data_dict['Time'] = [value[3]]
            data_dict['Place'] = [value[4]]
            data_dict['About'] = [value[5]]
            data_dict['About2'] = [value[6]]
            data_dict['File'] = [value[7]]
        self.new_data = pd.DataFrame(data_dict)

    def data_append(self):
        self.new_data['Age'] = self.new_data['Age'].astype(object)
        self.all_reg['Age'] = self.all_reg['Age'].astype(object)
        self.result_data = self.all_reg._append(self.new_data, ignore_index=True)
        # print(self.result_data.head())

    def data_update(self):
        self.read_all_reg.update([self.result_data.columns.values.tolist()] + self.result_data.values.tolist())
