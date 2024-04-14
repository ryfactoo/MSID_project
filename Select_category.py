import pandas as pd

df = pd.read_csv('datebase_yt/merged_all_csv.csv')

selected_rows = df[df['categoryId'].isin([10, 2, 24, 17, 25])]

selected_rows.to_csv('merged_select_category.csv', index=False)