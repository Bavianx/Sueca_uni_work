from sueca_tricks import parseGameFile

from sueca_tricks import *
import sys
if sys.argv[1:]:
  if".sueca" in sys.argv[1]:
    parseGameFile(sys.argv)
    print(sys.argv[2])
  elif  "-c" in sys.argv[1] and ".sueca" in sys.argv[1]:
    parseGameFile(sys.argv).show()
  elif "-g" in sys.argv[1] and ".sueca" in sys.argv[1]:
    print("ff")
  else:
      raise Exception("Invalid argument" +" "+  sys.argv[1] + "\nUsage: python sueca_scorer.py [-c | -g] <game_file>")
else:
    raise Exception("A game file is missing" + "\nUsage: python sueca_scorer.py [-c | -g] <game_file>")

    