#In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

#import libraries
import os
import csv

#Create file path
csv_file_path = os.path.join("Resources", "election_data.csv")

# Open csv in read mode
with open(csv_file_path, "r") as election_data:

    # Assign data to csvreader variable
    csvreader = csv.reader(election_data,delimiter=",") 

    #Skip header
    header = next(csvreader)     

    #Declare Variables 
    total_votes = 0 
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    #Iterate through each row in the csv
    for row in csvreader: 

        # Count total_votes
        total_votes = total_votes + 1

        #count each candidates votes check names
        if row[2] == "Khan": 
            khan_votes = khan_votes + 1
        elif row[2] == "Correy":
            correy_votes = correy_votes + 1
        elif row[2] == "Li": 
            li_votes = li_votes + 1
        elif row[2] == "O'Tooley":
            otooley_votes = otooley_votes + 1

#Create candidate list and votes list
candidate_list = ["Khan", "Correy", "Li","O'Tooley"]
votes_list = [khan_votes, correy_votes,li_votes,otooley_votes]

#Create a dictionary for both lists and use the zip method to create a tuple
dict_candidate_votes = dict(zip(candidate_list, votes_list))

#gets the max of the candidate votes using the get method to pullback the value of the specified key
key = max(dict_candidate_votes, key=dict_candidate_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) * 100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f'''

Election Results
=====================================================
Total Votes: {total_votes}
=====================================================
Khan: {khan_percent:.3f}% ({khan_votes})
Correy: {correy_percent:.3f}% ({correy_votes})
Li: {li_percent:.3f}% ({li_votes})
O'Tooley: {otooley_percent:.3f}% ({otooley_votes})
=====================================================
Winner: {key}

''')

# Output files
# Assign output file location and with the pathlib library
output_file = os.path.join("analysis", "Election_Results_Summary.txt")

with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"=====================================================")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"=====================================================")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"=====================================================")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
