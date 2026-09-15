import sys 
from dataclasses import dataclass

@dataclass
class TestCase:
    g: int
    n: int
    a: int
    b: int
    key: int

def parse_group(lines: list[str], group_number: int) -> TestCase:
    """ Turn one group of 'label value' lines into a TestCase. """
    values = {}
    for line in lines:
        parts = line.split()
        if len(parts) != 2:
            raise ValueError(
                f"Test case {group_number}: expected 'label value', got {line!r}"
            )
        label, value = parts
        values[label] = int(value)

    return TestCase(
        g=values["g"], n=values["n"], a=values["a"], b=values["b"], key=values["key"]
    )

def read_test_cases(path: str) -> list[TestCase]:
    """ Read each text group in the file. Lines starting with # are comments. """
    with open(path) as f:
        text = f.read()

    test_cases = []
    current_group: list[str] = []
    for raw_line in text.splitlines() + [""]:  
        line = raw_line.strip()
        if line.startswith("#"):
            continue  
        if line:
            current_group.append(line)
        elif current_group:
            test_cases.append(parse_group(current_group, len(test_cases) + 1))
            current_group = []

    return test_cases

def fast_mod(x, y, m):

    i = 1
    result = 1
    prevRemainder = x % m
    if y & i == i:
        result = (result * prevRemainder) % m

    while i in range(y):
        i = 2 * i
        currRemainder = (prevRemainder ** 2) % m

        if y & i == i:
            result = (result * currRemainder) % m
        prevRemainder = currRemainder

    return result

def recursive_fast_mod(b, e, m):
    if (e == 1):
        return b % m;
    elif (e % 2 != 0):
        return b * (fast_mod(b, e / 2, m) ** 2)
    else:
        return (fast_mod(b, e/ 2, m)) ** 2
 

def get_shared_key(g, n, a, b):
    capA = fast_mod(g, a, n)
    capB = fast_mod(g, b, n)

    keyA = fast_mod(capB, a, n)
    keyB = fast_mod(capA, b, n)

    if (keyA == keyB): 
        return keyA

def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <data_filename.txt>")
        sys.exit(1)
    path = sys.argv[1]
    try:
        test_cases = read_test_cases(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Read {len(test_cases)} test case(s) from {path}\n")
    for i, tc in enumerate(test_cases, start=1):
        print(f"Test case {i}:")
        print(f"  g   = {tc.g}")
        print(f"  n   = {tc.n}")
        print(f"  a   = {tc.a}")
        print(f"  b   = {tc.b}")
        print(f"  key = {tc.key}")
        print()


    for i, tc in enumerate(test_cases, start=1):
        print(f"Test case {i}:")
        print(get_shared_key(tc.g, tc.n, tc.a, tc.b) == tc.key)
        print()


    print(recursive_fast_mod(10, 89, 2026))

main()