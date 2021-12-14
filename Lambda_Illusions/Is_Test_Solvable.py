def isTestSolvable(ids, k):
    def digitSum(n): return 0 if n == 0 else n % 10 + digitSum(n//10)

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
