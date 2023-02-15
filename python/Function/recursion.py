v = int(input("Enter a number"))


def cursion(v):
    if v == 1:
        return v
    print(v, "+ ", cursion(v-1), endl)



cursion(v)