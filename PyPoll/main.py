#Python HW#2
import os
import csv

csvpath = os.path.join('raw_data', 'election_data_1.csv')

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
    print("Election Results")
    print("-------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------")

    # Store Candidates and Votes to Dictionary
    PyPoll = {}
    PyPoll_Percent = {}
    for i in range(number_of_candidates):
        PyPoll[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])
        PyPoll_Percent[candidate_list[i]] = candidate_duplicate.count(candidate_list[i])/total_votes
        print(candidate_list[i], ": {0}% ".format(PyPoll_Percent[candidate_list[i]]*100),"(", PyPoll[candidate_list[i]],")" ) 
       


    # # Select the Winner
    print("-------------------")
    print("Winner: ", max(PyPoll))
    print(PyPoll)
