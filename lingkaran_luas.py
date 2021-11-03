def lingkaran():
    while True:
        try:
            r = int(input("Masukkan jari-jari : "))
        except ValueError:
            print("input tidak valid")
        else:
            if r % 7 == 0:
                luas     =22/7 *r *r 
                keliling =2*(22/7*r)
                hasil    =[luas, keliling]
            else:
                luas     =3.14 * r * r
                keliling =2 * 3.14 * r
                hasil    = [luas, keliling]
        break 
    return hasil
print("bangun datar")
print("1.lingkaran")

pilihan = input("Masukkan Pilihan (1) : ")

if pilihan == "1":
    hasil = lingkaran()
    
    print("luas lingkaran :{}".format(hasil[0]))
    print("keliling lingkaran :{}".format(hasil[1]))

else:
    print("Input tidak valid")