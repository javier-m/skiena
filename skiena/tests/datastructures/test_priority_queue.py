import pytest

from datastructures import PriorityQueue
from datastructures.priority_queue import Item


def test_primitives():
    priority_queue = PriorityQueue()
    with pytest.raises(NotImplementedError):
        priority_queue.insert(Item(0, 0))
    with pytest.raises(NotImplementedError):
        priority_queue.find_min()
    with pytest.raises(NotImplementedError):
        priority_queue.delete_min()


def test_find_min_unsorted_array():
    priority_queue = PriorityQueue(implementation='unsorted_array')
    assert priority_queue.find_min() is None
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    assert priority_queue.find_min() is item_4
    priority_queue.insert(item_2)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_3)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1


def test_delete_unsorted_array():
    priority_queue = PriorityQueue(implementation='unsorted_array')
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    priority_queue.insert(item_2)
    priority_queue.insert(item_3)
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_2
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_3
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_4
    priority_queue.delete_min()
    assert priority_queue.find_min() is None
    priority_queue.delete_min()
    assert priority_queue.find_min() is None


def test_find_min_sorted_array():
    priority_queue = PriorityQueue(implementation='sorted_array')
    assert priority_queue.find_min() is None
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    assert priority_queue.find_min() is item_4
    priority_queue.insert(item_2)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_3)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1


def test_delete_sorted_array():
    priority_queue = PriorityQueue(implementation='sorted_array')
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    priority_queue.insert(item_2)
    priority_queue.insert(item_3)
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_2
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_3
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_4
    priority_queue.delete_min()
    assert priority_queue.find_min() is None
    priority_queue.delete_min()
    assert priority_queue.find_min() is None


def test_find_min_balanced_tree():
    priority_queue = PriorityQueue(implementation='balanced_tree')
    assert priority_queue.find_min() is None
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    assert priority_queue.find_min() is item_4
    priority_queue.insert(item_2)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_3)
    assert priority_queue.find_min() is item_2
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1


def test_delete_balanced_tree():
    priority_queue = PriorityQueue(implementation='balanced_tree')
    item_4 = Item(4, 4)
    item_2 = Item(2, 2)
    item_3 = Item(3, 3)
    item_1 = Item(1, 1)
    priority_queue.insert(item_4)
    priority_queue.insert(item_2)
    priority_queue.insert(item_3)
    priority_queue.insert(item_1)
    assert priority_queue.find_min() is item_1
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_2
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_3
    priority_queue.delete_min()
    assert priority_queue.find_min() is item_4
    priority_queue.delete_min()
    assert priority_queue.find_min() is None
    priority_queue.delete_min()
    assert priority_queue.find_min() is None
