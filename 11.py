
from itertools import combinations
import numpy as np
import time


def get_galaxies(file):
    local_cluster_file = open(file, "r")
    lines = local_cluster_file.readlines()
    local_cluster = []
    for line in lines:
        local_cluster.append((list(line[:-1])))
    local_cluster = np.array(local_cluster)
    rows = cols = len(local_cluster[0:])
    galaxies = {}
    id = 0
    for i in range(0, rows):
        for j in range(0, cols):
            if local_cluster[i][j] == '#':
                coords = [i, j]
                galaxies[id] = {'galaxy_id': id}
                galaxies[id]['coords'] = coords
                id += 1
    return galaxies


def get_empty_space(galaxies):
    is_not_empty_x = []
    is_not_empty_y = []

    for key, value in galaxies.items():
        is_not_empty_x.insert(0, value['coords'][0])
        is_not_empty_y.insert(0, value['coords'][1])
    is_not_empty_x.sort(reverse=True)
    is_not_empty_y.sort(reverse=True)
    # print(is_not_empty_x)
    # print(is_not_empty_y)
    return is_not_empty_x, is_not_empty_y


def expand_space(galaxies):
    (is_not_empty_x, is_not_empty_y) = get_empty_space(galaxies)
    expansion_coeficient = 1000000

    # print(galaxies)
    for i in reversed(range(is_not_empty_x[len(is_not_empty_x)-1],
                            is_not_empty_x[0])):
        if i not in is_not_empty_x:
            # print('expand x:', i)
            for key, value in galaxies.items():
                if (value['coords'][0] >= i):
                    value['coords'][0] += expansion_coeficient - 1

    for i in reversed(range(is_not_empty_y[len(is_not_empty_y)-1],
                            is_not_empty_y[0])):
        if i not in is_not_empty_y:
            # print('expand y:', i)
            for key, value in galaxies.items():
                if (value['coords'][1] >= i):
                    value['coords'][1] += expansion_coeficient - 1

    print(galaxies)
    return galaxies


def calculate_distance(galaxy_pair):
    return abs(galaxy_pair[0][0]-galaxy_pair[1][0]) + \
        abs(galaxy_pair[0][1]-galaxy_pair[1][1])


def main():
    start = time.time()
    times = 1
    for i in range(0, times):
        galaxies = get_galaxies("local_cluster.txt")
        galaxies = expand_space(galaxies)
        all_coords = []
        for key, value in galaxies.items():
            all_coords.append(value['coords'])
        # print(all_coords)
        total_distance = 0
        total_combinations = 0
        for galaxy_pair in combinations(all_coords, 2):
            # print(galaxy_pair, calculate_distance(galaxy_pair))
            total_distance += calculate_distance(galaxy_pair)
            total_combinations += 1
    print('total_combinations:',total_combinations)
    print(total_distance)
    end = time.time()
    print('time:', ((end - start)/times) * 1000, 'ms')


if __name__ == "__main__":
    main()
