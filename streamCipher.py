#enkripsi ASCII dengan kode biner
def enkripsi_ascii_biner(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        kode_biner = bin(kode_ascii)[2:]  #Mengabaikan awalan "0b" pada hasil biner
        hasil_enkripsi += kode_biner + " "
    return hasil_enkripsi

#dekripsi ASCII dengan kode biner
def deskripsi_ascii_biner(teks):
    teks_biner = teks.split()
    hasil_dekripsi = ""
    for biner in teks_biner:
        kode_ascii = int(biner, 2)
        karakter = chr(kode_ascii)
        hasil_deskripsi += karakter
    return hasil_deskripsi

#enkripsi ASCII dengan kode desimal
def enkripsi_ascii_desimal(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        hasil_enkripsi += str(kode_ascii) + " "
    return hasil_enkripsi

#dekripsi ASCII dengan kode desimal
def deskripsi_ascii_desimal(teks):
    teks_kode = teks.split()
    hasil_deskripsi = ""
    for kode in teks_kode:
        karakter = chr(int(kode))
        hasil_deskripsi += karakter
    return hasil_deskripsi

#enkripsi ASCII dengan kode heksadesimal
def enkripsi_ascii_heksadesimal(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        kode_heksa = hex(kode_ascii)[2:]  #Mengabaikan awalan "0x" pada hasil heksadesimal
        kode_heksa_kapital = kode_heksa.upper()
        hasil_enkripsi += kode_heksa_kapital + " "
    return hasil_enkripsi

#dekripsi ASCII dengan kode heksadesimal
def deskripsi_ascii_heksadesimal(teks):
    teks_heksa = teks.split()
    hasil_dekripsi = ""
    for heksa in teks_heksa:
        kode_ascii = int(heksa, 16)
        karakter = chr(kode_ascii)
        hasil_deskripsi += karakter
    return hasil_deskripsi

#enkripsi ASCII dengan kode oktal
def enkripsi_ascii_oktal(teks):
    hasil_enkripsi = ""
    for karakter in teks:
        kode_ascii = ord(karakter)
        kode_oktal = oct(kode_ascii)[2:]  #Mengabaikan awalan "0o" pada hasil oktal
        hasil_enkripsi += kode_oktal + " "
    return hasil_enkripsi

#dekripsi ASCII dengan kode oktal
def deskripsi_ascii_oktal(teks):
    teks_oktal = teks.split()
    hasil_deskripsi = ""
    for oktal in teks_oktal:
        kode_ascii = int(oktal, 8)
        karakter = chr(kode_ascii)
        hasil_deskripsi += karakter
    return hasil_deskripsi

#untuk melakukan deskripsi dengan kode biner,desimal,heksa,oktal
def deskripsi_berbagai_format(teks, format_type):
    if format_type == 'biner':
        decoded_text = int(teks, 2)
        decoded_text = chr(decoded_text)  #Mengonversi hasil deskripsi numerik ke dalam huruf abjad
        return decoded_text
    elif format_type == 'desimal':
        decoded_text = int(teks, 10)
        decoded_text = chr(decoded_text)  
        return decoded_text
    elif format_type == 'heksadesimal':
        decoded_text = int(teks, 16)
        decoded_text = chr(decoded_text)  
        return decoded_text
    elif format_type == 'oktal':
        decoded_text = int(teks, 8)
        decoded_text = chr(decoded_text)  
        return decoded_text

if __name__ == '__main__':
    print ('-----------------------------------')
    print ('    Nama        : Munis Zulhusni   ')
    print ('    Nim         : A11.2021.13693   ')
    print ('    Kelas       : A11.4302         ')
    print ('-----------------------------------')   
    
    option = int (input ('1. Enkripsi\n2. Deskripsi\nPilih Option                 : '))
    if option == 1:
        teks = input ('Masukan pesan (Plaintext)    : ')
        hasil_enkripsi_biner = enkripsi_ascii_biner(teks)
        print('Hasil Enkripsi Biner         :',hasil_enkripsi_biner)
        
        hasil_enkripsi_desimal = enkripsi_ascii_desimal(teks)
        print('Hasil Enkripsi Desimal       :',hasil_enkripsi_desimal)
        
        hasil_enkripsi_heksadesimal = enkripsi_ascii_heksadesimal(teks)
        print('Hasil Enkripsi Heksadesimal  :',hasil_enkripsi_heksadesimal)
        
        hasil_enkripsi_oktal = enkripsi_ascii_oktal(teks)
        print('Hasil Enkripsi Oktal         :',hasil_enkripsi_oktal)
        
    if option == 2:
        format_type = input('Masukan format\n(biner/desimal/heksadesimal/oktal): ')
        teks = input(f'Masukan pesan   ({format_type})           : ')
        hasil_deskripsi = deskripsi_berbagai_format(teks, format_type)
        print(f'Hasil Deskripsi ({format_type})           : {hasil_deskripsi}')
        
    else:
        print ('TIDAK VALID! PILIH OPSI LAIN!')    
