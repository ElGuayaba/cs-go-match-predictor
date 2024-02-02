# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Dataset
total_data = pd.read_csv('../data/interim/team_data.csv')
total_data.shape

# Input params have to be list-like
def transform_input(team1, team2):
    team1 = np.array(team1)
    team2 = np.array(team2)

    # Use a hash function to map frozensets to integers
    hash_function = lambda x: abs(hash(frozenset(x)))
    team1 = team1.apply(hash_function)
    team2 = team2.apply(hash_function)

    # Standardize numerical features
    scaler = StandardScaler()
    X_train[['members_team_1', 'members_team_2']] = scaler.fit_transform(X_train[['members_team_1', 'members_team_2']])
    X_test[['members_team_1', 'members_team_2']] = scaler.transform(X_test[['members_team_1', 'members_team_2']])
