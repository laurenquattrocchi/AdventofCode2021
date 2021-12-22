depths = []
 with open("input.csv") as f:
    for line in f:
        depth = line.strip()
        depths.append(int(depth))