import os
import csv

election_data_path = os.path.join(".","election_data.csv")

with open(election_data_path,newline='') as electionfile:
    csvreader = csv.reader(electionfile,delimiter=',')

    csvheader = next(csvreader)
    # print(csvheader)

    #set count and candidate lists based on first row of data
    first_vote = next(csvreader)
    total_vote_count = 1
    candidates = [first_vote[2]]
    votes_won = [1]

    #loop through votes to collect all candidates and how many votes they won
    for vote in csvreader:
        total_vote_count += 1
        current_candidate = vote[2]

        #if candidate is already in candidates list, add this vote to their running total
        if current_candidate in candidates:
            candidate_index = candidates.index(current_candidate)
            votes_won[candidate_index] += 1
        #otherwise, add this candidate to the list and give them 1 vote
        else:
            candidates.append(current_candidate)
            votes_won.append(1)

#calculate percentages for each candidate
percentages_won = []

for candidate in candidates:
    candidate_index = candidates.index(candidate)
    candidate_votes = votes_won[candidate_index]
    win_percentage = round(candidate_votes / total_vote_count * 100,3)
    percentages_won.append(win_percentage)

#determine winner by looping through percentages won
highest_percentage = 0
winnter = 'n/a'

for percent in percentages_won:
    if percent > highest_percentage:
        highest_percentage = percent
        percent_index = percentages_won.index(percent)
        winner = candidates[percent_index]

#print results to terminal
print("Election Results")
print("------------------------------")
print(f"Total Votes: {total_vote_count}")
print("------------------------------")
for candidate in candidates:
    candidate_index = candidates.index(candidate)
    candidate_percent = percentages_won[candidate_index]
    candidate_votes = votes_won[candidate_index]
    print(f"{candidate}: {candidate_percent}% ({candidate_votes})")
print("------------------------------")
print(f"Winner: {winner}")
print("------------------------------")

#print text file
output_summary_path = os.path.join(".","election_summary_output.txt")

with open(output_summary_path,'w',newline='') as summaryoutput:

    summaryoutput.writelines("Election Results\n")
    summaryoutput.writelines("------------------------------\n")
    summaryoutput.writelines(f"Total Votes: {total_vote_count}\n")
    summaryoutput.writelines("------------------------------\n")
    for candidate in candidates:
        candidate_index = candidates.index(candidate)
        candidate_percent = percentages_won[candidate_index]
        candidate_votes = votes_won[candidate_index]
        summaryoutput.writelines(f"{candidate}: {candidate_percent}% ({candidate_votes})\n")
    summaryoutput.writelines("------------------------------\n")
    summaryoutput.writelines(f"Winner: {winner}\n")
    summaryoutput.writelines("------------------------------\n")