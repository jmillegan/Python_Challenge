import os
import csv

#creating the path in order to get the data in the next step
csvpath = os.path.join('C:\\Users\\joeim\\BootCampC\\Python_Challenge\\PyBank\\Resources\\budget_data.csv')
py_bank_txt_path = os.path.join('C:\\Users\\joeim\\BootCampC\\Python_Challenge\\PyBank\\analysis\\Budget_Results.txt')
#create a list to reflect the profits and losses
count = 0 
net = 0
previousrow = 0
changes = []
proloss = previousrow
dates = []
#needed to bring over year with gain and loss in last step
#open csv file imported above
with open(csvpath, 'r') as csvfile: # utf is not really necessary but may work better than not using
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    

#for loop be sure to do all items within it right after each other listing them
#count how many months included 
#net total amount of pro/loss over entire period
#look in second column for the biggest and smallest months
    for row in csvreader:
       count += 1
       net += int(row[1])
       avg = int(row[1]) - previousrow  
       previousrow = int(row[1]) 
       changes.append(avg) 
    # to keep track of the date
       dates.append(row[0])
    #Find the greatest increase in profit   
       greatest_increase = max (changes)
       greatest_index = changes.index (greatest_increase)
       greatest_date = dates[greatest_index]
     #Find the greatest decrease in profit
       greatest_decrease = min (changes)
       greatest_decrease_index = changes.index (greatest_decrease)
       greatest_decrease_date = dates[greatest_decrease_index]
   

#Print each result
changes.pop(0)
print("Financial Analysis")
print("Total Months:", count)
print(f"Total:  ${net}")
print(f"Average Change: ${round(sum(changes)/(count -1),2)}")
print(f"Greatest Increase in Profits: {greatest_date}, (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date}, (${greatest_decrease})")

#Export to folder
with open(py_bank_txt_path, 'w') as txtfile:
   txtfile.write("Financial Analysis \n")
   txtfile.write("-------------------------\n")
   txtfile.write("Total Months:, count \n")

   txtfile.write(f"Total:  ${net}\n")

   txtfile.write(f"Average Change: ${round(sum(changes)/(count -1),2)}\n")
   
   
   txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date}, (${greatest_decrease})\n")     
    



