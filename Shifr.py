alfavit='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
print('\nШифр Цезаря')
print('Введите 1, если хотите зашифровать текст и 2, если расшифровать')
A=0
    
otvet=int(input())
if otvet==1:
    print('Напишите текст (на русском языке), который нужно зашифровать')
    try:
        text=input()
        print('Сдвиг шифровки')

        try:
            sdvig=int(input())
            text_z=text.lower() 
            text_new=''
            
            while sdvig > 33:
                sdvig -= 33
            k = sdvig 

            for ic in text_z:
                position=alfavit.find(ic)
                new_position=position+k
                
                if ic in alfavit:
                    text_new=text_new + alfavit[new_position]
                else:
                    text_new=text_new+ic
                
            if text==text_new:
                A=1
                print('Вы ввели или символ, или текст не на русском языке')
            else:
                print ('Зашифрованный текст:', text_new)
        except IndexError:
            A=1
            print('Шаг сдвига слишком большой.  ')

        except ValueError:
            A=1
            print('Должна быть цифра.')

    except TypeError:
        A=1
        print('Введите текст.')

if otvet==2:
    print('Напишите текст (на русском языке), который нужно расшифровать')
    text=input()

    print('Сдвиг шифровки')
    try:
        sdvig=int(input())

        text_z=text.lower() 
        text_new='' 
        while sdvig > 33:
                sdvig -= 33
        k = sdvig

        for ic in text_z:
            position=alfavit.find(ic)
            new_position=position-k
            if ic in alfavit:
                text_new=text_new + alfavit[new_position]
            else:
                text_new=text_new+ic
        if text==text_new:
            A=1
            print('Вы ввели или символ, или текст не на русском языке.  ')
        else:
            print ('Расшифрованный текст:', text_new)

    except IndexError:
            A=1
            print('Шаг сдвига слишком большой.  ')
    except ValueError:
            A=1
            print('Должна быть цифра.  ')
            
if (otvet<1 or otvet>2):
    A=1
    print('Вы ввели не ту цифру.  ') 
    
while A==1:
    try:   
        print('\nВведите 1, если хотите зашифровать текст и 2, если расшифровать') 
        otvet=int(input())
        if otvet==1:
            print('Напишите текст (на русском языке), который нужно зашифровать')
            try:
                text=input()
                print('Сдвиг шифровки')
                try:
                    A==0
                    sdvig=int(input())

                    text_z=text.lower() 
                    text_new=''
                    while sdvig > 33:
                        sdvig -= 33
                    k = sdvig 

                    for ic in text_z:
                        position=alfavit.find(ic)
                        new_position=position+k
                        
                        if ic in alfavit:
                            text_new=text_new + alfavit[new_position]
                        else:
                            text_new=text_new+ic
                        
                    if text==text_new:
                        A==1
                        print('Вы ввели или символ, или текст не на русском языке.  ')
                    else:
                        print ('Зашифрованный текст:', text_new)

                except IndexError:
                    A==1
                    print('Шаг сдвига слишком большой.  ')

                except ValueError:
                    A==1
                    print('Должна быть цифра.  ')

            except TypeError:
                A==1
                print('Введите текст.  ')
        if otvet==2:
            print('Напишите текст (на русском языке), который нужно расшифровать')
            text=input()

            print('Сдвиг шифровки')
            try:
                sdvig=int(input())

                text_z=text.lower() 
                text_new='' 
                while sdvig > 33:
                        sdvig -= 33
                k = sdvig

                for ic in text_z:
                    position=alfavit.find(ic)
                    new_position=position-k
                    if ic in alfavit:
                        text_new=text_new + alfavit[new_position]
                    else:
                        text_new=text_new+ic
                if text==text_new:
                 print('Вы ввели или символ, или текст не на русском языке.  ')
                else:
                    print ('Расшифрованный текст:', text_new)
 
            except IndexError:
                print('Шаг сдвига слишком большой.  ')
            except ValueError:
                print('Должна быть цифра.  ')
                
        if (otvet<1 or otvet>2):
            print('Вы ввели не ту цифру.  ') 
    
    except ValueError:
        print('Нужно ввести 1, если хотите зашифровать текст и 2, если расшифровать. ')
