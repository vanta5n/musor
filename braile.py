import random


alphabet = [
    ('A', '.     '),
    ('B', '. .   '),
    ('C', '..    '),
    ('D', '.. .  '),
    ('E', '.  .  '),
    ('F', '...   '),
    ('G', '....  '),
    ('H', '. ..  '),
    ('I', ' ..   '),
    ('J', ' ...  '),
    ('K', '.   . '),
    ('L', '. . . '),
    ('M', '..  . '),
    ('N', '.. .. '),
    ('O', '.  .. '),
    ('P', '... . '),
    ('Q', '..... '),
    ('R', '. ... '),
    ('S', ' .. . '),
    ('T', ' .... '),
    ('U', '.   ..'),
    ('V', '. . ..'),
    ('W', ' ... .'),
    ('X', '..  ..'),
    ('Y', '.. ...'),
    ('Z', '.  ...'),
    ('CAPITAL', '     .'),
    ('DIGIT', ' . ...'),
    ('.', '  .. .'),
    (',', '  .   '),
    ('?', '  .  .'),
    (';', '  . . '),
    ('!', '  ... '),
    ('"BEGIN', '  . ..'),
    ('"END', '   ...'),
    ('()', '  ....'),
    ('-', '    ..'),
    ('1', '.     '),
    ('2', '. .   '),
    ('3', '..    '),
    ('4', '.. .  '),
    ('5', '.  .  '),
    ('6', '...   '),
    ('7', '....  '),
    ('8', '. ..  '),
    ('9', ' ..   '),
    ('0', ' ...  '),
]
random.shuffle(alphabet)
random.shuffle(alphabet)
random.shuffle(alphabet)

t1 = input('t/f >>> ').strip().lower()
score = 0

if t1 == 't':
    for x in alphabet:
        print(x[0])
        s1 = input().strip('\\')
        s2 = input().strip('\\')
        s3 = input().strip('\\')
        ans = s1 + s2 + s3
        if ans == x[1]:
            score += 1
            print("\033[32m" + "correct!" + "\033[0m")
        else:
            print("\033[31m" + "wrong!" + "\033[0m")
            # print("\033[31m\033[40m" + x[1][:2] + "\033[0m")
            # print("\033[31m\033[40m" + x[1][2:4] + "\033[0m")
            # print("\033[31m\033[40m" + x[1][4:] + "\033[0m")
            for s in (x[1][:2], x[1][2:4], x[1][4:]):
                for c in s:
                    if c == '.':
                        print("\033[31m\033[40m" + c + "\033[0m", end='')
                    else:
                        print("\033[31m\033[47m" + c + "\033[0m", end='')
                print()

else:
    for x in alphabet:
        if x[0].isdigit():
            continue

        # print(x[1][:2], x[1][2:4], x[1][4:], sep='\n')
        for s in (x[1][:2], x[1][2:4], x[1][4:]):
            for c in s:
                if c == '.':
                    print("\033[31m\033[40m" + c + "\033[0m", end='')
                else:
                    print("\033[31m\033[47m" + c + "\033[0m", end='')
            print()

        x0 = x[0]
        if x0 in 'ABCDEFGHIJ':
            x0 += str('0ABCDEFGHIJ'.index(x[0]) % 10)
        ans = input().upper().strip('\\')
        if ans == x0:
            score += 1
            print("\033[32m" + x0 + "\033[0m")
        else:
            print("\033[31m" + x0 + "\033[0m")

print(score, '/', len(alphabet) - 10 * (t1 == 'f'))

