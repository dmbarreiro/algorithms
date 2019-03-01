#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib.knapsack_greedy_solvers import knapsack_greedy_order_solver
from lib.dp_iterative_solver import knapsack_dp_iterative_solver
from lib.helpers import read_knapsack_input, read_ordered_knapsack_input
from lib.prepare_solution_knapsack import prepare_solution_knapsack

def call_dpi(input_data):
    input_tuples, sack_capacity, n_items = read_knapsack_input(input_data)    
    value, taken, optimal = knapsack_dp_iterative_solver(input_tuples, sack_capacity)
    return prepare_solution_knapsack(value, taken, optimal)

def call_brg(input_data):
    input_tuples, sack_capacity, n_items = read_ordered_knapsack_input(input_data)
    value, taken, optimal = knapsack_greedy_order_solver(input_tuples, sack_capacity)
    return prepare_solution_knapsack(value, taken, optimal)

def call_ng(input_data):
    input_tuples, sack_capacity, n_items = read_knapsack_input(input_data)
    value, taken, optimal = knapsack_greedy_order_solver(input_tuples, sack_capacity)
    return prepare_solution_knapsack(value, taken, optimal)

if __name__ == '__main__':
    import sys
    help = """
        This solver requires an algorithm and an input file.
        Available algorithms are:
         * ng(naive greedy)
         * brg(best ratio greedy)
         * dpi(dynamic programming iterative)
        Please select input file from the data directory.
        (i.e. python knapsack.py ng ./data/ks_4_0)
        """
    if len(sys.argv) > 2:
        algorithm = sys.argv[1].strip()
        file_location = sys.argv[2].strip()
        try:
            with open(file_location, 'r') as input_data_file:
                input_data = input_data_file.read()
        except FileNotFoundError:
            print('Error: File {} not found.'.format(file_location))
        else:
            output_data = ''
            if(algorithm == 'ng'):
                output_data = call_ng(input_data)
            elif(algorithm == 'brg'):
                output_data = call_brg(input_data)
            elif(algorithm == 'dpi'):
                output_data = call_dpi(input_data)
            else:
                print(help)
            if(output_data != ''): print(output_data)
    else:
        print(help)
