# Import dependencies
import os
import csv

# Set path/file to import/export
election_data_csv = os.path.join("Resources", "election_data.csv")
election_data_analysis_txt = os.path.join("analysis", "election_data_analysis.txt")

# create variables for analysis and set start values & empty lists/dictionaries to hold analysis results
totalVotes = 0
candidates = []
candidateVotes = {}
winner = ""
winningVoteTotals = 0

# open and read csv file
with open(election_data_csv) as electionData:

    # assign csv reader to a variable
    reader = csv.reader(electionData)

    # read headers
    header = next(reader)

    # create for loop to count votes
    for row in reader:

        totalVotes = totalVotes + 1



# results/analysis
electionFinalResults = (f"Election Results\n"
                        f"-------------------------\n"
                        f"Total Votes: {totalVotes}\n"
                        f"-------------------------\n"


# export analysis as a text file
with open(election_data_analysis_txt, "w") as txt_file:
    txt_file.write("election_data_analysis.txt")
    
    
