def compact(enum):
    data = []
    for i in enum:
        if i != next(reversed(data), None) or (len(data) == 0 and i is None):
            data.append(i)
    return data


if __name__ == '__main__':
    print(compact([1, 1, 2, 2, 3, 2]))
    print(compact([None, 0, "", []]))
    c = compact(n**2 for n in [1, 2, 2])
    print(iter(c) is c)
