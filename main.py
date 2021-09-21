# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.

from csv import DictReader
from csv import reader
import operator
import os


class Algorithm:
    def __init__(self):
        self.data = {
            'data': []
        }
        self.client_shares_bought = []
        self.client_wallet = 500

    def get_csv_files(self):
        cwd = os.getcwd()
        desktop = os.path.join(cwd, "data")
        files = os.listdir(desktop)
        self.get_all_data_from_csv(files)

    def get_all_data_from_csv(self, files):
        for file in files:
            if not file.endswith('.csv'):
                print("Not a CSV file.")
                pass
            else:
                with open('data/'+file, 'r') as read_obj:
                    csv_reader = reader(read_obj)
                    for row in csv_reader:
                        try:
                            if float(row[1]) == 0:
                                serialized_data = self.serializing_data(row, 0)
                                self.data['data'].append(serialized_data)
                                self.client_shares_bought.append(serialized_data)
                            elif float(row[1]) <= 0:
                                self.client_wallet += abs(float(row[1]))
                                serialized_data = self.serializing_data(row, 0)
                                self.client_shares_bought.append(serialized_data)
                            else:
                                ratio = self.calculating_ratio(row)
                                serialized_data = self.serializing_data(row, ratio)
                                self.data['data'].append(serialized_data)
                        except ValueError:
                            pass
        print('Wallet: ' + str(self.client_wallet))
        print(self.client_shares_bought)
        self.buy_shares(self.data)

    def serializing_data(self, data_row, ratio):
        serialized_data = {
            'name': data_row[0],
            'price': float(data_row[1]),
            'profit': float(data_row[2]),
            'ratio': ratio
        }
        return serialized_data

    def calculating_ratio(self, data_row):
        ratio = float(data_row[2]) / float(data_row[1])
        return ratio

    def buy_shares(self, data):
        data['data'].sort(key=lambda e: e['ratio'], reverse=True)
        for item in data['data']:
            print(item)


if __name__ == "__main__":
    Algorithm().get_csv_files()
