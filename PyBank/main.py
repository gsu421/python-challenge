#Python HW1
import os
import csv

csvpath = os.path.join('raw_data', 'budget_data_2.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # firstline = csvfile.readline()
    # print(firstline)
    # (isinstance(csvfile.readline(0), str))
    next(csvreader)
    month=[]
    total_rev = 0
    monthly_rev=[]
    #diff=[]

    #  Total Numbr of Months
    for row in csvreader:      
        month.append(row[0])
        # Total Amount of Revenue
        total_rev += float(row[1])
        monthly_rev.append(row[1])    
    total_month = len(month)

    # Put Variance in Dictionary
    
    PyBank_Var = {}
    diff_rev = []
    for i in range(total_month-1):
        diff_rev.append(int(monthly_rev[i+1]) - int(monthly_rev[i]))
        PyBank_Var[month[i+1]] = int(monthly_rev[i+1]) - int(monthly_rev[i])
    #print(PyBank_Var)
    #print(sum(diff_rev))

    # Average Revenue Change
    avg_rev_change = sum(diff_rev) / int(len(month)-1)

    # Get Max Index and Min Index
    max_index = diff_rev.index(max(diff_rev)) + 1
    min_index = diff_rev.index(min(diff_rev)) + 1
    
    print("Financial Analysis")
    print("--------------------------------------")
    print("Total Months: ", len(month))
    print("Total Revenue: ", "$", int(total_rev))
    print("Average Revenue Change: ", "$", int(avg_rev_change))
    print("Greatest Increase in Revenue: ", month[max_index], "($", max(diff_rev), ")")
    print("Greatest Decrease in Revenue: ", month[min_index], "($", min(diff_rev), ")")
    
   
