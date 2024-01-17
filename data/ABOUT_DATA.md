# About the data

This dataset created by Filipe Macedo
github user: https://www.kaggle.com/filipechavesdemacedo 

These datasets were built by the owner using a pipeline that collects data from competitive Counter Strike go (cs-go) games. 

The original dataset contains three .csv files. 

**match_results.csv - Contains information related to match results:**
1. data_unix: Start date of the match in Unix format.
2. event_name: Name of the event or championship.
3. map: Name of the map on which the match was played.
4. match_id: Match identifier.
5. match_link: Partial link to the match; for the complete link, concatenate it with www.hltv.org
6. offset: Page offset number on the hltv.org website.
7. team_*_id: Identifiers of the teams that participated in the match.
8. team_*_link: Partial links of the teams that participated in the match; for the complete link, concatenate them with www.hltv.org.
9. team_*_name: Names of the teams that participated in the match.
10. team_*_score: Scores of the teams that participated in the match.

**match_players.csv - Contains the score of players during the matches:**
adr: Average damage per round caused by the player.
assists: Assists provided by the player to help a teammate eliminate an opponent.
deaths: Number of deaths of the player in the match.
fkdiff: Difference between the number of times the player was the first to kill or be killed in the round.
hs: Number of opponents eliminated with a headshot.
kdratio: Percentage of rounds in which the player either had an assist, eliminated an opponent, or survived in the match.
kill: Number of opponents eliminated in the match.
match_id: Match identifier.
match_link: Partial link to the match; for the complete link, concatenate it with www.hltv.org 
player_id: Player identifier.
player_nick: Nickname of the player.
players_link: Partial link to the player; for the complete link, concatenate it with www.hltv.org.
rating: Rating 2.0.
team_name: Name of the team in which the player participates.

**player_stats.csv - Contains the stats from the players in played matches. This dataset is an aggregate from the two previous datasets**
assists_round: Average assists per round played.
deaths_round: Average deaths per round played.
dmg_round: Average damage caused per round played.
gnd_dmg_round: Average damage caused with grenades per round played.
hs_percentage: Percentage of headshots.
impact: Impact caused by the player in the matches played.
kast: Percentage of rounds in which the player had an assist, eliminated an enemy, or survived.
kd_ratio: Kill-to-death ratio, the percentage of rounds in which the player had an assist, eliminated an enemy, or survived in the match.
kills_round: Average opponents eliminated per round played.
maps_played: Number of maps/matches played by the player.
player_age: Age of the player.
player_country: Country of the player.
player_id: Player identifier.
players_link: Partial link to the player; for the complete link, concatenate it with www.hltv.org.
player_nick: Nickname of the player.
rating_1:NO DESCRIPTION BY THE USER.
rounds_played: Number of rounds played by the player.
save_team_round: Rounds in which the player saved a teammate divided by the number of rounds played.
save_by_team_round: Rounds in which the player was saved by a teammate divided by the number of rounds played.
total_deaths: Total deaths suffered by the player.
total_kills: Total opponents eliminated by the player.