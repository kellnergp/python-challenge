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
        votes.append(row[2])

#total number of votes cast
total_votes = len(votes)

#pull all candidate names
candidates = []

for x in votes:
    if x not in candidates:
        candidates.append(x)

cand_index = [*range(0, len(candidates))]

#create array for vote counts
vote_counts = []

for name in candidates:
    vote_counts.append(0)

#count votes for each candidate with loop and conditionals
for vote in votes:
    for choice in cand_index:
        if vote == candidates[choice]:
            vote_counts[choice] += 1

#calculate percentage of total votes received by each candidate
percentages = [round((100*(countvalue/total_votes)),3) for countvalue in vote_counts]

#determine the winner
winner_count = max(vote_counts)

for value in cand_index:
    if vote_counts[value] == winner_count:
        winner = candidates[value]

#generate strings for analysis printout
line1 = f"Election Results"
linedash = f"-------------------------"
linetotal = f"Total Votes: {total_votes}"
linewinner = f"Winner: {winner}"
lineresults = []

for value in cand_index:
    lineresults.append(f"{candidates[value]}: {percentages[value]}% ({vote_counts[value]})")

#print analysis to terminal
print(line1)
print(linedash)
print(linetotal)
print(linedash)
for value in cand_index:
    print(lineresults[value])
print(linedash)
print(linewinner)
print(linedash)