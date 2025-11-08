from itertools import combinations
from typing import List, Tuple

def find_best_subset(target_sum:float, *args: float) -> Tuple[List[float], float]:
    """
    Finds the subset of numbers that is closest to the target sum without exceeding it.
    
    :param target_sum: The target sum to be achieved.
    :param args: A variable number of float arguments representing the numbers to consider.
    :return: A tuple containing the best subset and its total sum.
    """
    best_subset = []    # Initialize the best subset
    best_sum = float('inf') # Initialize the best sum to infinity
    
    # Iterate through all possible combinations of the input numbers
    for r in range(1, len(args) + 1):   # r is the size of the combination
        for subset in combinations(args, r):    # Generate combinations of size r
            current_sum = sum(subset)   # Calculate the sum of the current subset
            # Check if the current sum is less than or equal to the target sum
            if abs(current_sum - target_sum) < abs(best_sum - target_sum):      # Update best subset if current is closer
                best_sum = current_sum      # Update the best sum
                best_subset = list(subset)  # Update the best subset
    
    # Return the best subset and its total sum
    return best_subset, best_sum if best_sum != float('inf') else 0.0
