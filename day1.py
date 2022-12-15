n_to_keep = 3
top_n_list = [0]

with open('day1_input.txt', 'r') as input_file:
    running_sum = 0
    for line in input_file:
        line = line.rstrip()
        if line == '':
            top_n_list = sorted(top_n_list + [running_sum])[-3:]
            running_sum = 0
        else:
            running_sum += int(line)
print(top_n_list)
print(sum(top_n_list))
