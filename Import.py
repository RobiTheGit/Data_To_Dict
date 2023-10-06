#!/usr/bin/python3
import Data2Dict							#	Import The Data2Dict Scripts 
Data2Dict.MakeDict(open("data.txt",'r'), "|", "\n", False)		#	Run Data2Dict on the example file, Data2Dict.MakeDict(<datafile>, sep1, sep2, OUTPUTVALUE)
for x in (Data2Dict.Dict):						#	While the counter isn't the same value as the length of the output
    print(f'[{Data2Dict.Dict[x]}]')					#	Print The output
