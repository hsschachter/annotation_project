"""
Randomly samples 500 quotes
Adds a unique ID for each row
Adds a blank Label column
Keeps only ID, Quote, and Label
Splits the 500 into two parts of 250 each: label_pt1.tsv and label_pt2.tsv
Saves files in tab-separated format (.tsv)
"""

import pandas as pd



#Load the original quotes
quotes_file = 'quotes.csv'
quotes_df = pd.read_csv(quotes_file)

#Randomly sample 500 quotes
sampled_quotes = quotes_df.sample(n=500, random_state=42).reset_index(drop=True)

#Assign a unique ID
sampled_quotes['ID'] = range(1, 501)

#Add blank Label column
sampled_quotes['Label'] = ''

#Keep only ID, Quote, and Label (reordered)
sampled_quotes = sampled_quotes[['ID', 'Quote', 'Label']]

#Save full 500-sample dataset
sampled_quotes.to_csv('500_sampled_quotes.tsv', sep='\t', index=False)

#Split into two parts of 250 each
pt1 = sampled_quotes.iloc[:250]
pt2 = sampled_quotes.iloc[250:]

pt1.to_csv('label_pt1.tsv', sep='\t', index=False)
pt2.to_csv('label_pt2.tsv', sep='\t', index=False)

print("Successfully saved:")
print("- 500_sampled_quotes.tsv (full set)")
print("- label_pt1.tsv (first 250)")
print("- label_pt2.tsv (second 250)")
