ask :: String -> IO ()
ask prompt = do
  putStrLn prompt
  line <- getLine
  
  -- version 2
  test2 prompt line

  -- model answer
  if line == ""
    then ask prompt
    else if (line == "quit")
      then putStrLn("quitting..") --condition added for quitting
    else do
      putStrLn ("you said: " ++ reverse line)
      ask prompt --needed for repeated inputsl answer

-- used case pattern
test2 prompt line = do
    case line of
      t | t == "quit" -> putStrLn("quitting..")
        | t /= "" -> putStrLn ("you said: " ++ reverse line) >> ask prompt -- used >> to ignore previous result and continue sequence
        | otherwise -> ask (prompt ++ "!")

main :: IO ()
main = do
  let prompt = "please say something"
  ask prompt

