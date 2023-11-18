def rec_area(lenght,width):
    if lenght>=width:
        return lenght*width
    

width_lenght_A=input('enter the width and the lenght of the apartment A(seperate them with comma): ')    
width_lenght_B=input('enter the width and the lenght of the apartment B(seperate them with comma): ')
counter=0
lenght_A=''
width_A=''
lenght_B=''
width_B=''
for i in width_lenght_A:
    if i==',':
        counter+=1
        continue
    elif counter==1:
        lenght_A+=i
    else:
        width_A+=i
            

counter=0
for i in width_lenght_B:
    if i==',':
        counter+=1
        continue
    elif counter==1:
        lenght_B+=i
    else:
        width_B+=i
            

if rec_area(int(lenght_A),int(width_A))>rec_area(int(lenght_B),int(width_B)):
    print('Apartment A')
elif   rec_area(int(lenght_A),int(width_A))<rec_area(int(lenght_B),int(width_B)):
    print('Apartment B')
else:
    print('their size are the same')      
   