# -*- coding: utf-8 -*-

from string import letters, digits
from random import choice
from itertools import islice, count, tee, takewhile, imap

def randstrings(strs, limit=None):
    """
    generate random strings by given string.
    """
    return (choice(strs) for x in countup(stop=limit))

def randalphanumerics(limit=None):
    """
    generate random alphabet or numeric.
    """
    return randstrings(letters + digits, limit)

def take(seq, num):
    """
    take items from sequence
    """
    return islice(seq, 0, num)

def takeright(seq, num):
    """
    selects last n elements.
    """
    length = len(seq)
    return islice(seq, length - num, None)

def mkstring(seq, sep=''):
    """
    this is another way to make sring join iterbles.
    """
    return sep.join(seq)

def countup(stop=None):
    """
    countup for stop. if stop is None, countup to infinity.
    """
    return (x for x in take(count(), stop))

def head(seq):
    """
    select first element.
    """
    return next(take(seq, 1))

def tail(seq):
    """
    selects all elements except the first.
    """
    return islice(seq, 1, None)

def swap(x, y, pred=lambda x,y: true):
    """
    swap args, if pred is true.
    """
    return (y, x) if pred(x,y) else (x, y)

def zipwithindex(seq, start=0):
    """
    zip with indexing.
    """
    return ((i, x) for i, x in enumerate(seq, start))

def splitat(seq, index, step=0):
    """
    splits this list into two at a given position.
    """
    seq1, seq2 = tee(seq)
    return islice(seq1, 0, index), islice(seq2, index + step, None)

def sliding(seq, size, step=1):
    """
    Groups elements in fixed size blocks by passing a 'sliding window' over them (as opposed to partitioning them, as is done in grouped.
    """
    def _(_seq, _size, _step):
        seq1, seq2 = splitat(_seq, _size, _step-_size)
        yield list(seq1)
        for seq3 in sliding(seq2, size, step):
            yield seq3

    return takewhile(lambda x: x != [], _(seq, size, step))

def slidingwithpadding(seq, size, step=1, padding=''):
    def _(lst):
        if len(lst) != size:
            return lst + [padding]*(size-len(lst))
        else:
            return lst

    return imap(_, sliding('abcdefg', size, step))

def reduceright(seq):
    """
    applies a binary operator to all elements of this list, going right to left.
    """
    pass

def reversemap(func, seq):
    """
    builds a new collection by applying a function to all elements of this list and collecting the results in reversed order.
    """
    pass
