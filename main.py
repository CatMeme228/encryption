print('Шифр Цезаря')
print('Введите слово')
inp= input()
print('Введите сдвиг')
indent= int(input())
alphabetsmall= 'abcdefghijklmnopqrstuvwxyz'
alphabetbig= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
inpmass=[]
end= ''
for i in range(len(inp)):
    inpmass.append(inp[i])
    if str(inpmass[i]).isupper() == True:
        letter = alphabetbig.find(str(inpmass[i]))
        final = int(letter) + indent
        if final<25:
            end= end + alphabetbig[final]
        else:
            final2= final-26
            end = end + alphabetbig[final2]
    elif str(inpmass[i]).islower() == True:
        letter = alphabetsmall.find(str(inpmass[i]))
        final = int(letter) + indent
        if final < 25:
            end= end + alphabetsmall[final]
        else:
            final2= final-26
            end = end + alphabetsmall[final2]
    else:
        end= end + inpmass[i]
print(end)
