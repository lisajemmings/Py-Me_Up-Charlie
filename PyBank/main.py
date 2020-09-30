# Import the OS module
# This will allow us to create file paths across operating systems
import os

# Module for opening & reading CSV files
import csv

budget_data_csvpath = os.path.join("Resources", "budget_data.csv")

# Define variables
month_count = 0
net_profit = 0
monthly_profit_change = 0
previous_month_profit = 0

# Define lists
monthly_profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", -1]

# Read budget_data.csv file
with open(budget_data_csvpath) as csv_file:

    csvreader = csv.reader(csv_file, delimiter = ',')

    # Reads header row first
    csv_header = next(csvreader)

# The total number of months included in the dataset
    for row in csvreader:
        month_count = month_count + 1

# The net total amount of "Profit/Losses" over the entire period
        net_profit = net_profit + int(row[1])

# The average of the changes in "Profit/Losses" over the entire period
        monthly_profit_change = int(row[1]) - previous_month_profit
        previous_month_profit = int(row[1])

        if month_count > 1:
            monthly_profit_changes.append(monthly_profit_change)
            average_monthly_change = sum(monthly_profit_changes) / len(monthly_profit_changes)

# The greatest increase in profits (date and amount) over the entire period
        if monthly_profit_change > greatest_increase[1]:
            greatest_increase[1] = monthly_profit_change
            greatest_increase[0] = row[0]

# The greatest decrease in losses (date and amount) over the entire period
        if monthly_profit_change < greatest_decrease[1]:
            greatest_decrease[1] = monthly_profit_change
            greatest_decrease[0] = row[0]

average_monthly_change = str(round(average_monthly_change, 3))


print(f"Financial Analysis")
print(f"----------------------------")

print(f"Total Months: {month_count}\n")
print(f"Total: ${net_profit}\n")
print(f"Average Change: ${average_monthly_change}\n")
print(f"Greatest Increase in Profits: {greatest_increase[0]} $({greatest_increase[1]})\n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} $({greatest_decrease[1]})\n")