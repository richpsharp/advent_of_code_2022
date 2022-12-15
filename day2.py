opponent_play_index = ['A', 'B', 'C']
response_play_index = ['X', 'Y', 'Z']

# win gets +6
# X gets +1
# Y gets +2
# Z gets +3
score_matrix_part1 = [
    [1+3, 2+6, 3+0],
    [1+0, 2+3, 3+6],
    [1+6, 2+0, 3+3]]

# win gets +6
# A gets +1
# B gets +2
# C gets +3
score_matrix_part2 = [
    [3+0, 1+3, 2+6],
    [1+0, 2+3, 3+6],
    [2+0, 3+3, 1+6]]


running_score = 0
with open('day2_input.txt', 'r') as input_file:
    for line in input_file:
        op_play, resp_play = line.rstrip().split(' ')
        op_index = opponent_play_index.index(op_play)
        resp_index = response_play_index.index(resp_play)
        score = score_matrix_part2[op_index][resp_index]
        running_score += score
        print(op_play, resp_play, score, running_score)
