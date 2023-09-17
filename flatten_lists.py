#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def iter_flatten(iterable):
    it = iter(iterable)
    for e in it:
        if isinstance(e, (list, tuple)):
            for f in iter_flatten(e):
                yield f
        else:
            yield e


list1 = [["elem1", "elem2", ["elem3", "elem4"]], "elem5", "elem2"]
list2 = ["test2"], [["elem1"]]


flatten_list1 = [i for i in iter_flatten(list1)]
flatten_list2 = [i for i in iter_flatten(list2)]

set1 = set(flatten_list1)
set2 = set(flatten_list2)

print(list(set1.union(set2)))
