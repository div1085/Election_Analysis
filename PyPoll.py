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

#4 Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    #6 Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
     


#5 Close the file
