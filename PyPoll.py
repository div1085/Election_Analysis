# data we need to retrive
#1 total number of votes cast
#2 complete list of candidates who received the votes
#3 %age of votes each canadiate received
#4 total number of votes each candidate received
#5 declare winner of electon based on popular vote

# Using the open() function with the "w" mode we will write data to the file.
#outfile=open(file_to_save, "w")

#add data hello world to file
#outfile.write("Hello World")

# Create a filename variable to a direct or indirect path to the file.
##file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Counties in Election\n-------------\nArapahoe\nDenver\nJefferson")

#1 import csv and os module
import csv
import os
#2 Assign a variable for the file to load and the path
file_to_load = os.path.join('Resources','election_results.csv')
#3 Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#4 Initialize a total vote counter
total_votes=0
#5 adding candidates options
candidate_options = []
#6 add empty dictionary for votes received
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    #7 Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #8 Read and print the header row.
    headers = next(file_reader)
    #9 Print each row in csv file
    for row in file_reader:
        # add to the total vote
        total_votes+=1 
        #Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
             # 1 Add it to the list of candidates.
            candidate_options.append(candidate_name)
             # 2. Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # 3 Add a vote to that candidate's count
        candidate_votes[candidate_name]+=1
#save results to text file
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # save final vote count to tet file
    txt_file.write(election_results)
    # Determine the percentage of votes for each candidate by looping through the counts. or each candidate vote_percentage = (votes / total_votes) * 100
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes=candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage=(float(votes)/float(total_votes))*100
        # 4. Print the candidate name and percentage of votes.
        candidate_results=(
            f'{candidate_name}: {vote_percentage:.1f}%  ({votes:,})\n')
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #5 Determine if the vote count that was calculated is greater than the wining count
        if (votes> winning_count) and (vote_percentage>winning_percentage):
            # 2. If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary= (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
