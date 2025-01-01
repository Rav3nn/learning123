import re
dna1 = input("input the first DNA sequence: ")
n = int(input("input the length of the sub sequence: "))
substringlist = [dna1[i:i+n] for i in range(len(dna1) - n + 1)]
ssdict = {}

for sstr in substringlist:
    ssdict[sstr] = re.findall('[GC]',sstr).__len__()/len(sstr)
   
for key in ssdict:
    if ssdict[key] == max(ssdict.values()):
        print(key)
        break    
