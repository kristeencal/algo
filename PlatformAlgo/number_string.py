#Write a program that takes an array of numbers and replaces any number that's negative to a string called 'Dojo'. For example if array = [-1, -3, 2] after your program is done array should be ['Dojo', 'Dojo', 2].

def number_string(arr):
    for i in range(len(arr)):
        if arr[i]< 0:
            arr[i] = "dojo"

    return arr


print(number_string([-1, -3, 2]))
