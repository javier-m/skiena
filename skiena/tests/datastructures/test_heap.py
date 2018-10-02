import random

from datastructures import Heap
from datastructures.heap import Item


def test_insert_min_heap():
    heap = Heap()
    items = [Item(key=i) for i in range(10)]
    random.shuffle(items)
    for item in items:
        heap.insert(item)
    for i in range(10):
        assert heap.extract_root().key == i
    assert heap.extract_root() is None


def test_construct_min_heap():
    heap = Heap()
    items = [Item(key=i) for i in range(10)]
    random.shuffle(items)
    heap.construct(items)
    for i in range(10):
        assert heap.extract_root().key == i
    assert heap.extract_root() is None


def test_insert_max_heap():
    heap = Heap(heaptype='max')
    items = [Item(key=i) for i in range(10)]
    random.shuffle(items)
    for item in items:
        heap.insert(item)
    for i in range(10):
        assert heap.extract_root().key == 10 - i - 1
    assert heap.extract_root() is None


def test_construct_max_heap():
    heap = Heap(heaptype='max')
    items = [Item(key=i) for i in range(10)]
    random.shuffle(items)
    heap.construct(items)
    for i in range(10):
        assert heap.extract_root().key == 10 - i - 1
    assert heap.extract_root() is None
