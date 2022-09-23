Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.

>>>
>>> squares = [1, 4, 9, 16, 25]
>>> squares
[1, 4, 9, 16, 25]
Like strings (and all other built-in sequence types), lists can be indexed and sliced:

>>>
>>> squares[0]  # indexing returns the item
1
>>> squares[-1]
25
>>> squares[-3:]  # slicing returns a new list
[9, 16, 25]
All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:

>>>
>>> squares[:]
[1, 4, 9, 16, 25]
Lists also support operations like concatenation:

>>>
>>> squares + [36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:

>>>
>>> cubes = [1, 8, 27, 65, 125]  # something's wrong here
>>> 4 ** 3  # the cube of 4 is 64, not 65!
64
>>> cubes[3] = 64  # replace the wrong value
>>> cubes
[1, 8, 27, 64, 125]
You can also add new items at the end of the list, by using the append() method (we will see more about methods later):