#!/usr/bin/env python3
import sys
import numpy as np

def read_positive_int(prompt):
    while True:
        try:
            v = int(input(prompt).strip())
            if v <= 0:
                print("Please enter a positive integer.")
                continue
            return v
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def read_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a real number (e.g., 3, -1.2, 0.75).")

def main():
    print("=== k-NN Regression (NumPy) ===")
    N = read_positive_int("Enter N (number of points, positive integer): ")
    k = read_positive_int("Enter k (number of neighbors, positive integer): ")

    # Read N (x, y) points
    xs = np.empty(N, dtype=float)
    ys = np.empty(N, dtype=float)
    for i in range(N):
        xs[i] = read_float(f"Point {i+1} - enter x: ")
        ys[i] = read_float(f"Point {i+1} - enter y: ")

    # Check k vs N
    if k > N:
        print(f"Error: k ({k}) must be <= N ({N}).")
        sys.exit(1)

    # Read query X
    Xq = read_float("Enter X (query point): ")

    # k-NN regression in 1D: average the y-values of k nearest x's to Xq
    dists = np.abs(xs - Xq)

    # Get indices of k smallest distances (O(n) selection), then order them for display (optional)
    k_idx_unsorted = np.argpartition(dists, kth=k-1)[:k]
    k_idx = k_idx_unsorted[np.argsort(dists[k_idx_unsorted])]

    y_pred = float(np.mean(ys[k_idx]))

    # Output
    print("\n=== Result ===")
    print(f"Nearest neighbor indices (0-based): {k_idx.tolist()}")
    print(f"Distances: {dists[k_idx].tolist()}")
    print(f"Predicted Y at X={Xq}: {y_pred}")

if __name__ == "__main__":
    main()
