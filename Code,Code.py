#01 Strings-Zaheln
'Dies ist ein Blatt, das viele Zeilen Code enthalten soll. Unter anderem mit Strings und Zahlen'
'Wie auch die Zahl',(5) 

#02 Listen
'Hier werde ich eine kurze Liste mit dem Inhalt von unserem Lager erstellen'
Inventar_short = ['Gabelstapler', 'Leiter' , 'Webermur920' ]
# Ich muss noch einen Eintrag in die Liste aufnehmen
Inventar_short.append('Schaufel')
# aber die Leiter haben wir nicht mehr
Inventar_short.remove('Leiter')
print(Inventar_short)

#03 if




#04 Loops
Inventar_short = ['Gabelstapler', 'Leiter' , 'Webermur920' ] 
for P in Inventar_short:
    print(P)

for x in 'Gabelstapel':
    print(x)

for j in Inventar_short:
    print(j)
    if j == 'Webermur92':
        break
    
for k in Inventar_short:
     print(k)
     if k == 'Leiter':
         continue
     
#05 Functionen

