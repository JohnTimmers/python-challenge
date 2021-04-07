import os
import csv
import pandas as pd

# Get relative path to access csv
resource_dir = os.getcwd() + "\\PyPoll"
election_csv = os.path.join(resource_dir, "Resources", "election_data.csv")

# Read the csv
voter_var = pd.read_csv(election_csv)

# Find the total number of (unique) voters/entries in VoterID column
totalVotes = len(voter_var.VoterID.unique())
print("\n\tTOTAL VOTES: "+ str(totalVotes) + "\n")

# Find total number of votes per candidate
results = voter_var.Candidate.value_counts()

candidates = []
wonVotes = []
pctVotes = []

# Iterate through 'results' to return each candidate name, how many total votes they got, and what percentage of votes they got
for i in range(4):
    candidates.append(results.index[i])
    wonVotes.append(results[i])
    pctVotes.append(str(int((wonVotes[i]/totalVotes)*100)) + "%")

# Reflect above values as a DataFrame, and add an axis label of "Candidate"
resultsDF2 = pd.DataFrame({"     Percent of Vote" : pctVotes, "     Number of Votes" : wonVotes}, candidates)
resultsDF2 = resultsDF2.rename_axis("Candidate")

print(resultsDF2)

print("\n\tWINNER : " + candidates[0] + "\n")