"""
module5_call.py
Main script that uses NumberStore from module5_mod to collect N integers and search for X.
"""

from module5_mod import NumberStore

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
