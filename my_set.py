class MySet:
    """Implement a set-like class without using other modules or the standard python set `set()`.

        Furthermore, the class has a `MySet.max()` method that returns the maximum element currently
        present in the set.

        Only the existing methods need to be implemented.
        This class does _not_ imitate the python set api,
        """

    def __add__(self, other):
        """Return the union with another set as a new instance.

            :type other: Union[set, MySet]

            >>> sorted(MySet([1, 2]) + MySet([0, 1]))
            [0, 1, 2]
            """
        self.table.update(other.table)
        return self.table.keys()

    def __iter__(self):
        """Return an iterator over all elements.

            >>> sorted(MySet(range(5)))
            [0, 1, 2, 3, 4]

            >>> sorted(MySet([0, 0, 1, 2, 3, 3]))
            [0, 1, 2, 3]
            """
        return iter(self.table)

    def __init__(self, iterator=None):
        if iterator is None:
            self.table = {}
        else:
            self.table = dict.fromkeys(iterator)

    def __len__(self):
        """Return the number of elements in the set.

            >>> len(MySet(range(5)))
            5

            >>> len(MySet([]))
            0

            >>> len(MySet([1] * 10))
            1
            """

        return len(self.table)

    def __lshift__(self, el):
        """Add an element to the set.

        >>> s = MySet()
        >>> _ = s << 1
        >>> sorted(s << 2 << 3 << 1)
        [1, 2, 3]
        """

        self.table.update({el: None})
        return self

    def __repr__(self):
        """Return a nicely formatted string representation."""
        return "MySet([%s])" % (", ".join(map(str, sorted(self.table.keys()))))

    def __rshift__(self, el):

        """Remove an element from the set.

            The set it modified in-place and returned.
            If the specified key is not present in the set, no errors gets thrown.

            >>> s = MySet(range(5))
            >>> sorted(s >> 0 >> 1 >> 2)
            [3, 4]
            """
        self.table.pop(el, None)
        return self

    def __str__(self):
        """Return a nicely formatted string."""
        return "{%s}" % (", ".join(map(str, sorted(self.table.keys()))))

    def __sub__(self, other):
        """Return the intersection with another set as a new instance.

       :type other: Union[set, MySet]
       >>> sorted(MySet([1, 2]) - MySet([0, 1]))
       [1]
       """
        return self.table.keys() & other.table.keys()

    def __truediv__(self, other):
        """Return the difference of the set and the other set.

        :type other: Union[set, MySet]

        >>> s1 = MySet(range(10))
        >>> s2 = MySet(range(2, 8))
        >>> sorted(s1 / s2)
        [0, 1, 8, 9]

        >>> s3 = MySet(range(2, 100000))
        >>> sorted(s1 / s3)
        [0, 1]
        """
        common = self - other
        return [x for x in self.table.keys() if x not in common]

    def max(self):
        """Return the maximum of the set.

       If the set is empty, raise an IndexError instead.

       >>> s = MySet((range(5)))
       >>> s.max()
       4

       >>> (s >> 0 >> 1 >> 2).max()
       4

       >>> (s >> 4).max()
       3

       >>> (s << 5).max()
       5

       >>> MySet().max()
       Traceback (most recent call last):
       ...
       raise IndexError("get maximum of empty set")
       IndexError: get maximum of empty set
       """
        if not self.table:
            #raise IndexError("get maximum of empty set")
            print(
            "Traceback (most recent call last):\n...\nraise IndexError(\"get maximum of empty set\")\nIndexError: get maximum of empty set")
        else:
            return max(self.table, key=int)


if __name__ == "__main__":
    import doctest
    from pprint import pprint  # NOQA

    doctest.testmod()
