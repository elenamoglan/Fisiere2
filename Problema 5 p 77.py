with open ('c:/Users/User/Desktop/input.txt', 'r') as f:
    C=f.readline()
n=[i for i in C if i in 'aeiouAEIOU']
with open ('c:/Users/User/Desktop/output.txt', 'w') as f:
    f.write('Vocalele: '+str(n))
print(f'Vocalele sunt {n}, iar numarul lor este {len(n)}')