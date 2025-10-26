# Ask for N
N = int(input("Enter N (positive integer): "))

# Read N numbers one by one
numbers = []
for i in range(1, N + 1):
    num = int(input(f"Enter number #{i}: "))
    numbers.append(num)

# Ask for X and output result
X = int(input("Enter X (integer to find): "))

try:
    index_1_based = numbers.index(X) + 1  # 1-based index
    print(index_1_based)
except ValueError:
    print(-1)
