import os
from keysdict import *
from set import Huruf


pilih = -1
while (int(pilih) <= 0) or (int(pilih) >= 4):
    os.system ("clear")

    # MENU
    print (f'{Huruf.hijaugelap}TERMUX PROFILES :')
    print ("="*17,"\n")
    for nomor in profiles:
        print (f'{nomor}. {profiles [nomor]}')
    print (Huruf.netral)        

    # OPSI INPUT
    pilih = input ("\nPilih Opsi No. >>  ")

    # PROSES INPUT NILAI PILIH
    if (pilih == '1'):
        nama_xkey = profiles [pilih]
        xkey = xkeys [nama_xkey]    
    elif (pilih == '2'):   
        nama_xkey = profiles [pilih]
        xkey = xkeys [nama_xkey]    
    elif (pilih == '3'):   
        nama_xkey = profiles [pilih]
        xkey = xkeys [nama_xkey]    
    elif (pilih.lower() == 'q'):
        os.system('clear')
        print("Terima Kasih atas pilihanmu,\ntelah menggunakan X - Key")
        exit()
    else:
        pilih = -1

# PROSES TULIS/BUAT FILE
eksekusi = 'z'
while (eksekusi.lower() != 'y'):    
    os.system ('clear')
    eksekusi = input (Huruf.kuningterang + "Yakin akan melakukan perubahan TERMUX EXTRA-KEY (y/C) >>  " + Huruf.netral)
    if (eksekusi.lower() == 'y'):    
        try:
            # ignore -- os.mkdir ('/home/recki/demo')
            os.mkdir ("/data/data/com.termux/files/home/.termux")
        except:
            pass
        # ignore -- file = open ("/home/recki/demo/termux.properties",'w')
        file = open ("/data/data/com.termux/files/home/.termux/termux.properties",'w')
        file.write (f"extra-keys = {xkey}")
        file.close()

        # TERMUX RELOAD SETTINGS
        os.system ("termux-reload-settings")

        # INFORMASI        
        os.system ('clear')
        print (f"{Huruf.biruterang}\nSELAMAT, {nama_xkey}{Huruf.mencolok} :SUKSES DITERAPKAN{Huruf.netral}\n")
        kembali = input ('Ingin kembali ke Menu Awal (y/N) >>  ')
        if (kembali.lower() == 'y'):
            os.system ('python3 main.py')
        else:
            exit()
    elif (eksekusi.lower() == 'c'):    
        os.system ('python3 main.py')
        break
    else:
        eksekusi = 'z'
