sgn x = if x < 0 
          then -1 
          else if x == 0 
              then 0 
              else 1
-- The sgn function maps all negative values to -1, and all positive values to +1, 0 remains 0

sgnGuards x | x < 0 = -1
            | x == 0 = 0
            | otherwise = 1

main = do
    putStrLn "Please enter a number"
    input <- getLine 
    let x = (read input :: Int)
    putStrLn( show (sgnGuards (x)) )
