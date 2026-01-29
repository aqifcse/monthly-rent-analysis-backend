import pandas as pd

file_path = 'assessment_data.pkl'

df = pd.read_pickle(file_path)

print(df.columns)