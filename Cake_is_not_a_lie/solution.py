def splitBySize(s, size):
    for pos in range(0, len(s), size):
        yield s[pos: pos+size]

def validCake(s):
    for n in range(len(set(s)), len(s)):
        piece = set()
        for st in splitBySize(s, n):
            piece.add(st)
        if len(piece) == 1:
            return len(s)/n
    return 1

if __name__ == '__main__':
    all_pass = True
    tcs = {"abccbaabccba": 2,
           "abcabcabcabc": 4,
           "abcabcabcabcd": 1}
    for tc in tcs:
        res = validCake(tc)
        expcted = tcs[tc]
        if res != expcted:
            all_pass = False
            print "FAKE ANSWER"
    if all_pass:
        print "All TEST PASSED"
