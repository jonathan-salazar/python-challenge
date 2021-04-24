# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
# You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. 
# (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:

#Imports
import os
import csv

#Open the file using the file path
budget_data = os.path.join("Resources", "budget_data.csv")

#budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data, "r") as csv_file:

    #Split data by comma
    csv_reader = csv.reader(csv_file, delimiter=",") 

    #Skip the header
    header = next(csv_reader)

    #Create lists
    total_months = []
    total_profit = []
    monthly_change = []

    for row in csv_reader:
        
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_change.append(total_profit[i+1]-total_profit[i])
        
    
# The total number of months included in the dataset
month_count = len(total_months)

# The net total amount of "Profit/Losses" over the entire period
net_total = sum(total_profit)

total_changes = sum(monthly_change)
changes_month_count = len(monthly_change)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
avg_change = total_changes / changes_month_count

#The greatest increase in profits (date and amount) over the entire period
MAX_CHANGE = max(monthly_change)
MAX_MONTH_CHANGE = monthly_change.index(MAX_CHANGE) + 1

#The greatest decrease in losses (date and amount) over the entire period
MIN_CHANGE = min(monthly_change) 
MIN_MONTH_CHANGE = monthly_change.index(MIN_CHANGE) + 1
   
#Summary
print(f''' 

Financial Analysis
==========================================
Total Months: {month_count} 
Net Total : {net_total}
Average Change: {round(avg_change, 2)}
Greatest Increase: {total_months[MAX_MONTH_CHANGE]} ${MAX_CHANGE}
Greates Decrease: {total_months[MIN_MONTH_CHANGE]} ${MIN_CHANGE}      

''')


    
#Output files
output_file = os.path.join("analysis", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("=======================================")
    file.write("\n")
    file.write(f"Total Months: {month_count}")
    file.write("\n")
    file.write(f"Total: ${net_total}")
    file.write("\n")
    file.write(f"Average Change: {round(avg_change, 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[MAX_MONTH_CHANGE]} (${(str(MAX_CHANGE))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[MIN_MONTH_CHANGE]} (${(str(MIN_CHANGE))})")
        


