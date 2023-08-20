if __name__ == '__main__':
    # Initialize an empty list
    my_list = []

    # Read the value of n
    n = int(input())

    # Iterate through each command
    for _ in range(n):
        command = input().split()
        operation = command[0]

        if operation == "insert":
            position = int(command[1])
            element = int(command[2])
            my_list.insert(position, element)
        elif operation == "print":
            print(my_list)
        elif operation == "remove":
            element = int(command[1])
            my_list.remove(element)
        elif operation == "append":
            element = int(command[1])
            my_list.append(element)
        elif operation == "sort":
            my_list.sort()
        elif operation == "pop":
            my_list.pop()
        elif operation == "reverse":
            my_list.reverse()
