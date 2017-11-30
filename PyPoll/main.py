#Python HW#2
import os
import csv

output_file = "output/PyPoll_GSu_2.txt"
csvpath = os.path.join('raw_data', 'election_data_2.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    #skip first line
    next(csvfile) 

    # A Complete List of Candidates
    candidate_duplicate = []
    candidate_list = []
    for row in csvreader:
        candidate_duplicate.append(row[2])
    candidate_list = set(candidate_duplicate) #remove duplicates using set properties
    candidate_list = list(candidate_list) #convert to list
    number_of_candidates = len(candidate_list) #number of candidates
    #print(candidate_list)

    #The Total Number of Votes Cast
    total_votes = len(candidate_duplicate)
    # print("Election Results")
    # print("-------------------")
    # print("Total Votes: " + str(total_votes))
    # print("-------------------")

    results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(results, end="")

    # Store Candidates and Votes to Dictionary
    PyPoll = {}
    PyPoll_Percent = {}
    for i in range(number_of_candidates):
        PyPoll[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])
        PyPoll_Percent[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])/total_votes
        #print(candidate_list[i], ": {0}% ".format(PyPoll_Percent[candidate_list[i]]*100),"(", PyPoll[candidate_list[i]],")" ) 
        #voter results
        voter_results = f"{candidate_list[i]}: {PyPoll_Percent[candidate_list[i]]*100:.3f}% ({PyPoll[candidate_list[i]]})\n"
        print(voter_results, end="")
       


    # # Select the Winner
    # print("-------------------")
    # print("Winner: ", max(PyPoll))
    # print(PyPoll)
    winner = (
        f"-------------------------\n"
        f"Winner: {max(PyPoll)}\n"
        f"-------------------------\n")
    print(winner)

with open(output_file, "w") as txt_file:

    # Write Results
    txt_file.write(results)
    # Write Voter Results
    for i in range(number_of_candidates):
        PyPoll[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])
        PyPoll_Percent[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])/total_votes
        #print(candidate_list[i], ": {0}% ".format(PyPoll_Percent[candidate_list[i]]*100),"(", PyPoll[candidate_list[i]],")" ) 
        #voter results
        voter_results = f"{candidate_list[i]}: {PyPoll_Percent[candidate_list[i]]*100:.3f}% ({PyPoll[candidate_list[i]]})\n"
        txt_file.write(voter_results)
    # Write Winner to file
    txt_file.write(winner)
