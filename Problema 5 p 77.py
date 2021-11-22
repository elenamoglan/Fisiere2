with open ('pr5.txt', 'r') as f:
    C=f.readline()
n=[i for i in C if i in 'aeiouAEIOU']
print('Numarul vocalelor din fisier este', len(n))