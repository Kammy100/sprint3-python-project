# 3. b) Add new game with append() and print new length
video_game_sales.append([21, 'Animal Crossing: New Horizons', 'NS', 2020, 'Simulation', 'Nintendo', 7.45, 5.21, 7.37, 31.18])
print(len(video_game_sales))

# 3. c) Tuple for metadata
# Using len() after appending will be 21, but before it was 20
num_games = len(video_game_sales)
num_columns = 10
dataset_name = 'Video Game Sales'

dataset_info = (num_games, num_columns, dataset_name)
print(dataset_info)

# A tuple is more appropriate than a list because this metadata is fixed and should not be changed / mutated - tuples are immutable and protect the data integrity.
