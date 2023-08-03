import pandas as pd

player_stats = pd.read_csv("all_players_stats.csv")

total_goals = player_stats["Goals"].sum()
total_penalties = player_stats["Penalties"].sum()
total_yellow_cards = player_stats["YellowCards"].sum()
total_red_cards = player_stats["RedCards"].sum()
total_teams = player_stats["Team"].nunique()

print("Total goals: ", total_goals)
print("Total penalties: ", total_penalties)
print("Total yellow cards: ", total_yellow_cards)
print("Total red cards: ", total_red_cards)
print("Total different teams: ", total_teams)

user_input = input("Give me the last name of a player: ")

player_row = player_stats[player_stats['Player'].str.contains(user_input, case=False)]

if len(player_row) == 0:
    print("No player found with that last name.")
else:
    row_index = player_row.index[0]
    player_info = player_row.iloc[0]
    print("Team: ", player_info["Team"])
    print("Jersey Number: ", player_info["JerseyNo"])
    print("Position: ", player_info["Position"])
    print("Appearances: ", player_info["Apearances"])
    print("Substitutions: ", player_info["Substitutions"])
    print("Goals: ", player_info["Goals"])
    print("Penalties: ", player_info["Penalties"])
    print("Yellow cards: ", player_info["YellowCards"])
    print("Red cards: ", player_info["RedCards"])
    print("Red cards: ", player_info["RedCards"])