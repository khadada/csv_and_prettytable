import csv
from prettytable import PrettyTable
table = PrettyTable()

with open("weather-data.csv") as data:
    info = csv.reader(data)
    temptures = []
    for row in info:
        if row[0] == 'day':
            table.field_names = row
        else:
            table.add_row(row)
    table.align = 'l'
print(table)