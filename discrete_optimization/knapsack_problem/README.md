# Knapsack problem

Some optimization methods implemented to solve this problem. Test data included.

## Execution

All is in python3 at the moment:

```
python3 knapsack.py <algorithm> <file>
```

## Available opitmization methods

### Naive greedy(ng)

No optimization involved, just takes elements in the order they appear.

### Best ratio greedy(brg)

First orders the elements by decreasing value/weight and then picks them up in order.

### Iterative dynamic programming(dpi)

Not working well. Doesn't find optimal solution yet.

## Acknowledgments

I started this repository to keep track of my work during the online [discrete optimization course](https://www.coursera.org/learn/discrete-optimization) offered by [University of Melbourne](https://www.unimelb.edu.au/) in [Coursera](https://www.coursera.org/). The data used to test the algorithm was taken from the course.
