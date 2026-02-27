
def even_generator(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield str(i)

try:
    n = int(input())
    gen = even_generator(n)
    print(",".join(gen))
except:
    ValueError(print("idi v pen")) 