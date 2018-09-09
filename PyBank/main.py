import os
import csv

budget_data_path = os.path.join(".","budget_data.csv")

with open(budget_data_path, newline='') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')

    csvheader = next(csvreader)
    # print(csvheader)

    #set count and running total variables beginning with first row of data
    opening_month = next(csvreader)
    months = 1
    current_profit = float(opening_month[1])
    total_net_profit = current_profit

    #set change, greatest increase, and greatest decrease variables to 0 to begin
    total_monthly_change = 0
    greatest_increase_amount = 0
    greatest_increase_month = 'N/A'
    greatest_decrease_amount = 0
    greatest_decrease_month = 'N/A'

    #loop through months of data
    for month in csvreader:
        current_month = month[0]
        #add to month count
        months +=1

        #reset current profit add to profit running total
        previous_profit = current_profit
        current_profit = float(month[1])
        total_net_profit += current_profit

        #add monthly change to running total
        current_monthly_change = current_profit - previous_profit
        total_monthly_change += current_monthly_change

        #determine whether this month's profit should be the greatest increase or decrease
        if current_monthly_change > greatest_increase_amount and current_monthly_change > 0:
            greatest_increase_amount = current_monthly_change
            greatest_increase_month = current_month
        if current_monthly_change < greatest_decrease_amount and current_monthly_change < 0:
            greatest_decrease_amount = current_monthly_change
            greatest_decrease_month = current_month

# print results:
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {months}")
print(f"Total: ${int(total_net_profit)}")
print(f"Average Change: ${round(total_monthly_change / (months-1),2)}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase_amount)})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease_amount)})")
print("------------------------------")
        

#print text file:

output_summary_path = os.path.join(".","budget_summary_output.txt")

with open(output_summary_path,'w',newline='') as summaryoutput:

    summaryoutput.writelines("Financial Analysis\n")
    summaryoutput.writelines("------------------------------\n")
    summaryoutput.writelines(f"Total Months: {months}\n")
    summaryoutput.writelines(f"Total: ${int(total_net_profit)}\n")
    summaryoutput.writelines(f"Average Change: ${round(total_monthly_change / (months-1),2)}\n")
    summaryoutput.writelines(f"Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase_amount)})\n")
    summaryoutput.writelines(f"Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease_amount)})\n")
    summaryoutput.writelines("------------------------------")


    

    
