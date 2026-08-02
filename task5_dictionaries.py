# 5. b) Count games per publisher
games_per_publisher = {}
for game in video_game_sales:
    publisher = game[PUBLISHER]
    if publisher in games_per_publisher:
        games_per_publisher[publisher] += 1
    else:
        games_per_publisher[publisher] = 1

print(games_per_publisher)

# 5. c) Dictionary for #1 ranked game
top = video_game_sales[0] # rank 1

top_game = {
    'name': top[NAME],
    'year': top[YEAR],
    'genre': top[GENRE],
    'publisher': top[PUBLISHER],
    'global_sales': top[GLOBAL_SALES]
}

for key, value in top_game.items():
    print(f"{key}: {value}")
