# 2. a) Extract 5th game name (index 4) and get "Pokemon"
game_name = video_game_sales[4][NAME]
# "Pokemon Red/Blue" -> "Pokemon" is first 7 characters
print(game_name[0:7])

# 2. b) Clean messy names
for name in messy_names:
    cleaned = name.strip().lower()
    print(cleaned)

# 2. c) Formatted summary of #1 game with f-string
top_game = video_game_sales[0]
top_name = top_game[NAME]
top_year = top_game[YEAR]
top_sales = top_game[GLOBAL_SALES]

print(f"#1 Best Seller: {top_name} ({top_year}) - ${top_sales}M global sales")
