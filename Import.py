#!/usr/bin/python3
import Data2Dict					#	Import The Data2Dict Scripts
Data2Dict.MakeDict(open("data.txt",'r'), "|", "\n")	#	Run Data2Dict on the example file
print(Data2Dict.Dict)					#	Print The output (though the script already prints it)
