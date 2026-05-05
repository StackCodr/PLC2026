module Intro1 where

-- define named constants:

r1 :: Integer
r1 = 1
-- Yellow warning, Resolved: Type signature was missing
{-
WARNING EXPLANATION
Haskell applies Monomorphism restrictions (force it to have one concrete type) if its a top-level value with no arguments (not a function)
-}

r2 :: Double
r2 = b**2 + 1/b where b = 2
-- Yellow warning, Resolved: Type inconsistency across expression occured.
{- 
WARNING EXPLANATION
(^) was used, exponent must be an integral type (i.e. Int, Integer)
(a / b) was used, both a and b must be a fractional type (i.e. Float or Double)
The expression was unified type-wise (to Fractional) by replacing (^) with (**)
(a ** b) expects both a and b to be of a floating type (e.g. Float, Double).
-}

-- define a function:
diff :: Num a => a -> a -> a
diff a b = abs (a - b)
-- Yellow warning, Resolved: Type signature was missing
-- abs() is a built-in Haskell function that returns absolute value of number (result always non-negative)
-- diff function takes in two arguments.
{-
TYPE SIGNATURE EXPLANATION
• A type signature describes what kinds of values a function takes and what it returns.  
• A type variable (like a) is a placeholder that can represent any type, making functions reusable for many types.  
• A type constraint (like Num a =>) restricts those variables to a group of types that share certain operations.  
• The => symbol separates constraints from the main part of the type, e.g. Num a => a -> a -> a.  
• These general (polymorphic) type signatures are just flexible versions of fixed ones like Integer -> Integer -> Integer.
-}

r3, r4 :: Integer
r3 = diff (diff a a) a  where a = 1
r4 = diff (diff a b) b  where a = 1; b = 1
-- Yellow warning, Resolved: Type signature was missing
{-
CODE FUNCTIONALITY r3
1. where a = 1 defines local variable, a = 1
2. (diff a a) is an inner call, result is substituted into outer call diff (x) a, where x is result.

CODE FUNCTIONALITY r4
1. where a = 1; b = 1 defines local variables, a = 1 and b = 1
2. similar to r3

"where" keyword introduces local variables:
    - each one is separated by semi-colons (inline way).
    - each one is placed on new line, with indentation
-}

-- lists by enumeration
r5, r6 :: [Integer]
r5 = [1,3,4,1]
r6 = [1..5]
-- Yellow warning, Resolved: Type signature was missing

inc :: Num a => a -> a
inc n = n + 1
-- Yellow warning, Resolved: Type signature was missing

r7, r8 :: [Integer]
r9 :: [Double]
r7 = map inc [1..3] 
r8 = map (diff 2) [1..3]
r9 = map sqrt [1..3]
-- Yellow warning, Resolved: Type signature was missing

{-
CODE FUNCTIONALITY r7
"[1..3]": Create list from 1 to 3.
map:
    - Haskell built-in function, takes a list and function (in its type signature, function is denoted by (a -> b)).
    - Purpose, applies function to every element of a list, producing a new list of results
    - map only works with lists and produces lists

In r8, partial application is used—by giving diff only its first argument (2), it creates a new one‑argument function that’s later applied to each list element by map.

-}

r10, r11 :: [(Integer, Double)]
r10 = zip [1..3] (map sqrt [1..3])
r11 = zip [1..3] (map sqrt [1..2])
-- Yellow warning, Resolved: Type signature was missing
{-
TYPE SIGNATURE EXPLANATION
r10, r11 :: [(Integer, Double)]
- each variable (r10 and r11) holds a list of tuples (i.e. x, y), the tuple (pair) being Integer and Double
- Summary: variables hold list of Integer, Double pairs

CODE FUNCTIONALITY r10
- computation: usually evaluated from right to left
    - (map sqrt [1..3]): map applies sqrt function to each element in list and generates a new list
    - zip [1..3] (x), where x is result of map (list): zip combines two lists into one list of pairs (tuples).

zip:
    - Haskell built-in function that combines two lists into one, producing list with tuples (denoted in type signature by [a] -> [b] -> [(a,b)])
    - If one list is shorter, the zip stops.
    - Example:`zip [1,2,3] [10,20]`, will output [(1,10),(2,20)]

-}

r12 :: IO()
r12 = print [1..3]
-- Yellow warning p1, Resolved: Type signature was missing
{-
TYPE SIGNATURE EXPLANATION
r12 :: IO()
- r12 is an IO action
- IO() type means r12 is an action that interacts with the outside world (e.g. print) and, when it’s done, returns () nothing useful 

CODE FUNCTIONALITY
- list is created in range 1 to 3
- print outputs list to the screen

print:
    - Haskell built-in function that returns an action, something that runtime performs later when program runs.
-}

main :: IO ()
main = pure ()
-- Yellow warning p1, Resolved: Type signature was missing
{-
CODE FUNCTIONALITY
pure: Haskell built-in function that is a do-nothing IO action
-}