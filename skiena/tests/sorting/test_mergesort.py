import random

from sorting import mergesort
from datastructures import KeyedItem


def test_min_mergesort():
    sorted_items = [KeyedItem(key=i) for i in range(100)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    mergesort(items)
    assert items == sorted_items


def test_max_mergesort():
    sorted_items = [KeyedItem(key=i) for i in range(99, -1, -1)]
    items = [item for item in sorted_items]
    random.shuffle(items)
    mergesort(items, order='max')
    assert items == sorted_items
