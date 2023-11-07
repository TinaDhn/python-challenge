import os
import csv


election_data_path=os.path.join('Resources','election_data.csv')

total_votes=0
vote_1=0
vote_2=0
vote_3=0


with open(election_data_path, 'r') as csvfile:
    csvreader =csv.reader(csvfile , delimiter=",")
    header = next(csvreader)
    for row in csvreader:
     total_votes+=1 
     if row[2]=="Charles Casper Stockham":
        vote_1+=1
     elif row[2]=="Diana DeGette":
      vote_2+=1
     elif row[2]=="Raymon Anthony Doane":
      vote_3+=1



count1=vote_1
count2=vote_2
count3=vote_3
votes = [vote_1, vote_2, vote_3]   

rate1=round(count1/total_votes * 100,3)
rate2=round(count2/total_votes * 100,3)
rate3=round(count3/total_votes * 100,3)

vote_person=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
vote_rate=[rate1,rate2,rate3]
vote_count=[count1,count2,count3]
maximun_rate=max(vote_rate)

winner_index = vote_count.index(max(vote_count))   
winner = vote_person[winner_index]                 


conclusion = list([rate1, rate2, rate3])

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
   
for i in range(len(vote_person)):
        print(f'{vote_person[i]}: {conclusion[i]} % ({votes[i]})')

print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

output_file=os.path.join("analysis","election_analysis.txt")

with open(output_file,"w",newline='') as datafile:
    writer=csv.writer(datafile)
    writer.writerow(['Election Results'])
    writer.writerow(['-------------------------'])
    writer.writerow([f'Total Votes: {total_votes}'])
    writer.writerow([f'-------------------------'])
    for i in range(len(vote_person)):
        writer.writerow([f'{vote_person[i]}: {conclusion[i]} % ({votes[i]})'])
    writer.writerow([f'-------------------------'])
    writer.writerow([f'Winner: {winner}'])




