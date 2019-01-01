#!/bin/python3

total_surface_area = 0

def smallest_side(dimension):
    length = min(dimension)
    dimension.remove(length)
    width = min(dimension)

    return (length * width)

def get_surface_area(gift):
    dimension = []

    for i in gift.split('x'):
        dimension.append(int(i))

    surface_area = 2*(dimension[0] * dimension[1]) + 2*(dimension[1]*dimension[2]) + 2*(dimension[2]*dimension[0])

    slack = smallest_side(dimension)

    print("[Gift]: {}\n[SurfaceA]: {}\n[Slack]: {}\n".format(gift, surface_area, slack))

    return (surface_area + slack)

with open('puzzle', 'r') as file:
    for line in file:
        if len(line) == 0:
            continue
        else:
            sa = get_surface_area(line.strip())
            total_surface_area += sa

print(total_surface_area)
