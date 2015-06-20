from time import strftime
from datetime import datetime

#get the current system time
now = datetime.now()

#read parameters
fpara = open('para.txt', 'r+')
parameters = []
for eachline in fpara:
    parameters.append(eachline.strip())
read_filename = parameters[0]
initials = parameters[1]
kg = parameters[2]
temp = parameters[3]
v_scale = parameters[4]
comment = parameters[5]
write_filename = initials + '$r' + read_filename
read_filename_aff = read_filename + '.Asc'
fpara.close()
#end of reading parameters

#write the header of the output file
fwrite = open(write_filename, 'w')
fwrite.write('RF$rJP01   DATE: %s-%s-%s   TIME: %s:%s:%s\n'\
             % (strftime('%d'), strftime('%b').upper(), strftime('%y'), \
                now.hour, now.minute, now.second))
fwrite.write('%s                              B=%s  kG; T=%s K; VS=%s\n'\
             % (comment, kg, temp, v_scale))
fwrite.write('   512     0     0     0     0\n')
fwrite.write('     0.000000     0.000000     0.000000     0.000000\n')
#end of the writing the header

#read the source file, store the data into j1
fread = open(read_filename_aff, 'r')
j1 = []

for eachline in fread:
    j1.append(eachline.split()[1])

#discard the first one and last two numbers, extend the second number 
#and the 3rd number of the end
j1.pop(0)
j1.pop(-1)
j1.pop(-1)
last_one = j1.pop(-1)
first_one = j1.pop(0)
for i in range(0,3):
    j1.append(last_one)
for j in range(0,3):
    j1.insert(0, first_one)

#generate an iterator and put the data into the right format
it = iter(j1)
for each in range(0, 64):
    for ea in range(0, 8):
        fwrite.write(' ')
        fwrite.write(it.next())
        fwrite.write('.')

    fwrite.write('\n')
    
#close the file
fwrite.close()
fread.close()
# end of closing

print 'Done!'

