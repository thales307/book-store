def total(basket):    
    groups = []

    while basket != []:
        books = set(basket)
        for b in books:
            basket.remove(b)
        groups.append(len(books))
    while 3 in groups and 5 in groups:
        groups.remove(5)
        groups.remove(3)
        groups.append(4)
        groups.append(4)

    prices = {
        1: 800,
        2: 1520,
        3: 2160,
        4: 2560,
        5: 3000
    }

    return int(sum(prices[b] for b in groups))