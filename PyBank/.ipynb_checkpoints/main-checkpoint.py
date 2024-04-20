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
netChangeHolder = []
monthChange = []

# set upper/lower limits for greatest increase/decrease
greatestIncrease = ["", 0]
greatestDecrease = ["", 999999999999999]

# open and read csv file
with open(budget_data_csv) as budgetData:

    # assign csv reader to a variable
    reader = csv.reader(budgetData)

    # read headers
    header = next(reader)

    # set first data row and variables to track totals and changes
    firstRow = next(reader)
    totalNet += int(firstRow[1])
    lastNet = int(firstRow[1])
    totalMonths += 1

    # confirm code starts on first data row
    print(firstRow)

    # create for loop for calculations/counting
    for row in reader:

        # track totals
        totalMonths += 1
        totalNet += int(firstRow[1])

        # track/calculate changes in net
        netChange = int(row[1]) - lastNet
        lastNet = int(row[1])
        netChangeHolder.append(netChange)

        # calculate greatest increase
        if(netChange > greatestIncrease[1]):
            #update depending on findings
            greatestIncrease[0] = row[0]
            greatestIncrease[1] = netChange
        

        # calculate greatest decrease
        if(netChange < greatestDecrease[1]):
            #update depending on findings
            greatestDecrease[0] = row[0]
            greatestDecrease[1]= netChange


# calculate/format data for analysis summary
monthlyAverage = sum(netChangeHolder) / len(netChangeHolder)
averageChange = round(monthlyAverage,2)


# Print the analysis to the terminal to match instructions
analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {totalMonths}\n"
    f"Total: ${totalNet}\n"
    f"Average Change: {averageChange}\n"
    f"Greatest Increase in Profits: {greatestIncrease[0]} ${greatestIncrease[1]}\n"
    f"Greatest Decrease in Profits: {greatestDecrease[0]} ${greatestDecrease[1]}\n")

print(analysis)

# export to text file

budget_data_analysis_txt = os.path.join("analysis", "budget_data_analysis.txt")


# end of code