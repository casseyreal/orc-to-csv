import pyorc
import csv
example = open("./actions_20201208_0001.orc", "rb")
reader = pyorc.Reader(example)
rows = reader.read()
with open('orc.csv', 'w') as out:
    csv_out = csv.writer(out)
    csv_out.writerow(reader.schema.fields.keys())
    csv_out.writerows(rows)