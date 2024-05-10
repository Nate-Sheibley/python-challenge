import os
import csv

print(os.getcwd())
#Use os.getcwd() to ensure inside of the PyPoll folder
filename = "election_data.csv"
filepath = os.path.join(".", "Resources" , filename)

count_ballots = 0
canidate_dict = {
    "" : {
        "votes" : 0,
        "percent" : 0
        }
    }

with open(filepath,"r") as file:
    csv_reader = csv.reader(file)
    #define header
    header = next(csv_reader)
    for line in csv_reader:
        count_ballots += 1
        canidate = line[2]
        if canidate in canidate_dict:
            canidate_dict[canidate]["votes"] += 1
        else:
            canidate_dict[canidate] = {"votes" : 1}

prev = ""
for canidate in canidate_dict.keys():
    canidate_dict[canidate]["percent"] = round(canidate_dict[canidate]["votes"] / count_ballots, 3)
    winner = canidate if canidate_dict[canidate]["percent"] > canidate_dict[prev]["percent"] else prev
    prev = canidate

# set up strings to be printed and saved
header_str = "Election Results"
spacer = "-------------------------"
ballot_count_str = f'Total Votes: {count_ballots}'
winner_str = f'Winner: {winner}'

def canidates_strs(dict):
    canidate_strs = []
    for canidate in dict.keys():
        if canidate:
            canidate_strs.append([f'{canidate}: {dict[canidate]["percent"]}% ({dict[canidate]["votes"]})'])
    return canidate_strs

#print to terminal
print(header_str)
print(spacer)
print(ballot_count_str)
print(spacer)
for line in canidates_strs(canidate_dict):
    print(line)
print(spacer)
print(winner_str)
print(spacer)

filename = "results.txt"
filepath = os.path.join(".", "analysis", filename)

with open(filepath, "w+") as file:
    csv_writer = csv.writer(file)
    #not very pythonic and very messy wrt scope...
    csv_writer.writerow([header_str])
    csv_writer.writerow([spacer])
    csv_writer.writerow([ballot_count_str])
    csv_writer.writerow([spacer])
    csv_writer.writerows(canidates_strs(canidate_dict))
    csv_writer.writerow([spacer])
    csv_writer.writerow([winner_str])
    csv_writer.writerow([spacer])