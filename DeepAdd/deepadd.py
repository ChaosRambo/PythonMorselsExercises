from datetime import timedelta


def deep_add(inp, *args, **kwargs):
    inp = list(inp)
    for i, val in enumerate(inp):
        if not isIter(val):
            if i == 0:
                cnt = val
            else:
                cnt += val
        else:
            if i == 0:
                cnt = deep_add(val)
            else:
                cnt += deep_add(val)
    if len(inp) == 0:
        cnt = 0
    if 'start' in kwargs:
        cnt += kwargs.get('start')
    for i in args:
        cnt += i
    return cnt


def isIter(obj):
    try:
        iter(obj)
    except Exception:
        return False
    else:
        return True
    

if __name__ == '__main__':
#    print(deep_add([[timedelta(5), timedelta(10)], [timedelta(3)]], timedelta(5)))
#    print(deep_add([[1, 2], [3, 4]], start=2))
    numbers = [1, 2, 3, 4]
    cubes_and_squares = ((n, (n ** 3, n ** 2)) for n in numbers)
    print(cubes_and_squares)
    print(deep_add(cubes_and_squares))
    print(deep_add([1, [2, [3, 4], [], [[5, 6], [7, 8]]]]))
