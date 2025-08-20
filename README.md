# 🎯 Best Subset Finder

This Python script helps you find the subset of numbers whose sum is closest to a target value **without exceeding it**. It's useful for optimization problems, budgeting scenarios, or any situation where you need to select the most valuable combination of items under a constraint.

## 🚀 Features

- Accepts a flexible number of float inputs
- Efficiently searches all possible subsets
- Returns the best subset and its total sum
- Simple and easy-to-use function interface

## 📦 Installation

No external dependencies required. Just make sure you're using Python 3.6 or higher.

## 🧠 Usage

```python
from findsum import find_best_subset

subset, total = find_best_subset(10.0, 1.5, 3.2, 4.8, 2.0)
print(f"Best subset: {subset}, Total sum: {total}")
```

# Parameters
* `target_sum` (`float`): The maximum allowed sum.
* `*args` (`float`): A variable number of float values to choose from

# Returns
* A tuple: `([best_subset], best_sum)`

## 📘 Example: 
``` python
find_best_subset(15.0, 5.5, 6.0, 4.0, 3.5, 2.0)
# Output: ([6.0, 4.0, 3.5], 13.5)
```

## 🛠️ Function Definition
```python
def find_best_subset(target_sum: float, *args: float) -> Tuple[List[float], float]:
```

# 📄 License
This project is open-source and available under the MIT License.
