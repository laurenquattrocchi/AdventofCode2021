#part 1
def depth_increases(filename):
    depths = []
    with open(filename) as f:
        for line in f:
            depth = line.strip()
            depths.append(int(depth))


    count = 0
    for i, value in enumerate(depths):
        if i == 0:
            last_value = value
            continue
        if value > last_value:
            count += 1
        last_value = value

    print(count)

#part 2
