# a)
total_games = len(video_game_sales)
print(total_games)

# b)
total_global_sales = 0

for game in video_game_sales:
    total_global_sales += game[GLOBAL_SALES]

avg_global_sales = total_global_sales / total_games
print("Average global sales:", avg_global_sales)

# c)
top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_global_sales) * 100
print(top_game_share)
