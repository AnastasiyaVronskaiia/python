my_list = [1, 12, 23, 8, 4, 9, 5, 4, 10]
more_then = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(more_then)