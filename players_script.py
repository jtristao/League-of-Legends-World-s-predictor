import pandas as pd
import numpy as np

matches = pd.read_csv("Database/2020_LoL_esports_match_data_from_OraclesElixir_20201002.csv")
teams = ["Top Esports", "G2 Esports", "DAMWON Gaming", "Team SoloMid", "JD Gaming", "Suning", "Fnatic", "DRX", "Rogue", "Gen.G", "FlyQuest",
        "Machi Esports", "LGD Gaming", "Team Liquid", "PSG Talon", "Unicorns Of Love.CIS"]
leagues = ["LPL", "LEC", "LCS", "LCK", "PCS", "LCL"]
split = ["Summer"]

PlayersTable = pd.DataFrame(columns=["Player", "Team"])

for team in teams:
    team_matches = matches[matches['team'] == team]
    team_matches = team_matches[team_matches['split'] == "Summer"]
    team_matches = team_matches[team_matches['player'].notna()]
    players = pd.unique(team_matches['player'])

    for player in players:
            PlayersTable = PlayersTable.append({'Player':player, 'Team':team}, ignore_index=True)
            
PlayersTable.to_csv("Database/2020_lol_worlds_teams.csv")