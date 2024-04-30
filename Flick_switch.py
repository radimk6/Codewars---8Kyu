# Create a function that always returns True/true for every item in a given list.
# However, if an element is the word 'flick', switch to always returning the opposite boolean value.

# Examples
# ['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

# ['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

# ['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
# Notes
# "flick" will always be given in lowercase.
# A list may contain multiple flicks.
# Switch the boolean value on the same element as the flick itself.

# flick_switch(['codewars', 'flick', 'code', 'wars']), [True, False, False, False]
# flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']), [False, False, False, False]
# flick_switch(['bicycle', 'jarmony', 'flick', 'sheep', 'flick']), [True, True, False, False, True]
# flick_switch(['bicycle']), [True]
# flick_switch(['john, smith, susan', 'flick']), [True, False]
# flick_switch(['flick', 'flick', 'flick', 'flick', 'flick']), [False, True, False, True, False]
# flick_switch([]), []

def flick_switch(lst):
    boolean = True
    result = []
    for word in lst:
        if boolean == False and word == "flick":
            boolean = True
        elif word == "flick":
            boolean = False
        # print(boolean)
        result.append(boolean)
    return result #print(result)
    

flick_switch(['codewars', 'flick', 'code', 'wars'])