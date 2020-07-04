def compact(enum):
    data = []
    for i, e in enumerate(enum):
        if i == 0 or enum[i - 1] != e:
            data.append(e)
    return data


if __name__ == '__main__':
    print(compact([]))
