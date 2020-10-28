def multipleOf3and5(number):
    i = 0
    total = 0
    while (i < number):
        if ((i % 3 == 0) or (i % 5 == 0)):
            total += i
        i += 1

    return total


