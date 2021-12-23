#file to read in
depths = []
with open('input.csv') as f:
    for line in f:
        depth = line.strip()
        depths.append(int(depth))

#part 1
def depth_increases(lst):
    count = 0
    for i, value in enumerate(lst):
        if i == 0:
            last_value = value
            continue
        if value > last_value:
            count += 1
        last_value = value
    return count

#part 2
def win_depth_increase(lst):
    count = 0
    for i,value in enumerate(lst):
        if i + 2 > len(lst) - 1:
            break
        else:
            win = []
            win.append(value)
            win.append(lst[i+1])
            win.append(lst[i+2])
            total = sum(win)
            if i == 0:
                last_total = total
                continue
            if total > last_total:
                count += 1
            last_total = total
    return count



