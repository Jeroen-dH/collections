#listen van de dagen
dagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag','zaterdag','zondag']
werkdagen = ['maandag','dinsdag','woensdag','donderdag','vrijdag']
weekend = ['zaterdag','zondag']
omdagen = ['zondag', 'zaterdag', 'vrijdag', 'donderdag', 'woensdag', 'dinsdag', 'maandag']
omwerkdagen = ['vrijdag', 'donderdag', 'woensdag', 'dinsdag', 'maandag' ]
omweekend = ['zondag', 'zaterdag']
#vraag voor welke dagen je wilt weten
vraag = input("welke dagen wil je weten? (A)Dagen, (B)Werkdagen, (C)weekend, (D)omgekeerde dagen, (E)omgekeerde werkdagen, (F)omgekeerd weekend: ")
#veranderd de variable 'b' op basis van het antwoord 
def dagen1(hoi2):
    if vraag == 'A'.lower(): 
        b = 'dagen'
        list(dagen,b)
    if vraag == 'B'.lower(): 
        b = 'werkdagen'
        list(werkdagen,b)
    if vraag == 'C'.lower(): 
        b = 'weekend dagen'
        list(weekend,b)
    if vraag == 'D'.lower(): 
        b = 'omgekeerde dagen'
        list(omdagen,b)
    if vraag == 'E'.lower(): 
        b = 'omgekeerde werkdagen'
        list(omwerkdagen,b)
    if vraag == 'F'.lower(): 
        b = 'Omgekeerd weekenddagen'
        list(omweekend,b)   
#print de dagen van de week van de gekozen dagen         
def list(hoi,b):
    dag = len(hoi)
    a1 = dag
    print('De',b, 'van de week zijn: ')
    for a in range(a1):
        print(hoi[a])
dagen1(vraag)