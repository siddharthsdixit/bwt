string = "TTGCCAGGA"
txt = []
count = 0
recover = []
total_occurance = []
str1 = ""
for i in range(len(string)):

    txt.append(string[i])

f = []
l = []

txt.append('$')
matrix = []

for i in range(len(txt)):

    matrix.append(txt[(len(txt)-i):] + txt[:(len(txt))-i])
    #print((txt[(len(txt)-i):] + txt[:(len(txt))-i]))
    #output
    '''
    ['T', 'T', 'G', 'C', 'C', 'A', 'G', 'G', 'A', '$']
    ['$', 'T', 'T', 'G', 'C', 'C', 'A', 'G', 'G', 'A']
    ['A', '$', 'T', 'T', 'G', 'C', 'C', 'A', 'G', 'G']
    ['G', 'A', '$', 'T', 'T', 'G', 'C', 'C', 'A', 'G']
    ['G', 'G', 'A', '$', 'T', 'T', 'G', 'C', 'C', 'A']
    ['A', 'G', 'G', 'A', '$', 'T', 'T', 'G', 'C', 'C']
    ['C', 'A', 'G', 'G', 'A', '$', 'T', 'T', 'G', 'C']
    ['C', 'C', 'A', 'G', 'G', 'A', '$', 'T', 'T', 'G']
    ['G', 'C', 'C', 'A', 'G', 'G', 'A', '$', 'T', 'T']
    ['T', 'G', 'C', 'C', 'A', 'G', 'G', 'A', '$', 'T']
    '''
matrix.sort()

#print matrix
for i in range(len(txt)):

    f.append(matrix [i][0])
    l.append(matrix [i][-1])

print ("\n\nMATRIX                                  F      L\n\n")
for x in range(len(txt)):

    print (matrix[x],'   ',f[x],'    ',l[x],' ')

unique_char = []
for i in l:
    if i not in unique_char:
        unique_char.append(i)
        print(i,end=" ")
unique_char.remove('$')
unique_char.sort()


for s in range (0,len(unique_char)):

    total_occurance.append(l.count(unique_char[s]))
    ##print(l.count(unique_char[s],end=" ")
f_new = []
for i in range(0,len(unique_char)):

    for j in range(0,len(l)):

        if unique_char[i] == l[j]:

            z = str(count)
            l[j] = l[j] + z
            count = count + 1
    j = 0 ; count = 0
    f_new.append(unique_char[i]*total_occurance[i])
    str1 += f_new[i]

f_new = list(str1)

for i in range(0,len(unique_char)):

    for j in range(0,len(f_new)):

        if unique_char[i] == f_new[j]:

            z = str(count)
            f_new[j] = f_new[j] + z
            count = count + 1
    j = 0 ; count = 0

f_new.insert(0,'$')
print ("F AND L AFTER INDEXING\n\n",f_new,l,)

i = 0
str1 = ""

while (1):
    recover.append(l[i])
    if l[i] == '$':
        recover = list(str1)
        break
    str1 += l[i]
    i = f_new.index(l[i])
str1 = (str1[0::2])
str1 = (str1[::-1])
print ("YOUR RECOVERD STRING :",str1)


'''
OUTPUT:


MATRIX                                  F      L


['$', 'T', 'T', 'G', 'C', 'C', 'A', 'G', 'G', 'A']     $      A  
['A', '$', 'T', 'T', 'G', 'C', 'C', 'A', 'G', 'G']     A      G  
['A', 'G', 'G', 'A', '$', 'T', 'T', 'G', 'C', 'C']     A      C  
['C', 'A', 'G', 'G', 'A', '$', 'T', 'T', 'G', 'C']     C      C  
['C', 'C', 'A', 'G', 'G', 'A', '$', 'T', 'T', 'G']     C      G  
['G', 'A', '$', 'T', 'T', 'G', 'C', 'C', 'A', 'G']     G      G  
['G', 'C', 'C', 'A', 'G', 'G', 'A', '$', 'T', 'T']     G      T  
['G', 'G', 'A', '$', 'T', 'T', 'G', 'C', 'C', 'A']     G      A  
['T', 'G', 'C', 'C', 'A', 'G', 'G', 'A', '$', 'T']     T      T  
['T', 'T', 'G', 'C', 'C', 'A', 'G', 'G', 'A', '$']     T      $  
F AND L AFTER INDEXING

 ['$', 'A0', 'A1', 'C0', 'C1', 'G0', 'G1', 'G2', 'T0', 'T1'] ['A0', 'G0', 'C0', 'C1', 'G1', 'G2', 'T0', 'A1', 'T1', '$']
YOUR RECOVERD STRING : TTGCCAGGA


'''


