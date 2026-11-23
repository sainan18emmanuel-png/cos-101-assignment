import statistics
from typing import List, Union, Tuple

Number = Union[int, float]


def get_sum(numbers: List[Number]) -> Number:
    """Return the sum of a list of numbers."""
    return sum(numbers)


def get_mean(numbers: List[Number]) -> float:
    """Return the arithmetic mean (average) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the mean of an empty list.")
    return sum(numbers) / len(numbers)


def get_median_and_mode(numbers: List[Number]) -> Tuple[Number, List[Number]]:
    """Return a tuple containing the median and a list of mode(s) of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate the median and mode of an empty list.")
    median_val = statistics.median(numbers)
    mode_vals = statistics.multimode(numbers)
    return median_val, mode_vals


if __name__ == "__main__":
    sample_numbers = [10, 20, 20, 30, 40, 50]

    print(f"Numbers: {sample_numbers}")
    print(f"1. Sum: {get_sum(sample_numbers)}")
    print(f"2. Mean (Average): {get_mean(sample_numbers)}")

    median, modes = get_median_and_mode(sample_numbers)
    print(f"3. Median: {median}, Mode(s): {modes}")
