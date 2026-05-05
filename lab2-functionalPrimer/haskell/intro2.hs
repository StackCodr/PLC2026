module Intro2 where
-- test Comment
-- String algebra:
name = "Alice"
-- "if" has a special syntax but otherwise a typed version of Lisp's "if":
name2 = if name /= "" then name else "no name" -- "NOTE: /= means not equal"

pname3 = print "Bob"

myprogram = print (1 + m)  -- compiler error: m undefined
m = 1                      -- unless this line is also present

-- sequencing several imperative programs (they are programs made up of statements that run one after another):
prg1 = do -- NOTE: do introduces a block of sequential IO actions
  print "hello " 
  print name  -- level of indentation is important

-- the same, but using algebra of imperative programs:
prg1' = sequence_ [print "hello ", print name]
-- NOTE: sequence_ , built-in function that takes list of actions and runs them in order (ignores their results and returns combined IO() action)

-- one imperative program passing value to another:
prg2 = do
  line <- getLine
  putStrLn ("you typed: " ++ line)
-- NOTE: getLine, IO action that waits for user to input something and then returns it as a string. 
  -- Use of arrow can bind result to a name (In Haskell, the arrow means "run getLine and name its result x", its not about storing a value in a variable)
-- NOTE: putStrLn , IO action that takes a string and prints it to a new line
-- NOTE: ++ operator ,can be used to concatenate strings.

main =  do
  putStrLn name -- like print, but only for strings
  -- putStrLn pname3 -- Couldn't match type ...; Expected type: String; Actual type: IO ()
  pname3 -- in Lisp: eval pname3
  myprogram; prg1; prg2;ello -- sequencing, like 3 lines
-- NOTE:  putStrLn : Mentioned in prg2. But additionally, it only works with strings compared to print.
-- NOTE:  multiple statements can be in one line, separated by semicolons. They will execute in order, from left to right.

-- generic string conversion, using a Java-friendly name:
toString value = show value
-- NOTE: show, a built-in function that converts any printable value into a String

-- string concatenation:
greet1 = "hello " ++ name ++ (toString 123)
-- the same, but with the operator as a function (like Lisp):
greet2 = (++) "hello " name
-- concatenating more than 2 strings:
greet3 = concat ["hello ", name, toString 123]

ello = do
  print greet1
-- NOTE: This is an ready-to-use imperative program.
-- NOTE: main is the only imperative program that runs, so everything else has to be into here to execute.
-- NOTE: Difference between show and print, show does not print anything and just returns a string but print displays value to screen and its an IO action