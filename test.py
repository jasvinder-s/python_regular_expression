# Open a file
import re
fo = open("fmms_a.txt", "r+")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
 

matchObject = True
previousLine = "learning"

#2010-07-07 10:40:51,337 fmms.connectors: UglyHackHandler running disconnect
errorPattern = "^\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2},\d{1,3}\s\w*"

#loop through all the lines in file,
# print trace  messaages - 1 line before Traceback and complete trace.
for line in fo:
    
    #print line
    if(matchObject == True):
        matchObj = re.match( 'Traceback', line, re.I)
        
        if(matchObj != None and matchObject == True):
            #print "-------------------"
            print previousLine 
            print line
            matchObject = False # print all the trace, so dont match any further
            matchObj = None            
        
        else:         
            previousLine = line # get the previous line before Traceback

    # Print traceback
    else:
        errorObj = re.match(errorPattern, line, re.I); #for checking it trace has ended
        if(errorObj == None): # means this is still trace line
            print line 
        else:
             matchObject = True
             previousLine = line
             print "------------------------------"

fo.close()    

