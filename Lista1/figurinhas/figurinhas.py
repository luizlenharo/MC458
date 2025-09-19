i = int(input())


def getMdc(a: int, b: int) -> int:
    if b == 0:
        return a

    return getMdc(b, a % b)


for j in range(i):
    a, b = map(int, input().split())
    print(getMdc(a, b))
