import os
import csv
import pandas as pd

# Get relative path to access csv
resource_dir = os.getcwd() + "\\PyBank"
budget_csv = os.path.join(resource_dir, "Resources", "budget_data.csv")

# Read the csv
bank_var = pd.read_csv(budget_csv)

#Find total number of unique entries in 'Date' column
nTotalMonths = len(bank_var.Date.unique())
print("Total Months: " + str(nTotalMonths))

#Find sum of the ProfitLosses column
totalPL = bank_var.ProfitLosses.sum()
print("Total: $" + str(totalPL))

sumDiff = 0
i = 0
# Find change between every entry in ProfitLosses
while i < 85:
    sumDiff += (bank_var.ProfitLosses[i+1] - bank_var.ProfitLosses[i])
    i += 1

# Divide by (number of Months - 1) to find avg change
avgDiffRound = round((sumDiff / 85) , 2)
print("Average Change: $" + str(avgDiffRound))

monthlyDiff = []
i = 0
# Create a monhtlyDiff list reflecting each change in ProfitLosses
while i < 85:
    monthlyDiff.append(bank_var.ProfitLosses[i+1] - bank_var.ProfitLosses[i])
    i += 1

# Find highest and lowest values in monthlyDiff list
greatestInc = max(monthlyDiff)
greatestDec = min(monthlyDiff)
print("Greatest Increase in profits: $" + str(greatestInc))
print("Greatest Decrease in profits: $" + str(greatestDec))
