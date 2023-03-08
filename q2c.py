for i in range(1, 1000):
    total = 0
    divs = []
    for div in range(1, i+1):
        if i % div == 0:
            total += div
            divs.append(div)
    if i*2 == total:
        print(f"{i} is half the sum of its positive factors: {divs}")
    divs.clear()