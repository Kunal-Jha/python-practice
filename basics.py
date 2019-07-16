"""Please add bodies to all of the below functions, so that the doctests complete successfully.

You must not add any import statements, only the basic python language features are required
and the imported `re` module.
"""

import re


def as_range(x, y):
    """Get a given range between x and y.

    :type x: int
    :type y: int

    :returntype list

    >>> as_range(0, 5)
    [0, 1, 2, 3, 4, 5]

    >>> as_range(5, 3)
    [5, 4, 3]

    >>> as_range(0, -5)
    [0, -1, -2, -3, -4, -5]

    >>> as_range(0, 0)
    [0]
    """
    if x < y:
        return list(range(x, y + 1, 1))
    elif x > y:
        return list(range(x, y - 1, -1))
    else:
        return [x]


def filter_strings(substring, strings):
    """Return all strings that include a certain sub-string (case insensitive).

    >>> filter_strings('x', ['x', '123xdfg', 'ert', 'eXq', 'kll'])
    ['x', '123xdfg', 'eXq']

    >>> filter_strings('hello', ['hello ', 'python', '123-HellOx'])
    ['hello ', '123-HellOx']
    """
    result = []
    for check_string in strings:
        if re.search(substring, check_string, re.IGNORECASE):
            result.append(check_string)
    return result


def get_every_third_element(iterable):
    """Return every the first and every consecutive third element of an iterable.

    :returntype Generator

    >>> g = get_every_third_element(range(1000000000000000000000000))
    >>> next(g)
    0
    >>> next(g)
    3
    >>> next(g)
    6
    >>> g.close()
    """
    return (i for i in range(iterable.start, iterable.stop, 3))


def get_every_third_split(iterable, delimiter, regex):
    """Split a string by a delimiter and return every third split matching a pattern.

    :type iterable: Iterable[str]
    :type delimiter: str
    :type regex: str
    :returntype Generator

    >>> g = get_every_third_split(["123-456-789", "qwe-asd-xcv", "wer-sdf"], "-", ".*[17qxwd].*")

    >>> next(g)
    '123'

    >>> next(g)
    'asd'

    >>> next(g)
    'sdf'

    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    x = []
    r = re.compile(regex)
    for ele in iterable:
        x.append(list(filter(r.match, ele.split(delimiter))))
    flatten = [item for sublist in x for item in sublist]
    i = 0
    while i < len(flatten):
        if i % 3 == 0:
            yield flatten[i]
        i += 1


def get_splits_including_pattern(string, delimiter, regex):
    """Split a string by a delimiter and return all splits matching a regex pattern.

    The delimiter is a single-character string.

    :type string: str
    :type delimiter: str
    :type regex: str
    :returntype Generator

    >>> g = get_splits_including_pattern("qwe-asd-xwecv", "-", "as.*")
    >>> next(g)
    'asd'
    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration

    >>> g = get_splits_including_pattern("qwe-asd-xwecv", "a", "[a-zA-Z]{2}-.*")
    >>> next(g)
    'sd-xwecv'

    >>> g = get_splits_including_pattern("qwe-asd-xwecv", "x", "we")
    >>> next(g)
    'wecv'

    >>> next(g)
    Traceback (most recent call last):
    ...
    StopIteration
    """
    r = re.compile(regex)
    for a in list(filter(r.match, string.split(delimiter))):
        yield a


def return_list_from_behind(li):
    """Return the list in opposite order without last element.

    >>> return_list_from_behind([1, 2, 3, 4])
    [3, 2, 1]

    >>> return_list_from_behind([])
    []

    >>> return_list_from_behind([1, 2])
    [1]
    """
    li.reverse()
    return li[1:]


def update_dict(d, *ds):
    """Update a dict out-of-place with values from other dicts.

    Only values for existing keys in d should be updated.

    :type d: dict
    :type *ds: tuple of dicts

    >>> pprint(update_dict({1: 2, 3: 4}, {0: 1, 1: "2"}))
    {1: '2', 3: 4}

    >>> pprint(update_dict({1: 2, 3: 4}, {0: 1, 1: "2"}, {3: "hello", 4: 5}))
    {1: '2', 3: 'hello'}
    """
    d.update((k, v) for tup in ds for k, v in tup.items() if k in d)
    return d


if __name__ == "__main__":
    import doctest
    from pprint import pprint  # NOQA

    doctest.testmod()
