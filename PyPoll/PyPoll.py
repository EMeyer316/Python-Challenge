import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

csvpath = os.path.join ("Resources","election_data.csv")

totalvotes = 0
candidates = {}

with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        totalvotes = totalvotes + 1
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print("Election Results")
print("---------------------------------------------------")
print (f"Total Votes: {totalvotes}")
print("---------------------------------------------------")

output_path = os.path.join("PyPoll.txt")

with open(output_path, "w", newline="") as datafile:
    #writer = csv.writer(datafile, delimiter=",")

    datafile.write("Election Results\n")
    datafile.write("---------------------------------------------------\n")
    datafile.write (f"Total Votes: {totalvotes}\n")
    datafile.write("---------------------------------------------------\n")

    largestnumbervotes = 0
    winner = ""

    for candidate in candidates:
        percentvote = (candidates[candidate] / totalvotes) * 100
        print(f"{candidate}: {round(percentvote,3)}% ({candidates[candidate]})")
        datafile.write(f"{candidate}: {round(percentvote,3)}% ({candidates[candidate]})\n")

        if candidates[candidate] > largestnumbervotes:
            largestnumbervotes = candidates[candidate]
            winner = candidate

    print("---------------------------------------------------")
    print(f"Winner: {winner}")

    #print("----", file=datafile) another way to write in python
    datafile.write("---------------------------------------------------\n")
    datafile.write(f"Winner: {winner}")


