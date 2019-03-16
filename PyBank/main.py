import os
import pandas as pd
import numpy as np
#import file and open with pandas
budget_data = os.path.join( ".", "budget_data.csv")
budget_df = pd.read_csv(budget_data)
#Rename Profit/Losses Column
budget_rename_df = budget_df.rename(columns={"Date": "Date", "Profit/Losses": "pl"})
#Finds total number of Months
Months = len(budget_rename_df)
#Finds the total of the PandL column
pl_ttl = budget_rename_df["pl"].sum()
#Finds the month to month difference of the PandL column
monthly_change = budget_rename_df["pl"].diff()
#Create a new column with the difference of PandL column
budget_rename_df["monthly_change"] = monthly_change
#Find the Avg of the MonthlyChange
mon_ch_avg = budget_rename_df["monthly_change"].mean()
#Finds the max of the MonthlyChange column
mon_ch_max = budget_rename_df['monthly_change'].max()
#FInds the min of the MonthlyChange column
mon_ch_min = budget_rename_df['monthly_change'].min()
#Set Index to MonthlyChange
budget_df = budget_rename_df.set_index("monthly_change")
#Find date of greatest increase
mon_max_date = budget_df.loc[1926159.0, "Date"]
#Find date of the greatest decrease
mon_min_date = budget_df.loc[-2196167.0, "Date"]

#Print Analysis
print("Financial Analysis")
print("-------------------")
print(f"Total Months: {Months}")
print(f"Total: ${pl_ttl}")
print(f"Average Change: ${mon_ch_avg}")
print(f"Greatest Increase: {mon_max_date} ${mon_ch_max}")
print(f"Greatest Decrease: {mon_min_date} ${mon_ch_min}")


