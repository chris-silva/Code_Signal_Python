def coolPairs(a, b):
    uniqueSums = {x[0] + x[1]
                  for x in {(i, j) for i in a for j in b if (i*j) % (i+j) == 0}}
    return len(uniqueSums)
