# minesweeper

The readme isn't meant to be a blog but I figured I'll catalogue some stuff here.

I recently picked up Python after a long hiatus (>2 years) from programming in general. Last time I touched a high level programming language (C#) was back in mid 2015! And no, T-SQL and PL/SQL doesn't count as programming ... at least not to me.

Python is new to me and besides doing tutorials online and implementing basic data structures and test cases, it's great to just write some code with a goal in mind. So far from my experience, the first most QoL upgrade ovre C# and other similar languages is the loosely typed aspect. Having done some javascript in the past which is also loosely typed, there is a marked difference in the way I approach coding between loosely/strongly typed languages :-

1) Time saved by not having to think upfront what type your variable is going to be. Especially with like int/bigint scenarios, you don't even need to handle that in Python 3.
2) For numbers, often you deliberate between int, float, long, decimal etc... most times you just need a "number". Work with an int for a while then you realize you needed a float ... vice versa. Loosely type means you don't have to worry about what type to choose.

For point 1, of course thinking about type your variable should be is good practice and I guess compiled code in those scenarios are more efficient versus interpretive code like Python, since types are assigned at runtime. In my javascript days, you do run into weird errors because a variable was actually a type you didn't expect midway through (forgot my examples now but ...)

For point 2, if needed you can always 'cast' it to the type you need using int() for example so you can always make it strongly typed if you require.

Anyway, I digress.

--------

I decided to write a simple Minesweeper thing  due to an upcoming tech interview with Triplebyte. I still don't know if they are legit, but just gonna give it a try! As part of their interview guide they start with a section of writing a simple game, an example given of which was Minesweeper.

Wrote this thingy in about an hour. With every new code I write, I learn a little bit about Python syntax, libraries, and what it means to write "Pythonic code". I learnt a couple of things working on this simple minesweeper app :-

1) Pythonic way of initiatizing a list of objects, courtesy of here : https://stackoverflow.com/questions/1807026/initialize-a-list-of-objects-in-python

e.g. self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

2) Also the fact you can use _ to replace a variable if the index doesn't matter.

3) Pythonic way of working with lists directly, courtesy of here : https://stackoverflow.com/questions/7984169/strip-all-the-elements-of-a-string-list the list comprehension syntax is pretty neat.

e.g. actions = [x.strip() for x in inp.split(',')]

4) random.sample which is useful for picking random elements from a list, which I used to generate the mines at random indices. I suspect this is useful for whatever random sampling statistical analysis. Courtesy of here : https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list

e.g. mineIndex = random.sample(list(range(0, self.rows*self.cols-1)), self.numMines)

5) Finally, the fact that is it 'pythonic' to let try/except clauses handle LOTS of things, "easier to ask forgiveness than permission" i quote, from here : https://stackoverflow.com/questions/3501382/checking-whether-a-variable-is-an-integer-or-not

I use it to forgo checks where inputs are not in the required structure, are not integers, and also if array indices are out of bounds. Pretty useful and certainly convenient.

Besides, it was also opportunity to use some syntax I recall from previous learning e.g. the // operator is a divide and floor operator which is useful when working with integers.

e.g. self.numMines = (self.rows*self.cols)//4 #decide how many mines

So learnt quite a few things by just sitting down, writing code for an hour and looking up stackoverflow!
