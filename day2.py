course = []
with open('puzzle_input.csv') as f:
    for line in f:
        move = line.strip()
        course.append(move)

#part1
def calc_position(course, horizontal=0, depth=0):

    for move in course:
        direction, distance = move.split()
        dist = int(distance)
        if direction == 'forward':
            horizontal += dist
        if direction =='down':
            depth += dist
        if direction == 'up':
            depth -= dist

    print('horizontal', horizontal, 'depth', depth)
    return horizontal * depth    

#part2
def calc_position2(course, horizontal=0, depth=0, aim=0):

    for move in course:
        direction, distance = move.split()
        dist = int(distance)
        if direction == 'forward':
            horizontal += dist
            depth += aim*dist
        if direction =='down':
            aim += dist
        if direction == 'up':
            aim -= dist

    print('horizontal', horizontal, 'depth', depth)
    return horizontal * depth   

