
from collections import namedtuple
import copy

def knapsack_dp_iterative_solver(input_items, capacity):
    n_items = len(input_items)
    record_value = []
    record_taken = []
    record_weight = []
    all_time_best_index = -1
    # Begin algorithm profiling
    #import cProfile
    #cp = cProfile.Profile()
    #cp.enable()
    ###########################
    for iteration in range(len(input_items)):
        if(input_items[iteration].weight <= capacity and input_items[iteration].value > 0):
            # If element fits in knapsack and does not have a negative value
            # assume weights cannot be negative but values can
            if(iteration == 0):
                best_value = input_items[0].value
                best_taken = [0]*n_items
                best_taken[0] = 1
                best_weight = input_items[0].weight
                record_value.append(best_value)
                record_taken.append(best_taken)
                record_weight.append(best_weight)
                all_time_best_index = 0
            else:
                if(record_weight[-1] + input_items[iteration]. weight <= capacity): 
                    best_value = record_value[-1] + input_items[iteration].value
                    best_taken = copy.deepcopy(record_taken[-1])
                    best_taken[iteration] = 1
                    best_weight = record_weight[-1] + input_items[iteration].weight
                    record_value.append(best_value)
                    record_taken.append(best_taken)
                    record_weight.append(best_weight)
                else:
                    best_fit_index = -1
                    best_value_found = -1
                    for past in range(iteration):
                        if(record_weight[past] + input_items[iteration].weight < capacity and
                            record_value[past] > best_value_found):
                            best_value_found = record_value[past]
                            best_fit_index = past
                    if(best_fit_index != -1 and best_value_found != -1):
                        best_value = record_value[best_fit_index] + input_items[iteration].value
                        best_taken = copy.deepcopy(record_taken[best_fit_index])
                        best_taken[iteration] = 1
                        best_weight = record_weight[best_fit_index] + input_items[iteration].weight
                        record_value.append(best_value)
                        record_taken.append(best_taken)
                        record_weight.append(best_weight)
                    else:
                        best_value = input_items[iteration].value
                        best_taken = [0]*n_items
                        best_taken[iteration] = 1
                        best_weight = input_items[iteration].weight
                        record_value.append(best_value)
                        record_taken.append(best_taken)
                        record_weight.append(best_weight)
                if(record_value[all_time_best_index] < best_value): all_time_best_index = iteration
    # Profiling end
    #cp.disable()
    #cp.print_stats()
    ###############
    return record_value[all_time_best_index], record_taken[all_time_best_index], 0
