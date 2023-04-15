import gspread
import pandas as pd
import json


class Handler():
    def __int__(self):
        self.connect()

    def connect(self):
        gc = gspread.service_account(filename='service_account.json')
        read_cart_orders = gc.open('Регистрация').get_worksheet(0)
        cart_orders = read_cart_orders.get_all_values()
        self.cart_orders_data = pd.DataFrame(cart_orders)
        reg_info = json.load(open('res.json'))

