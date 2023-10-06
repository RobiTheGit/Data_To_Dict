#!/usr/bin/python3
if __name__ == "__main__":				#	Are we running the script itself
    global Sep1, Sep2					#	Global the required variables
    File = "data.txt"					#	Open data.txt (this file can be anything)
    Data = open(File,'r')					#	Open the file in read only mode
    Sep1 = '|'						#	Define the seperator character for person information entry as "|"
    Sep2 = '\n'						#	Define the seperator character for a new person as a newline

global Dict, datalist, print_output			#	Global the required variables
Dict = {}						#	Set up the dictionary
datalist = []						#	Define datalist (only used for making the dict)
print_output = True					#	Set printing the final dictionary to True

def MakeDict(datafile, sep1, sep2):			#	<FUNCTION (MakeDict) BEGIN>
    datafile2 = datafile.readlines()			#	Read the lines from the data file
    res = []						#	Define a result list
    [res.append(x) for x in datafile2 if x not in res]	#	Append all unique items to the list
    for x in range(len(res)):				#	Repeat for all of the unique entries
        datalist.append((res[x].split(sep2))[0])	#	Add the person to the data list
    for x in range(len(datalist)):			#	Repeat for all of the people in the Data List        
        dataitem = datalist[x].split(sep1)		#	Split the information for each person into list elements
        for y in range(len(dataitem)):			#	Repeat for the all people in the data
            Dict[x] = datalist[x].split(sep1)		#	Define the UserID for the person and put in the data for them
            Dict[x][x] = dataitem[x]			#	Add the user info into a list in the Dict entry
    if print_output == True: 				#	Are we printing the final dict?       
        print(Dict)					#	if so, print it
    return Dict						#	Send it to a variable so we can print it later
    pass						#	<FUNCTION (MakeDict) END>

if __name__ == "__main__":				#	Are we running the script itself
    MakeDict(Data, Sep1, Sep2)				#	If so, run the code for making the dictionary from the file
else:							#	If we aren't
    pass						#	Don't run anything (call with MakeDict(<datafile>) instead)
