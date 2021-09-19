# Chaque action ne peut être achetée qu'une seule fois.
# Nous ne pouvons pas acheter une fraction d'action.
# Nous pouvons dépenser au maximum 500 euros par client.

from csv import DictReader
from csv import reader
import operator
import os

# skip first line i.e. read header first and then iterate over each row od csv as a list
cwd = os.getcwd()
desktop = os.path.join(cwd, "data")
files = os.listdir(desktop)
data = []


for file in files:
    if file is file.endswith('.csv'):
        print("Not a CSV file.")
        pass
    else:
        with open('data/'+file, 'r') as read_obj:
            csv_reader = reader(read_obj)
            # sorted(csv_reader, key = lambda x:float(x), reverse=False)
            sortedlist = sorted(csv_reader, key=operator.itemgetter(1), reverse=False)
            for row in sortedlist:
                data.append(row)

client_purchases = []
client_credit = float(500)

for item in data:
    print(item[0] + ' | ' + item[1] + ' | ' + item[2])
