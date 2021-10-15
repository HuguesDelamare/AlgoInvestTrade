# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.
import itertools

from csv import DictReader
from csv import reader
import operator
import os
import time

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
                    list_of_row = []
                    csv_reader = reader(read_obj)
                    for row in csv_reader:
                        list_of_row.append(row)
                    self.combination(list_of_row, 2)

    def combination(self, iterable, n):
        iterable_row_count = len(iterable)-1
        indices = list(range(n))
        # Parcours les rows de 0 a n, ex : ('Share-XJDT', '0.0', '37.11')
        yield tuple(iterable[i+1] for i in indices)
        while True:
            # 0 1 2 3 4 5 etc
            for i in reversed(range(n)):
                # ex : if 5 != 5 + 1001 - 6 = 1000
                if indices[i] != i + iterable_row_count - n:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, n):
                indices[j] = indices[j-1] + 1
            yield tuple(iterable[i] for i in indices)


if __name__ == "__main__":
    start_time = time.time()
    Algorithm().get_csv_files()
    print("--- %s seconds ---" % (time.time() - start_time))


# SAC A DOS = 1 etape a la fois, se coupe sur les montants utilisés