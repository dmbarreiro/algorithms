#!/usr/bin/python

from collections import namedtuple

def sort_by_ratio(unordered_list, attribute, reverse=False):
    """Sorts list of namedtuples by attribute (increasing by default)
    """
    unordered_list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

def read_ordered_knapsack_input(file_data):
    """Reads knapsack problem input file data and returns knapsack capacity and
    items list ordered by decreasing value/weight ratio. Better items (with
    higher ratio) are first in the list.
    """
    Item = namedtuple("Item", ['index', 'value', 'weight', 'ratio'])
    lines = file_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = list()

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1]), int(parts[0])/int(parts[1])))
    
    sort_by_ratio(items, 'ratio', reverse=True)
    return items, capacity, item_count

def read_knapsack_input(file_data):
    Item = namedtuple("Item", ['index', 'value', 'weight'])
    lines = file_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = list()

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
        
    return items, capacity, item_count