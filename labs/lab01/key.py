import random

def recursive_fast_mod(b, e, m):
    # print("wer")
    if (e == 1):
        return b % m;
    elif (e % 2 != 0):
        return b * (recursive_fast_mod(b, e // 2, m) ** 2) % m
    else:
        return ((recursive_fast_mod(b, e // 2, m)) ** 2) % m

def brute_find_key(A, B, g, n):
    # find a:
    for x in range(2, n):
        if (recursive_fast_mod(g, x, n) == A):
            return recursive_fast_mod(B, x, n) 

def flt_test(n):
    x = 1
    p = 1000
    if (n < p):
        p = n
    for x in range(1, p):
        if (recursive_fast_mod(x, n, n) != x):
            return False
    return True

def testGenerator(n, g):
    a = 1
    remainderCount = 1
    for a in range(1, n):
        if (recursive_fast_mod(g, a, n) == 1):
            break
        remainderCount += 1

    return remainderCount

def main() -> None:
    print(recursive_fast_mod(10, 89, 2026))

    print()

    print(recursive_fast_mod(10, 157, 2026))

    print(brute_find_key(11, 17, 3, 31))

    print(brute_find_key(5697403814009845641, 10857110447958648793, 1380889579903879951, 12241706495108194253))

    print()
    print("Fermat's Little Theorem:")

    print(flt_test(12241706495108194253))

    print(flt_test(9963569738995424389))

    print(flt_test(9237750053364305929))

    print()
    print("Test G:")

    print(testGenerator(13, 7))

    passedFLT = False
    while(passedFLT == False):
        random_int = random.randint(100, 999)
        passedFLT = flt_test(random_int)

    g = 1
    while(testGenerator(random_int, g) != (random_int - 1)):
        g += 1

    print(f"g: {g}")
    print(f"n: {random_int}")
    print(testGenerator(random_int, g))    

    print()
    print("Find G for large n:")

    passedFLT = False
    random_int = random.randint(100, 999999)
    while (passedFLT == False):
        while(flt_test(random_int) == False):
            random_int = random.randint(100, 999999)
        print("found q")
        n = 2*random_int + 1
        passedFLT = flt_test(n)
        random_int = random.randint(100, 999999)

    g = random.randint(2, n - 2)
    while(recursive_fast_mod(g, 2, n) == 1):
        g = random.randint(2, n - 2)

    print(f"g: {g}")
    print(f"n: {n}")
    print(testGenerator(n, g))   

main()