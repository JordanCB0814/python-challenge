#Our Dependencies
import csv
import os

#Results we want to achieve
#Financial Analysis
#----------------------------
#Total Months:____
#Total: $_________
#Average Change: $___________
#Greatest Increase in Profits: Month-day ($_______)
#Greatest Decrease in Profits: Month-day ($_________)

#Files we load/send our data to or from
file_to_load = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join(".", "budget_analysis.txt")

#Setting our results to 0
total_months = 0
total = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
total_networth = 0
net_change_tracker = []
month_changes = {}
greatest = ["", 0]
least = ["", 99999999999]

#Read the csv to make a list formating
with open(file_to_load) as financial_data:

    reader = csv.reader(financial_data)

    #This part reads the header row of budget_data.csv
    header = next(reader)
    
    #grab then print our first row of the data set
    first_row = next(reader)

    #Placing our results/Calculations
    for row in reader:
        total_months += 1
        #Calculate total networth in the data set
        total_networth += int(first_row[1])
        #Record the previous networth grabbed
        previous_net = int(first_row[1])

        #Tracking the network change
        net_change = int(row[1]) - previous_net
        previous_net = int(first_row[1])
        net_change_tracker.append(net_change)

        #Calculating the greatest increase
        if (net_change > greatest [1]):
            greatest[0] = row[0]
            greatest[1] = net_change

        #Calculate the greatest decrease
        if (net_change < least [1]):
            least[0] = row[0]
            least[1] = net_change

        

#Average of our network change calculation
net_change_average = sum (net_change_tracker) / len(net_change_tracker)
        
#Mapping out our results
final_analysis =(
    f"Financial Analysis\n"
    f"-------------------\n"
    f"Total Months:{total_months}\n"
    f"Total Networth:${total_networth}\n"
    f"Average Change:${net_change_average:.2f}\n"
    f"Greatest Increase in Profits:{greatest[0]} ${greatest[1]}\n"
    f"Greatest Decrease on Profits:{least[0]} ${least[1]}\n"
)
    
        
print(final_analysis)


#Creating a text file to output the code
with open(file_to_output, "w") as txt_file:
    txt_file.write(final_analysis)



