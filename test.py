import os


os.system ('clear')

jawab = input ('Jawaban : ')

if (jawab.lower() != 'y'):
    print ('JAWABAN SALAH')
elif (jawab.lower() == 'y'):
    print ('TERJAWAB SUDAH')
