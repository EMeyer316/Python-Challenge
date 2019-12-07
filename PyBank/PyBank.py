#Modules
import os
import csv

#To be safe set path for current working directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Set path for file
csvpath = os.path.join ("Resources","budget_data.csv")

# Read the csv and convert it into a list of dictionaries
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')     

    # use of next to skip first title row in csv file
    next(csvreader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Average Revenue Change: $", (avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

with open("Bank.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("-----------------------------------\n")
    text_file.write(f"Total Months: {len(date)}\n")
    text_file.write(f"Total Revenue: ${sum(revenue)}\n")
    text_file.write(f"Average Revenue Change: ${avg_rev_change}\n")
    text_file.write(f"Greatest Increase in Revenue: {max_rev_change_date} (${max_rev_change})\n")
    text_file.write(f"Greatest Decrease in Revenue: {min_rev_change_date} (${min_rev_change})\n")

text_file.close()