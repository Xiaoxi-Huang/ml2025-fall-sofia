"""
module5_mod.py
Module that defines the NumberStore class to store integers and search for a target.
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
