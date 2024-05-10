 
import os
import csv

#ensure the current working directory (os.getcwd())
# is in the PyBank directory, where this file is launched from.

filename = "budget_data.csv"
filepath = os.path.join(".", "Resources", filename)

month_counter = 0
net_total = 0
changes = []
max_change = ("date", 0)
min_change = ("date", 0)

with open(filepath, "r") as file:
    csv_reader = csv.reader(file, delimiter=',')
    #skip header
    header = next(csv_reader)
    change = None
    prev = None

    for line in csv_reader:
        profit_loss = int(line[1])

        # exactly 1 line per month
        month_counter += 1

        net_total += profit_loss

        if isinstance(prev, int):
            change = profit_loss - prev
            changes.append(change)
            max_change = (line[0], change) if max_change[1] < change else max_change
            min_change = (line[0], change) if min_change[1] > change else min_change
        prev = profit_loss

average_change = round(sum(changes) / len(changes),2)

header = "Financial Analysis"
separator = "----------------------------"
months_str = f"Total Months: {month_counter}"
net_total_str = f"Total: ${net_total}"
ave_change_str = f"Average Change: ${average_change}"
max_change_str = f"Greatest Increase in Profits: {max_change[0]} (${max_change[1]})"
min_change_str = f"Greatest Decrease in Profits: {min_change[0]} (${min_change[1]})"

print(header)
print(separator)
print(months_str)
print(net_total_str)
print(ave_change_str)
print(max_change_str)
print(min_change_str)

filename = "report.txt"
filepath = os.path.join(".", "analysis", filename)

with open(filepath, "w+") as report:
    csv_writer = csv.writer(report)
    csv_writer.writerows([[header], [separator], [months_str], [net_total_str], [ave_change_str], [max_change_str], [min_change_str]])

