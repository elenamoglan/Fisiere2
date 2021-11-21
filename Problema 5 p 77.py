with open ('input.txt', 'r') as f:
    C=list(f.readline())
n=[i for i in C if i in 'aeiouAEIOU']
print('Numarul vocalelor din fisier este', len(n))