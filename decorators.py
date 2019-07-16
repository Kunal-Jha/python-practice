"""Please add bodies to all of the below functions, so that the doctests complete successfully.

You must not add any import statements, only the basic python language features are required
and the imported `re` module.
"""


from functools import wraps


def log(f):
    """Log every function call with callee and args.

    >>> @log
    ... def f(x): return x

    >>> f(1)
    call: f=f, *args=(1,), **kwargs={}
    1

    >>> f(1) == 1
    call: f=f, *args=(1,), **kwargs={}
    True
    """
    def echo_func(*func_args, **func_kwargs):
        print('call: f={}'.format(f.__name__) + ', *args=({},)'.format(*func_args)+', **kwargs={}'.format(func_kwargs))
        return f(*func_args, **func_kwargs)

    return echo_func


def multiply(factor):
    """Multiply a number by a given factor.

    :type factor: Union[int, float]

    >>> @multiply(2)
    ... def identity(x): return x

    >>> identity(1)
    2

    >>> @multiply(2)
    ... @multiply(.5)
    ... def identity(x): return x

    >>> identity(1)
    1.0
    """

    def function(original_func):
        def wrapper_function(*args):
            return factor * original_func(*args)
        return wrapper_function

    return function


if __name__ == "__main__":
    import doctest
    from pprint import pprint  # NOQA
    doctest.testmod()
