if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    # Create a tuple from the list of integers
    tuple_list = tuple(integer_list)

    # Calculate and print the hash value of the tuple
    hash_value = hash(tuple_list)
    print(hash_value)
