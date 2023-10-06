#!/usr/bin/python3
import Data2Dict
Data2Dict.MakeDict(open("data.txt",'r'), "|", "\n")
print(Data2Dict.Dict)
