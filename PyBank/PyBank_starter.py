# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_chng_list=[]
mon_chng_list=[]
last_profit_loss = 0
greatest_increase_mon = ""
greatest_increase = 0
greatest_decrease_mon = ""
greatest_decrease = 0
# Open and read the csv
with open(file_to_load) as financial_data:
	reader = csv.reader(financial_data)

	# Skip the header row
	header = next(reader)

	# Extract first row to avoid appending to net_change_list
	row_one=next(reader)

	# Track the total and net change
	total_months +=1
	total_net += int(row_one[1])
	last_profit_loss = int(row_one[1])

	# Process each row of data
	for row in reader:

		# Track the total
		total_months+= 1
		total_net+= int(row[1])

		# Track the net change
		net_chng = int(row[1]) - last_profit_loss
		last_profit_loss = int(row[1])
		net_chng_list.append(net_chng)
		mon_chng_list.append(row[0])


		# Calculate the greatest increase in profits (month and amount)
		if net_chng > greatest_increase :
			greatest_increase = net_chng
			greatest_increase_mon = row[0]

		# Calculate the greatest decrease in losses (month and amount)
		if net_chng > greatest_decrease :
			greatest_decrease = net_chng
			greatest_decrease_mon = row[0]


# Calculate the average net change across the months
avg_chng = sum(net_chng_list) / len(net_chng_list)


# Generate the output summary
output = (
	f"Financial Analysis\n"
	f"----------------------------\n"
	f"Total Months: {total_months}\n"
	f"Total: ${total_net}\n"
	f"Average Change: ${avg_chng:.2f}\n"
	f"Greatest Increase in Profits:{greatest_increase_mon} (${greatest_increase}) \n"
	f"Greatest Decrease in Profits:{greatest_decrease_mon} (${greatest_decrease}) \n"
	)

# Print the output
print(output)

# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
	#txt_file.write(output)