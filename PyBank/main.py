import os
import csv


budget_data_path=os.path.join('Resources','budget_data.csv')

Date=[]
Profit=[]


with open(budget_data_path, 'r') as csvfile:
    csvreader =csv.reader(csvfile , delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        Date.append(row[0])
        Profit.append(int(row[1]))
 

    print("Financial Analysis")
    print("-------------------------")
    total_months=len(Date)
    print(f'Total Months: {total_months}')
    total_price=sum(Profit)
    print(f'Total:$ {total_price}')


changes=[]


for i in range(0,(int(total_months)-1)):
    row_change=(Profit[i+1])-(Profit[i])
    changes.append(row_change)


total_average=round(sum(changes)/len(changes),2)
print(f'Average Change:$ {total_average}')


Greatest_increase=max(changes)
Greatest_increase_Date=Date[changes.index(Greatest_increase)+1]
print(f'Greatest Increase in Profits: {Greatest_increase_Date} (${Greatest_increase})')


Greatest_decrease=min(changes)

Greatest_decrease_Date=Date[changes.index(Greatest_decrease)+1]
print(f'Greatest Decrease in Profits: {Greatest_decrease_Date} (${Greatest_decrease})')


output_path= os.path.join("analysis","financial_analysis.txt")
with open(output_path , "w") as datafile:
 datafile.write(f'Financial Analysis\n')
 datafile.write(f'-------------------------\n')
 datafile.write(f'Total Months: {total_months}\n')
 datafile.write(f'Total:$ {total_price}\n')
 datafile.write(f'Average Change:$ {total_average}\n')
 datafile.write(f'Greatest_Increase in Profits: {Greatest_increase_Date} (${Greatest_increase})\n')
 datafile.write(f'Greatest_Increase in Profits: {Greatest_decrease_Date} (${Greatest_decrease})\n') 
