#import modules
import os
import csv

#set paths for input and output files
in_path = os.path.join("Resources","election_data.csv")
#out_path = os.path.join("Analysis","Analysis.txt")

#establish list for appending
votes = []

with open(in_path) as csvfile:
    
    election_reader = csv.reader(csvfile, delimiter=",")

    election_header = next(csvfile)

    for row in election_reader:
        votes.append(row)

#total number of votes cast
total_votes = len(votes)

#pull all candidate names
candidates = []

for x in votes:
    if x not in candidates:
        candidates.append(x)

