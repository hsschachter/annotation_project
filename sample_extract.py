"""
Will save a .cvs file for the first 50 samples.
we then need to annotate and make a .tsv file with

A sample of your data with 50 labels.  
Name this "data.tsv".  
This data should have three tab-separated columns:
data point ID (a unique identifier)
the label
the original text (not tokenized)

"""


import pandas as pd
import random

quotes_file = 'quotes.csv'  
quotes_df = pd.read_csv(quotes_file)

#Randomly sample 50 quotes
sampled_quotes = quotes_df.sample(n=50, random_state=42)

#Assign ID
sampled_quotes['ID'] = range(1, 51)

#Order columns
sampled_quotes = sampled_quotes[['ID', 'Author', 'Quote']]

#Save 50 sampled quotes
output_file = '50_sampled_quotes.csv' 
sampled_quotes.to_csv(output_file, index=False)

print(f'Successfully saved 50 random quotes to {output_file}')