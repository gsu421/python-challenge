
# coding: utf-8

# In[75]:


# Import required packages
import os
import csv
import datetime

file_to_load = os.path.join('raw_data/employee_data1.csv')
file_to_output = os.path.join('analysis/employee_data_reformatted1.csv')


# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load, newline = '') as emp_data:
    reader = csv.DictReader(emp_data, delimiter = ',')

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:
#         print(row['Name'])

        # Grab emp_ids and store it into a list
        emp_ids.append(row["Emp ID"])

        # Grab names, split them, and store them in a temporary variable
        split_name = row["Name"].split(" ")

        # Then save first and last name in separate lists
        emp_first_names.append(split_name[0])
        emp_last_names.append(split_name[1])

        # Grab DOB and reformat it
        reformatted_dob = datetime.datetime.strptime(row['DOB'], '%Y-%m-%d')
#         print(reformatted_dob)
        reformatted_dob = reformatted_dob.strftime("%m/%d/%Y")
#         print(reformatted_dob)
        # Then store it into a list
        emp_dobs.append(reformatted_dob)

        # Grab SSN and reformat it
        split_ssn = list(row["SSN"])
        split_ssn[0:3] = ("*", "*", "*")
        split_ssn[4:6] = ("*", "*")
        joined_ssn = "".join(split_ssn)

        # Then store it into a list
        emp_ssns.append(joined_ssn)

        # Grab the states and use the dictionary to find the replacement
        state_abbrev = us_state_abbrev[row["State"]]

        # Then store the abbreviation into a list
        emp_states.append(state_abbrev)

# Zip all of the new lists together
empdb = zip(emp_ids, emp_first_names, emp_last_names,
            emp_dobs, emp_ssns, emp_states)

# Write all of the election data to csv
with open(file_to_output, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp ID", "First Name", "Last Name",
                     "DOB", "SSN", "State"])
    writer.writerows(empdb)

