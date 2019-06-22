import os
import csv
"""
with open("C:\\Users\\Christina\\Desktop\\SMU_New\\SMUDAL201905DATA5\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    data = dict()
    candidates = []
    for row in reader:
        if row ["Candidate"] not in candidates:
            candidates.append(row["Candidate"])
        data[row['Voter ID']] = [row['County'], row['Candidate']]
print("Total Number of Voters:", len(data))
print("Candidates:", candidates)
"""
with open("C:\\Users\\Christina\\Desktop\\SMU_New\\SMUDAL201905DATA5\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    
    totalVotes = 0
   
    candidates = dict()
    for row in reader:
        totalVotes += 1
        if row["Candidate"] not in candidates:
            candidates[row["Candidate"]] = 1
        else:
            candidates[row["Candidate"]] += 1
print("Total Number of Voters: ", totalVotes)
print("Candidates:", candidates.keys())
for key, value in candidates.items():
    print(key + ": " + str((value / totalVotes) * 100) + "% (" + str(value) + ")")