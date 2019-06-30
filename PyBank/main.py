import os
import csv

"""budget_data = os.path.join("budget_data.csv")"""

budget_data = os.path.join ("C:\\Users\\Christina\\Documents\\GitHub\\python-challenge\\PyBank\\budget_data.csv")

"""
with open(budget_data, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    first_row = next(csv_reader)    
    print(first_row[0])
    for row in csv_reader:
    totalMonths = totalMonths + 1
    print(str(totalMonths))
print("End of program")
"""
with open(budget_data, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    data = dict()
    flag = False
    plTotal = 0
    totalchange = 0
    greatest = 0
    least = 0
    for row in reader:
        data[row['Date']] = int(row['Profit/Losses'])
        plTotal += int(row['Profit/Losses'])
        if not flag:
            flag = True
            last = float(row['Profit/Losses'])
            change = float(row['Profit/Losses']) - last
            if change > greatest:
                greatest = change
            if change < least:
                least = change
            totalchange += change
            last = float(row['Profit/Losses'])
print("Total Months:", len(data))
print("Total Profit/Losses:", plTotal)
print("Average:", totalchange/len(data))
print("Greatest profit:", greatest)
print("Greatest loss:", least)