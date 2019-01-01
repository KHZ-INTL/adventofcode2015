#!/bin/python3

total_length = 0

def get_ribbon_bow(gift):
    dimension = []

    for i in gift.split('x'):
        dimension.append(int(i))

    ribbon_length = 2*dimension[0] + 2*dimension[1]

    ribbon_bow = dimension[0] * dimension[1] * dimension[2]

    print("[Gift]: {}\n[SurfaceA]: {}\n[Slack]: {}\n".format(gift, ribbon_length, ribbon_bow))

    return (ribbon_length + ribbon_bow)

with open('puzzle', 'r') as file:
    for line in file:
        if len(line) == 0:
            continue
        else:
            sa = get_ribbon_bow(line.strip())
            total_length += sa

print(total_length)
