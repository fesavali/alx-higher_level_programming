9.10. Objects and values
If we execute these assignment statements,

a = "banana"
b = "banana"
we know that a and b will refer to a string with the letters "banana". But we don’t know yet whether they point to the same string.

There are two possible states:

Two state diagrams for multiple references with strings
In one case, a and b refer to two different things that have the same value. In the second case, they refer to the same thing. These things have names — they are called objects. An object is something a variable can refer to.

We can test whether two names have the same value using ==:

>>> a == b
True
We can test whether two names refer to the same object using the is operator:

>>> a is b
True
This tells us that both a and b refer to the same object, and that it is the second of the two state diagrams that describes the relationship.

Since strings are immutable, Python optimizes resources by making two names that refer to the same string value refer to the same object.

This is not the case with lists:

>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b
True
>>> a is b
False