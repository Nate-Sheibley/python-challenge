import os
import csv

print(os.getcwd())
#Use os.getcwd() to ensure inside of the PyPoll folder
filename = "election_data.csv"
filepath = os.path.join(".", "Resources" , filename)

count_ballots = 0
# placeholder "" canidate with minimum values
# can be exluded with a truthy if "": check.
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

# placeholder "" canidate so that prev canidate works proerly in the first pass
# supported by default canidate dict values above
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
#generater for canidate strings to be reported.
def canidates_strs(dict):
    for canidate in dict.keys():
        #truthy statement. values for all canidates so long as they are not ""
        if canidate:
            yield [f'{canidate}: {dict[canidate]["percent"]}% ({dict[canidate]["votes"]})']

#print to terminal
print(header_str)
print(spacer)
print(ballot_count_str)
print(spacer)
# was playing around with generators, must include [0] to prevent list syntax printing in the terminal
# did not have to do that with a return list from canidates_strs 
for line in canidates_strs(canidate_dict):
    print(line[0])
print(spacer)
print(winner_str)
print(spacer)

#path to write to
filename = "results.txt"
filepath = os.path.join(".", "analysis", filename)
#write report to analysis path
with open(filepath, "w+") as file:
    csv_writer = csv.writer(file)
    # unsure how to make this more pythonic due to the generator from canidates_strs
    csv_writer.writerows([[header_str], [spacer], [ballot_count_str], [spacer]])
    csv_writer.writerows(canidates_strs(canidate_dict))
    csv_writer.writerows([[spacer], [winner_str], [spacer]])
