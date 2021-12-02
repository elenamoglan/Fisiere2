note=[]
f=open('c:/Users/User/Downloads/Lista Clasei 11A.txt', 'r', encoding='utf-8')
L=list(f)
f.close()
f=open('c:/Users/User/Desktop/Lista_Clasei_11A.txt', 'w', encoding='utf-8')
f.write(f'Nume\tPrenume\t\tNota\tLimba\n')
a=open('c:/Users/User/Desktop/Elevii_Ce_Studiaza_LimbaEngleza.txt', 'w', encoding='utf-8')
b=open('c:/Users/User/Desktop/Elevii_Ce_Studiaza_LimbaGermana.txt', 'w', encoding='utf-8')
c=open('c:/Users/User/Desktop/Elevii_Ce_Studiaza_AlteLimbiStraine.txt', 'w', encoding='utf-8')
for i in range(len(L)):
    elev = L[i].split()
    n=int(input(f"Nota elevului {elev[0]} {elev[1]}:"))
    note.append(n)
    l=str(input(f'Limba straina aleasa:'))
    f.write(f'{elev[0]}\t{elev[1]}\t\t{str(n)}\t{l}\n')
    if str(l).lower() == 'engleza':
        a.write(f'{elev[0]}\t{elev[1]}\t{str(n)}\n')
    elif str(l).lower() == 'germana':
        b.write(f'{elev[0]}\t{elev[1]}\t{str(n)}\n')
    else:
        c.write(f'{elev[0]}\t{elev[1]}\t{str(n)}\t{l}\n')
a.close()
b.close()
c.close()
f.write(f'Media celor {len(L)} elevi este {sum(note)/float(len(L))}')
f.close()