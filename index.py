def persistence(num):
    persistence_count = 0

    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        persistence_count += 1

    return persistence_count
