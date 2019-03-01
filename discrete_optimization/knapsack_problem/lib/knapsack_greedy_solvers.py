from collections import namedtuple

def knapsack_greedy_order_solver(input_items, capacity):  
    value = 0
    weight = 0
    taken = [0]*len(input_items)

    for item in input_items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    
    # return solution
    optimal = 0
    return value, taken, optimal
