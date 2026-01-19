import pandas as pd
import os

data_folder = './data'
output_file = 'formatted_data.csv'

# 1. Load the three CSV files
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
df_list = []

for file in files:
    file_path = os.path.join(data_folder, file)
    df_list.append(pd.read_csv(file_path))

# Combine them into one large DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# 2. Filter for "Pink Morsel" only
# We remove any row where the product is not a Pink Morsel
pink_morsel_df = combined_df[combined_df['product'] == 'pink morsel'].copy()

# 3. Create the "sales" field
# Sales = price * quantity. We need to clean the price field first (remove '$')
pink_morsel_df['price'] = pink_morsel_df['price'].replace('[\$,]', '', regex=True).astype(float)
pink_morsel_df['sales'] = pink_morsel_df['price'] * pink_morsel_df['quantity']

# 4. Keep only the required fields: Sales, Date, Region
final_df = pink_morsel_df[['sales', 'date', 'region']]

# 5. Export to a single formatted CSV file
final_df.to_csv(output_file, index=False)

print(f"Success! {output_file} has been created.")