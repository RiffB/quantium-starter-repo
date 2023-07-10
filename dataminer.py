import csv
import os

directory = 'data'
outputfilepath = 'pink_morsels_output.csv'
fieldnames = ['sales', 'date', 'region']

with open (outputfilepath,'a', newline='') as outputfiledata:
    writer = csv.DictWriter(outputfiledata, delimiter=',', fieldnames=fieldnames)
    writer.writeheader()

    for inputfilename in os.listdir(directory):
        inputfilepath = os.path.join(directory, inputfilename)

        with open(inputfilepath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                if row['product'] == 'pink morsel':
                    sales = '$'+ str(float(row['price'][1:]) * int(row['quantity']))
                    writer.writerow({'sales': sales, 'date': row['date'], 'region': row['region']})

