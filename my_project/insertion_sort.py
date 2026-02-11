#!/usr/bin/env python

import random


def make_input(len):
    my_input = [x for x in range(1, len + 1)]
    # print(my_input)
    random.shuffle(my_input)
    return my_input


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        # print("i ", i)
        for j in range(i - 1, -1, -1):  # tested: this works!
            # print(list(range(i - 1, -1, -1)))
            new_i = i
            # print(new_i)
            if my_list[new_i] >= my_list[j]:
                print(my_list)
                break
            elif my_list[new_i] < my_list[j]:
                my_list[new_i], my_list[j] = my_list[j], my_list[new_i]
                print(my_list)
                # print(new_i)
                new_i = new_i - 1
                # print(new_i)
    return my_list


my_test_list = make_input(6)
print("my_test_list", my_test_list)
print(insertion_sort(my_test_list))
