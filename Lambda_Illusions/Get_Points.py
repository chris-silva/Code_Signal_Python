def getPoints(answers, p):
    questionPoints = lambda x, y : x + 1 if y == True else -1 * p

    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res
