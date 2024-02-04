# Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from pickle import load, dump

# Dataset
player_data = pd.read_csv('../data/raw/match_players.csv')

player_data = player_data[['player_id', 'player_nick']].drop_duplicates()

# SAVE THE DATASET
player_data.to_csv('../data/interim/player_data.csv', index=False)

# Input has to be a string array of len 5
def get_team_id_from_name(player_names_list):
    players = player_data[player_data['player_nick'].isin(player_names_list)]

    return players.groupby('player_nick').first()['player_id'].to_list()


with open("../models/scalers/standard_scaler.pkl", 'rb') as file:
    scaler = load(file)

# Input params have to be list-like
def transform_input(team1, team2):
    team1 = pd.DataFrame(team1)
    team2 = pd.DataFrame(team2)

    hash_function = lambda x: hash(frozenset(x))
    team1 = team1.apply(hash_function)
    team2 = team2.apply(hash_function)

    transformed_input = scaler.transform(pd.concat([team1,team2], axis=1))

    return [transformed_input, np.array([[0.0 for i in range(15)]])]

class InputTransformer:
    player_data = pd.read_csv('../data/interim/player_data.csv')

    scaler = scaler

    def __init__(self):
        pass

    def _get_team_id_from_name(self, player_names_list):
        players = player_data[player_data['player_nick'].isin(player_names_list)]
        return players.groupby('player_nick').first()['player_id'].to_list()

    def transform_input(self, team1, team2):
        team1 = self._get_team_id_from_name(team1)
        team2 = self._get_team_id_from_name(team2)

        team1 = pd.DataFrame(team1)
        team2 = pd.DataFrame(team2)

        hash_function = lambda x: hash(frozenset(x))
        team1 = team1.apply(hash_function)
        team2 = team2.apply(hash_function)

        transformed_input = scaler.transform(pd.concat([team1,team2], axis=1))

        return [transformed_input, np.array([[0.0 for i in range(15)]])]

# Create an instance
obj = InputTransformer()

with open("../models/input_transformer.pkl", "wb") as f:
    dump(obj, f)
