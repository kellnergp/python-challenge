#import basic modules
import os
import csv

#set path to data .csv file
input_path = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("Analysis", "Analyis.txt")

months = []
profits = []

with open(input_path) as csvfile:
    budget_reader = csv.reader(csvfile)

#pull out header row
    budget_header = next(csvfile)

#set lists for each column
    for row in budget_reader:
        months.append(row[0])
        profits.append(row[1])

#use len function to count months
num_months = len(months)

#convert profits to integers and sum
profits =[int(i) for i in profits]
total_profits = sum(profits)

change_profits = []
indexval = [*range(1, len(profits))]

#profit change = current month - previous month, so the first month doesn't have a value
for value in indexval:
    change_profits.append(profits[value] - profits[value-1])

#calculate arithmetic mean
ave_change = sum(change_profits) / len(change_profits)
round_ave = str(round(ave_change,2))

#use native functions to find min and max values
max_change = max(change_profits)
min_change = min(change_profits)

max_month = []
min_month = []

change_index = [*range(0, len(change_profits))]

#use loop and conditionals to find months for greatest increase and decrease in profit
#convert index value from change_profits back to index value of the input data
for val in change_index:
    if change_profits[val] == max_change:
        max_month.append(months[val + 1])
    if change_profits[val] == min_change:
        min_month.append(months[val + 1])

#print analysis values to terminal
line1 = f"Financial Analysis"
line2 = f"------------------------------"
line3 = f"Total Months: {num_months}"
line4 = f"Total: ${total_profits}"
line5 = f"Average Change: ${round_ave}"
line6 = f"Greatest Increase in Profits: {max_month} (${max_change})"
line7 = f"Greatest Decrease in Profits: {min_month} (${min_change})"

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)
print(line6)
print(line7)

#write analysis to text file
with open(output_path,'w') as out:
    out.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
