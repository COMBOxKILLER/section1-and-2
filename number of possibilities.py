# Given values
dictionary_size = 20000
average_word_length = 6.77

# For passwd1
possibilities_passwd1 = dictionary_size

# For passwd2
possible_positions_number = math.floor(average_word_length) + 1
possible_positions_symbol = math.floor(average_word_length) + 1

possibilities_passwd2 = dictionary_size * possible_positions_number * possible_positions_symbol

# Total possibilities
total_possibilities = possibilities_passwd1 * possibilities_passwd2

print("Total possible passwords:", total_possibilities)