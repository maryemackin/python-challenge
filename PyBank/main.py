# Import dependencies
import os
import csv

# Set path/file to import/export
budget_data_csv = os.path.join("Resources", "budget_data.csv")
budget_data_analysis_txt = os.path.join("analysis", "budget_data_analysis.txt")

#create variables
total_months = 0

# open and read csv file
with open(budget_data_csv) as budget_data:

    # assign csv reader to a variable
    reader = csv.reader(budget_data)

    # read headers
    header = next(reader)

