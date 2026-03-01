#!/usr/bin/env python

import random


def make_input(len):
    my_input = [x for x in range(1, len + 1)]
    random.shuffle(my_input)
    return my_input


def list_to_spaces(my_list):
    the_str = ""
    for item in my_list:
        the_str += str(item)
        the_str += " "
    return the_str


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        new_i = i
        for j in range(i - 1, -1, -1):  # tested: this works!
            if my_list[new_i] >= my_list[j]:
                break
            elif my_list[new_i] < my_list[j]:
                my_list[new_i], my_list[j] = my_list[j], my_list[new_i]
                print(list_to_spaces(my_list))
                new_i -= 1
    return my_list


my_len = 50
my_test_list = make_input(my_len)
# print("my_test_list", my_test_list)
my_sorted_list = insertion_sort(my_test_list)
if my_sorted_list == [x for x in range(1, my_len + 1)]:
    print("yay")
else:
    print("not yay")


# visualization of some sample outputs: https://docs.google.com/spreadsheets/d/1M17I7xZfv8ar-IW5LDPEzZW_9DRInr8dbi19-WghmwE/edit?gid=1595823321#gid=1595823321  # noqa
