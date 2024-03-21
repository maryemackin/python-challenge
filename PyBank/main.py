# Import dependencies
import os
import csv

# Set path/file to import/export
budget_data_csv = os.path.join("Resources", "budget_data.csv")
budget_data_analysis_txt = os.path.join("analysis", "budget_data_analysis.txt")

# create variables and set start values if applicable
totalMonths = 0
totalNet = 0

# create empty lists to hold analysis results
netChange = []
monthOfChang = []

# define greatest & least
greatest = ["", 0]
least = ["", 999999999999999999]

# open and read csv file
with open(budget_data_csv) as budgetData:

    # assign csv reader to a variable
    reader = csv.reader(budgetData)

    # read headers
    header = next(reader)

    # set first data row and start point of calculations/counting
    firstRow = next(reader)
    totalNet += int(firstRow[1])

    # confirm code starts on first data row
    print(firstRow)

    # create for loop for calculations/counting
    for row in reader:
        # define for calculations/counting and set data type as integer
        totalNet += int(firstRow[1])
        previousNet = int(firstRow[1])







