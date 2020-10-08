import pandas as pd
import numpy as np

teams = ["Top Esports", "G2 Esports", "DAMWON Gaming", "Team SoloMid", "JD Gaming", "Suning", "Fnatic", "DRX", "Rogue", "Gen.G", "FlyQuest",
        "Machi Esports", "LGD Gaming", "Team Liquid", "PSG Talon", "Unicorns Of Love.CIS"]
leagues = ["LPL", "LEC", "LCS", "LCK", "PCS", "LCL"]
split = ["Summer"]

players_table = pd.read_csv("../Database/2020_lol_worlds_players.csv", index_col=0)
matches = pd.read_csv("../Database/2020_LoL_esports_match_data_from_OraclesElixir_20201002.csv")

players = list(pd.unique(players_table['Player']))

worlds = matches[matches['team'].isin(teams)] # Filtering teams
worlds = matches[matches['player'].isin(players)] # Filtering players
worlds = worlds[worlds['league'].isin(leagues)] # Filtering leagues

worlds.to_csv("../Database/worlds_2020.csv")