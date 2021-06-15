import csv

#to make changes and save as
with open ("uncurated_trkAligands_list.csv", "r") as f:
    with open ("curated_trkAligands_list.csv", "w") as c:
        reader=csv.reader(f)
        writer=csv.writer(c)

for row in reader:
    print(row) #both files have to be open, otherwise I/O error

