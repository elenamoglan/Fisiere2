with open('c:/Users/User/Desktop/ListaClasei11A.txt', 'r', encoding='utf-8') as f:
    L=list(f)
note=[]
for i in range(1,len(L)+1):
    n=int(input(f"Nota elevului {i}:"))
    note.append(n)
print(f'Nume\tPrenume\tNota')
for i in range(len(L)):
    c=L[i].split()
    print(f'{c[0]}\t{c[1]}\t{note[i]}')
print(f'Media celor {len(L)} elevi este {sum(note)/float(len(L))}')