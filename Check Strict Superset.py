# Read the main set A
A = set(map(int, input().split()))

# Read the number of other sets
n = int(input())

# Initialize a flag to keep track of whether A is a strict superset
is_superset = True

# Iterate through the other sets
for _ in range(n):
    other_set = set(map(int, input().split()))

    # Check if A is not a strict superset of the other set
    if not A.issuperset(other_set):
        is_superset = False
        break

# Print the result
print(is_superset)
