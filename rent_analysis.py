import pandas as pd
from sklearn.metrics import r2_score
import numpy
from sklearn.model_selection import train_test_split

file_path = 'data/assessment_data.pkl'


def preprocess(file_path):
    df = pd.read_pickle(file_path)

    #Check for missing values
    df = df.isnull().sum()

    #Drop rows with missing valiues and place it in a new variable "df_cleaned"
    df =df.dropna()

    #Fill missing values with mean for numerical data and place it ina new variable called df_filled
    df = df.fillna(df.mean())

    #Identify duplicates
    df = df.duplicated().sum()

    return df

def train(file_path):
    df = preprocess(file_path)

    # Split features and target variable
    X = df.drop('target_column', axis=1)  # features
    y = df['target_column']  # target_varible

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    

print(train(file_path))