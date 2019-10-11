'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    w = word.lower()
    l = list(w)
    print(w.split('th'))
    # if l includes l:
    #     print('th is found in l', l)
    # count_t = 0
    # count_h = 0
    # if t in w and h in w:
    #     if t in w:
    #         count_t += 1
    #     elif h in w:
    #         count_h + 1
    #     else:
    #         return 0
    #     return (count_t + count_h) / 2
    # else:
    #     return count_th(word)
    # TBC
