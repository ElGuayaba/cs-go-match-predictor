import streamlit as st 
import pandas as pd
from pickle import load
from input_transformer import InputTransformer
from keras.models import load_model

st.title('CS GO Match predictor')
st.write("Based on two team compositions, we'll try to predict who would win. Give it a try:")

transformer = pd.read_pickle('../models/input_transformer.pkl')

model = load_model('../models/csgo_match_results_predictor-beta1.h5')

class_dict = {
    "0": "Tie",
    "1": "Team 1",
    "2": "Team 2"
}

player_options = transformer.player_data['player_nick'].drop_duplicates().sort_values()

st.header('Team 1')

player1_team1 = st.selectbox(label='1', key='Player 1 Team 1', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player2_team1 = st.selectbox(label='2', key='Player 2 Team 1', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player3_team1 = st.selectbox(label='3', key='Player 3 Team 1', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player4_team1 = st.selectbox(label='4', key='Player 4 Team 1', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player5_team1 = st.selectbox(label='5', key='Player 5 Team 1', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')

st.header('Team 2')

player1_team2 = st.selectbox(label='1', key='Player 1 Team 2', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player2_team2 = st.selectbox(label='2', key='Player 2 Team 2', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player3_team2 = st.selectbox(label='3', key='Player 3 Team 2', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player4_team2 = st.selectbox(label='4', key='Player 4 Team 2', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')
player5_team2 = st.selectbox(label='5', key='Player 5 Team 2', index=None, options=player_options, placeholder='Please choose a player...', label_visibility='collapsed')


if st.button("Predict"):
    team1 = [player1_team1, player2_team1, player3_team1, player4_team1, player5_team1]
    team2 = [player1_team2, player2_team2, player3_team2, player4_team2, player5_team2]

    players = team1+team2

    if any(not isinstance(elem, str) for elem in players):
        st.error('Please select all players', icon="🚨")
    elif len(set(players)) < len(players):
        st.error('Please make sure all players are different', icon="🚨")
    else:
        transformed_input = transformer.transform_input(team1, team2)

        prediction = str(int(model.predict(transformed_input)[0][0]))

        pred_class = class_dict[prediction]

        st.write("The winner is:", pred_class)