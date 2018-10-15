from typing import Sequence


class UnionFindGroup:
    def __init__(self, leader):
        self.leader = leader
        self.size = 1
        self._items = [leader]

    def add(self, item):
        self._items.append(item)

    def __iter__(self):
        for item in self._items:
            yield item


class UnionFind:
    def __init__(self, items: Sequence):
        self._items = items
        for item in items:
            item._union_find_group = UnionFindGroup(leader=item)

    def find(self, item) -> UnionFindGroup:
        """O(1)"""
        return item._union_find_group

    def union(self, item_1, item_2):
        """O(n)"""
        large_group, small_group = self.find(item_1), self.find(item_2)
        if large_group is small_group:
            return
        if large_group.size < small_group.size:
            large_group, small_group = small_group, large_group
        large_group.size += small_group.size
        for item in small_group:
            item._union_find_group = large_group
            large_group.add(item)
        del small_group


class LazyUnionFind:
    pass