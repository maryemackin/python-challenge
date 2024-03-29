# Import dependencies
import os
import csv

# Set path/file to import/export
election_data_csv = os.path.join("Resources", "election_data.csv")
election_data_analysis_txt = os.path.join("analysis", "election_data_analysis.txt")

# create variables for analysis and set start values & empty lists/dictionaries to hold analysis results

# total vote counter
totalVotes = 0

# create list of candidates and dictionary to hold names/count votes
candidates = []
candidateVotes = {}

# winner and their vote count
winningVoteTotals = 0
winner = ""


# open and read csv file
with open(election_data_csv) as electionData:

    # assign csv reader to a variable
    reader = csv.reader(electionData)

    # read headers
    header = next(reader)

    # create for loop to count votes
    for row in reader:

        # adding votes to totals
        totalVotes = totalVotes + 1

        # pull candidate names from each row for analysis
        candidateName = row[2]

        # create if statement to add candidates to list and count their votes
        if candidateName not in candidates:

            # add new name to candidates list
            candidates.append(candidateName)

            # create starting value for all candidates' vote counts
            candidateVotes[candidateName] = 0
        
        # update vote count with new votes
        candidateVotes[candidateName] += 1

        # results/analysis
        with open(election_data_analysis_txt, "w") as txt_file:
            electionAnalysis = (
                f"Election Results\n"
                f"-------------------------\n"
                f"Total Votes: {totalVotes}\n"
                f"-------------------------\n"
            )

            print(electionAnalysis, end="")

            txt_file.write(electionAnalysis)

            for candidate in candidateVotes:

                votes = candidateVotes[candidates]
                votePercent = float(votes) / float(totalVotes) * 100

                if(votes > winningVoteTotals):

                    winningVoteTotal = votes
                    winner = candidate
                
                electionFinal = (f"{candidate}: {votePercent:.3f}% ({votes})\n")

                print(electionFinal, end="")

                txt_file.write(electionAnalysis)
            
            electionSummary = (                
                f"{electionFinal}"
                f"-------------------------\n"
                f"Winner: {winner}\n"
                f"-------------------------\n"
            )

            print(electionSummary)

            txt_file.write(electionSummary)
            