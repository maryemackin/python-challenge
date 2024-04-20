# Import dependencies
import os
import csv

# Set path/file to import/export: PyPoll\Resources\election_data.csv
election_data_csv = os.path.join(".", "Resources", "election_data.csv")
election_data_analysis_txt = os.path.join(".", "analysis", "election_data_analysis.txt")

# create variables for analysis and set start values & empty lists/dictionaries to hold analysis results

# vote counter
total_votes = 0

# create list of candidates and dictionary to hold names/count votes
candidate_choice = []
candidate_votes = {}

# winner and their vote count
winner = ""
winning_vote_count = 0

# open and read csv file
with open(election_data_csv) as electionData:

    # read file w/csvreader
    reader = csv.reader(electionData)

    # read headers
    header = next(reader)

    # create for loop to count votes
    for row in reader:

        # adding votes to totals
        total_votes = total_votes + 1

        # pull candidate names from each row for analysis
        candidate_name = row[2]

        # create if statement to add candidates to list and count their votes
        if candidate_name not in candidate_choice:

            # add new name to candidates list
            candidate_choice.append(candidate_name)

            # create starting value for all candidates' vote counts
            candidate_votes[candidate_name] = 0
        
        #update vote count with new votes
        candidate_votes[candidate_name] += 1

# results/analysis/write & export in txt file
with open(election_data_analysis_txt, "w") as txt_file:
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    #remove extra lines in output
    print(election_results, end="")

    txt_file.write(election_results)
            
    #get winner stats, write & export to txt file
    for candidate_choice in candidate_votes:
        votes = candidate_votes[candidate_choice]
        vote_percent = float(votes) / float(total_votes) * 100

        if(votes > winning_vote_count):
            winning_vote_count = votes
            winner = candidate_choice
                
        voter_results = f"{candidate_choice}: {vote_percent:.3f}% ({votes})\n"

        print(voter_results, end="")

        txt_file.write(voter_results)

    winner_summary = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"-------------------------\n")
    print(winner_summary)

    txt_file.write(winner_summary)