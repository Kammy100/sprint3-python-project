# 4. c) Total NA vs JP sales
total_na = 0
total_jp = 0
for game in video_game_sales:
    total_na += game[NA_SALES]
    total_jp += game[JP_SALES]

print(f"Total NA Sales: {total_na}")
print(f"Total JP Sales: {total_jp}")

if total_na > total_jp:
    print("North America had higher total sales")
else:
    print("Japan had higher total sales")

# 4. d) List of Nintendo published games
nintendo_games = []
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])

print(nintendo_games)
print(len(nintendo_games))
