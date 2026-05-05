module Main where

main = do
    print (myFunc1 5)
    print (myFunc2 10)
    print (_3rdFunc)

myFunc1 x = x*10
myFunc2 x = x*2 -- resolved: names cannot start with capital letter
_3rdFunc = "Hello, this is 3rd Func" -- resolved: names cannot start with numbers

-- Names can start with _ or lowercase letters