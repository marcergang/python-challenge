# Marc Ergang 
#Homework3 - PyPoll
# Import Dependencies
import pandas as pd
import os
# Create a reference to the CSV and import it into a Pandas DataFrame
election_data = os.path.join(".", "election_data.csv")
election_pd = pd.read_csv(election_data)
#Get Overall total of votes
ttl_votes = len(election_pd)
#Set index to candidate
elect_pd = election_pd.set_index("Candidate")
#Get candidate groupby count and make new column
vote_group= elect_pd.groupby(["Candidate"]).size().reset_index(name='counts')
#Reset Candidate to index 
vote_group_ttl = vote_group.set_index("Candidate")
#Use loc to get make each candidate vote count a variable
correy_ttl = vote_group_ttl.loc["Correy", "counts"]
khan_ttl = vote_group_ttl.loc["Khan", "counts"]
li_ttl = vote_group_ttl.loc["Li", "counts"]
otooley_ttl = vote_group_ttl.loc["O'Tooley", "counts"]
#Get the % of votes by candidate
correy_percentage =(correy_ttl / ttl_votes)
khan_percentage =(khan_ttl/ ttl_votes)
li_percentage =(li_ttl/ ttl_votes)
otooley_percentage =(otooley_ttl/ ttl_votes)
#Find the winner
winner = vote_group_ttl.max()
#Print analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {ttl_votes}")
print("-------------------------")
print(f"Khan: {'{:.3%}'.format(khan_percentage)} {khan_ttl}")
print(f"Correy: {'{:.3%}'.format(correy_percentage)} {correy_ttl}")
print(f"Li: {'{:.3%}'.format(li_percentage)} {li_ttl}")
print(f"O’Tooley: {'{:.3%}'.format(otooley_percentage)} {otooley_ttl}")
print("-------------------------")
print(f"Winner is: Khan {winner}")
print("-------------------------")
#Output results to txt
file=open('Mergang_hw3.txt','a')
file.write("Election Results")
file.write("\n-------------------------")
file.write(f"\nTotal Votes: {ttl_votes}")
file.write("\n-------------------------")
file.write(f"\nKhan: {'{:.3%}'.format(khan_percentage)} {khan_ttl}")
file.write(f"\nCorrey: {'{:.3%}'.format(correy_percentage)} {correy_ttl}")
file.write(f"\nLi: {'{:.3%}'.format(li_percentage)} {li_ttl}")
file.write(f"\nO’Tooley: {'{:.3%}'.format(otooley_percentage)} {otooley_ttl}")
file.write("\n-------------------------")
file.write(f"\nWinner is: Khan {winner}")
file.write("\n-------------------------")
file.close()

