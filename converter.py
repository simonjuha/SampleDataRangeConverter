import os
filename = 'input.txt'

# Range
out_max = 250   
out_min = 0
in_max = 1
in_min = -1

# round ouput?
round_output = 1
# comma seperate?
com_sep = 1

# open file
with open(filename, 'r') as f:
    lines = f.readlines()
    line_numb = len(lines)
    new_lines = [0] * line_numb
    
    for idx, line in enumerate(lines, start=0):
        output = lines[idx].rstrip()
        
        # Chance value
        output = float(output)
        output = (output - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
        
        if round_output == 1:
            output = round(output)

        if com_sep == 1:
            new_lines[idx] = "{}{}".format(output, str(', '))
        else:
            new_lines[idx] = output
        

    
# save new file
with open('output.txt', 'w') as new_f:
    for item in new_lines:
        if com_sep == 0:
            new_f.write("%s\n" % item)
        else:
            new_f.write(item)

new_f.close() 
f.close()

