import streamlit as st 
import pandas as pd
from pickle import load
from input_transformer import InputTransformer

st.title('Hello World')

transformer = pd.read_pickle('../models/input_transformer.pkl')

model = pd.read_pickle('../models/csgo_match_results_predictor-beta1.pkl')

class_dict = {
    "0": "Tie",
    "1": "Team 1",
    "2": "Team 2"
}

player_options = transformer.player_data['player_nick'].drop_duplicates().sort_values()

player1_team1 = st.selectbox(label='Player 1 Team 1', index=None, options=player_options, placeholder='Please choose a player...')
player2_team1 = st.selectbox(label='Player 2 Team 1', index=None, options=player_options, placeholder='Please choose a player...')
player3_team1 = st.selectbox(label='Player 3 Team 1', index=None, options=player_options, placeholder='Please choose a player...')
player4_team1 = st.selectbox(label='Player 4 Team 1', index=None, options=player_options, placeholder='Please choose a player...')
player5_team1 = st.selectbox(label='Player 5 Team 1', index=None, options=player_options, placeholder='Please choose a player...')

player1_team2 = st.selectbox(label='Player 1 Team 2', index=None, options=player_options, placeholder='Please choose a player...')
player2_team2 = st.selectbox(label='Player 2 Team 2', index=None, options=player_options, placeholder='Please choose a player...')
player3_team2 = st.selectbox(label='Player 3 Team 2', index=None, options=player_options, placeholder='Please choose a player...')
player4_team2 = st.selectbox(label='Player 4 Team 2', index=None, options=player_options, placeholder='Please choose a player...')
player5_team2 = st.selectbox(label='Player 5 Team 2', index=None, options=player_options, placeholder='Please choose a player...')


if st.button("Predict"):
    transformed_input = transformer.transform_input(
        [player1_team1, player2_team1, player3_team1, player4_team1, player5_team1],
        [player1_team2, player2_team2, player3_team2, player4_team2, player5_team2])

    prediction = str(int(model.predict(transformed_input)[0][0]))

    pred_class = class_dict[prediction]

    st.write("The winner is:", pred_class)