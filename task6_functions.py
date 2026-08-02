# 6. b) Function to filter by genre with default 'Platform'
def filter_by_genre(data, genre='Platform'):
    filtered = []
    for game in data:
        if game[GENRE] == genre:
            filtered.append(game)
    return filtered

# Test without specifying genre (uses default 'Platform')
print(filter_by_genre(video_game_sales))
# Test with specifying a genre
print(filter_by_genre(video_game_sales, 'Sports'))

# 6. c) Function to get formatted summary
def get_summary(game):
    name = game[NAME]
    year = game[YEAR]
    genre = game[GENRE]
    sales = game[GLOBAL_SALES]
    return f"{name} ({year}) - {genre} - ${sales}M"

# Use it in a loop for every game
for game in video_game_sales:
    print(get_summary(game))
