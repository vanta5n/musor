import random


RUS = [
    ("А", ".-"),
    ("Б", "-..."),
    ("В", ".--"),
    ("Г", "--."),
    ("Д", "-.."),
    ("Е", "."),
    ("Ж", "...-"),
    ("З", "--.."),
    ("И", ".."),
    ("Й", ".---"),
    ("К", "-.-"),
    ("Л", ".-.."),
    ("М", "--"),
    ("Н", "-."),
    ("О", "---"),
    ("П", ".--."),
    ("Р", ".-."),
    ("С", "..."),
    ("Т", "-"),
    ("У", "..-"),
    ("Ф", "..-."),
    ("Х", "...."),
    ("Ц", "-.-."),
    ("Ч", "---."),
    ("Ш", "----"),
    ("Щ", "--.-"),
    ("Ъ", ".--.-."),
    ("Ы", "-.--"),
    ("Ь", "-..-"),
    ("Э", "..-.."),
    ("Ю", "..--"),
    ("Я", ".-.-")
]
ENG = [
    ("A", ".-"),
    ("B", "-..."),
    ("C", "-.-."),
    ("D", "-.."),
    ("E", "."),
    ("F", "..-."),
    ("G", "--."),
    ("H", "...."),
    ("I", ".."),
    ("J", ".---"),
    ("K", "-.-"),
    ("L", ".-.."),
    ("M", "--"),
    ("N", "-."),
    ("O", "---"),
    ("P", ".--."),
    ("Q", "--.-"),
    ("R", ".-."),
    ("S", "..."),
    ("T", "-"),
    ("U", "..-"),
    ("V", "...-"),
    ("W", ".--"),
    ("X", "-..-"),
    ("Y", "-.--"),
    ("Z", "--..")
]
inter = [
    ("А", "A"),
    ("Б", "B"),
    ("В", "W"),
    ("Г", "G"),
    ("Д", "D"),
    ("Е", "E"),
    ("Ж", "V"),
    ("З", "Z"),
    ("И", "I"),
    ("Й", "J"),
    ("К", "K"),
    ("Л", "L"),
    ("М", "M"),
    ("Н", "N"),
    ("О", "O"),
    ("П", "P"),
    ("Р", "R"),
    ("С", "S"),
    ("Т", "T"),
    ("У", "U"),
    ("Ф", "F"),
    ("Х", "H"),
    ("Ц", "C"),
    ("Ч", "-"),
    ("Ш", "-"),
    ("Щ", "Q"),
    ("Ъ", "-"),
    ("Ы", "Y"),
    ("Ь", "X"),
    ("Э", "-"),
    ("Ю", "-"),
    ("Я", "-")
]


t = input("r/e/i/RI >>> ").lower()
score = 0

if t == 'ri':
    m = [(i[0] + ' r', i[1]) for i in RUS] + [(i[0] + ' e', i[1]) for i in ENG]
    d = {}
    for i in m:
        if i[1] not in d.keys():
            d[i[1]] = [i[0]]
        else:
            d[i[1]].append(i[0])

    total, corr = 0, 0

    while True:
        p = random.choice(list(d.items()))
        i = random.randint(0, 1)
        if i:
            j = random.randint(0, len(p[1]) - 1)
            inn = input(p[i][j] + ' >>> ').upper()
            if inn == p[0]:
                corr += 1
                print("\033[32m" + p[0] + "\033[0m")
            else:
                print("\033[31m" + p[0] + "\033[0m")
            total += 1
        else:
            inn = input(p[i] + ' >>> ').upper()
            if inn in [aaa[0] for aaa in p[1]]:
                corr += 1
                print("\033[32m" + '/'.join(p[1]) + "\033[0m")
            else:
                print("\033[31m" + '/'.join(p[1]) + "\033[0m")
            total += 1
        print(str(corr / total * 100)[:5], '%')

elif t == 'i':
    random.shuffle(inter)
    for p in inter:
        if input(p[0] + " >>> ").upper() == p[1]:
            score += 1
            print("\033[32m" + p[1] + "\033[0m")
        else:
            print("\033[31m" + p[1] + "\033[0m")

    print(score)

elif t == 'r':
    random.shuffle(RUS)
    if input('t/f >>> ').lower() == 't':
        for p in RUS:
            if input(p[0] + " >>> ").upper() == p[1]:
                score += 1
                print("\033[32m" + p[1] + "\033[0m")
            else:
                print("\033[31m" + p[1] + "\033[0m")
    else:
        for p in RUS:
            if input(p[1] + " >>> ").upper() == p[0]:
                score += 1
                print("\033[32m" + p[0] + "\033[0m")
            else:
                print("\033[31m" + p[0] + "\033[0m")

    print(score)

else:
    random.shuffle(ENG)
    if input('t/f >>> ').lower() == 't':
        for p in ENG:
            if input(p[0] + " >>> ").upper() == p[1]:
                score += 1
                print("\033[32m" + p[1] + "\033[0m")
            else:
                print("\033[31m" + p[1] + "\033[0m")
    else:
        for p in ENG:
            if input(p[1] + " >>> ").upper() == p[0]:
                score += 1
                print("\033[32m" + p[0] + "\033[0m")
            else:
                print("\033[31m" + p[0] + "\033[0m")

    print(score)
