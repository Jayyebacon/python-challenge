# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Modules:HW", "3", "python-challenge", "PyPoll", "Resources", "election_data.csv")
file_to_output = os.path.join("Modules:HW", "3", "python-challenge", "PyPoll", "analysis", "election_analysis.txt")

# Initialize variables
total_votes = 0
candidate_list = []                 # Tracks unique candidates
candidate_votes = {}               # Tracks vote count per candidate
winning_candidate = ""
winning_votes = 0

# Read the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)

    for row in reader:
        total_votes += 1
        candidate_name = row[2]     # Index 2 for candidate name in election_data.csv

        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1

# Prepare results
results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    if votes > winning_votes:
        winning_votes = votes
        winning_candidate = candidate

results.append("-------------------------")
results.append(f"Winner: {winning_candidate}")
results.append("-------------------------")

# Print results
for line in results:
    print(line)

# Save to file
with open(file_to_output, "w") as txt_file:
    for line in results:
        txt_file.write(line + "\n")

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
