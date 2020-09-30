# Import the OS module
# This will allow us to create file paths across operating systems
import os

# Module for opening & reading CSV files
import csv

election_data_csvpath = os.path.join("Resources", "election_data.csv")

# Define variables
total_votes = 0
total_candidates = 0
candidate_votes = 0


# Define lists
candidate_options = [0, 0, 0, 0]
votes = []
vote_percentages = [0, 0, 0, 0]
winner = []

# Read election_data.csv file
with open(election_data_csvpath) as csv_file:

    csvreader = csv.reader(csv_file, delimiter = ',')

    # Reads header row first
    csv_header = next(csvreader)

# The total number of votes cast
    for row in csvreader:
        total_votes = total_votes + 1
        
        total_candidates = row[2]        

# A complete list of candidates who received votes

        if total_candidates in candidate_options:
            candidate_index = candidate_options.index(total_candidates)
            votes[candidate_index] = votes[candidate_index] + 1
        else:
            candidate_options.append(total_candidates)
            votes.append(1)

# The percentage of votes each candidate won
vote_percentages[0] = round(100 * (candidate_options[0] / total_votes), 3)
vote_percentages[1] = round(100 * (candidate_options[1] / total_votes), 3)
vote_percentages[2] = round(100 * (candidate_options[2] / total_votes), 3)
vote_percentages[3] = round(100 * (candidate_options[3] / total_votes), 3)

# The total number of votes each candidate won


# The winner of the election based on popular vote.


print(f"Election Results")
print(f"-------------------------")

print(f"Total Votes: {total_votes}\n")
print(f"-------------------------")

print(f"{candidate_index[0]}: {vote_percentages[0]}%")
print(f"{candidate_index[1]}: {vote_percentages[1]}%")
print(f"{candidate_index[2]}: {vote_percentages[2]}%")
print(f"{candidate_index[3]}: {vote_percentages[3]}%")

print(f"-------------------------")
#print(f"Winner: {winner}")
print(f"-------------------------")
