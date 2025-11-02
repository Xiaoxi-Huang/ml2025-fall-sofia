"""
module5_oop.py
Single-file program that uses OOP to collect N integers, then searches for X.
Outputs -1 if X was not among the N numbers; otherwise outputs the 1-based index of X.
"""

from typing import List

class NumberStore:
    def __init__(self) -> None:
        self._data: List[int] = []

    def insert_number(self, value: int) -> None:
        self._data.append(value)

    def search_first_index_1based(self, target: int) -> int:
        """Return 1-based index of first occurrence of target, or -1 if not found."""
        for i, v in enumerate(self._data, start=1):
            if v == target:
                return i
        return -1

    def size(self) -> int:
        return len(self._data)


def _read_positive_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            n = int(raw)
            if n <= 0:
                print("Please enter a positive integer (> 0).")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def _read_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main() -> None:
    store = NumberStore()
    N = _read_positive_int("Enter N (positive integer): ")

    for i in range(1, N + 1):
        x = _read_int(f"Enter number #{i}: ")
        store.insert_number(x)

    X = _read_int("Enter X (integer to search): ")
    idx = store.search_first_index_1based(X)
    print(idx)


if __name__ == "__main__":
    main()
