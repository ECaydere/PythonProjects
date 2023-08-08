import os
from datetime import datetime

ogrList=[]
systemUser=[
    ["Erdem","Karakoç","erdem@gmail.com","12345",0],
    ["Emre","Çaydere","emre@gmail.com","12345",1],
    ["Eylül","Ersoy","eylul@gmail.com","12345",2],
    ["İren","Uyanık","iren@gmail.com","12345",3]
]
loop=False
user=None
def log(islem):
    global user
    veri=user[0]+" "+user[1]+" işlem :"+islem+" Tarih : "+str(datetime.now())+"\n"
    yazdir(data=veri,dosya="log.csv")
def login():
    global loop
    global user
    while True:
        userName=input("Kullanıcı Adınız : ")
        userPass=input("Şifreniz : ")
        if (len(userName)>10) and ("@" in userName) and (len(userPass)>4):
            for usex in systemUser:
                if (userName==usex[2]) and (userPass==usex[3]):
                    loop=True
                    user=usex
                    log("Sisteme giriş yaptı")
                    break
            if loop==False:
                print("Kullanıcı verisi doğrulanamadı")
            else:
                break
        else:
            print("Kullanıcı adı ve şifresi hatalı!")
            print("Lütfen Tekrar Giriş Yapınız")




def dosyaAc(file="ogrData.csv",tip="r"):
    d=open(os.getcwd()+os.sep+file,tip,encoding="utf-8")
    return d
def oku(file=None):
    dosya=dosyaAc() if file==None else dosyaAc(file)
    veri=dosya.readlines()
    dosya.close()
    return veri
def yazdir(data="",dosyaTip="a+",dosya="ogrData.csv"):
    dosya=dosyaAc(file=dosya,tip=dosyaTip)
    dosya.write(data)
    dosya.close()
def ogrKayit():
    soru=["Adı : ","Soyadı : ","Sınıfı : ","Mail Adresi : "]
    ogrVeri=[]
    for i in soru:
        ogrVeri.append(input(i))
    yazdir(";".join(ogrVeri)+"\n")
    log(ogrVeri[0]+" "+ogrVeri[1]+" isimli kullanıcıyı kaydetti")
    dataOku()
def dataOku():
    global ogrList
    ogrList.clear()
    veri=oku()
    for satir in veri:
        ogrList.append(satir.replace("\n","").split(";"))
def dataWrite():
    global ogrList
    veri=""
    for ogr in ogrList:
        veri+=";".join(ogr)+"\n"
    yazdir(veri,dosyaTip="w")
def ogrListele():
    global ogrList
    print("{:*^30}".format("Öğrenci Listesi")) 
    s=1
    for ogr in ogrList:
        print(s,". "+ogr[0]+" "+ogr[1])  
        s+=1
    print("*"*30)
    log(" öğrencileri listeledi.")
def ogrSil():
    global ogrList
    ogrListele()
    i=input("""
Çıkmak için q harfini giriniz!
Silme istediğiz öğrenci numarasın giriniz :\n""")
    if i!="q":
        if i.isdigit() and int(i)>0 and int(i)<=len(ogrList):
            ogrDel=ogrList[int(i)-1]
            del ogrList[int(i)-1]
            dataWrite()
            log("-".join(ogrDel)+" isimli kullanıcıyı sildi.")
            print("--",i," numaralı öğrenci silidin")
        else:
            print("Hatalı veri girişi")
def detayaList():
    global ogrList
    ogrListele()
    i=input("Öğrenci no giriniz : ")
    if i!="q":
        if i.isdigit() and int(i)>0 and int(i)<=len(ogrList):
             print(f"""
             Adı : {ogrList[int(i)-1][0]}
             Soyadı : {ogrList[int(i)-1][1]}
             Sınıf : {ogrList[int(i)-1][2]}
             Mail : {ogrList[int(i)-1][3]}
             """) 
             log(ogrList[int(i)-1][0]+" "+ogrList[int(i)-1][1]+" isimli öğrencinin detay bilgilerini erişti.")   
        else:
            print("Hatalı veri girişi")
def ogrGuncelle():
    global ogrList
    ogrListele()
    i=input("Öğrenci no giriniz : ")
    if i!="q":
        if i.isdigit() and int(i)>0 and int(i)<=len(ogrList):
            soru=["Adı : ","Soyadı : ","Sınıfı : ","Mail Adresi : "]
            ogrVeri=[]
            for s in soru:
                ogrVeri.append(input(s))
            durum=input("Kayıt Yapılsın mı (E/H) :")
            if durum.lower() == "e":
                eski=ogrList[int(i)-1]
                ogrList[int(i)-1]=ogrVeri
                log("-".join(eski)+" kullanıcı verisini "+"-".join(ogrList[int(i)-1])+" şeklinde güncelledi")
                dataWrite() 
            else:
                print("İşlem İptal Edildi!")
        else:
            print("Hatalı veri girişi")

login()

if loop==True:
    dataOku()
    print(user[0],user[1],"hoş geldiniz!")
    #1 öğrenci listeler
    #2 öğrenci list ve datay liste
    #3 ekle liste güncelle detay
    #4 ekle sil güncelle detay
    rol=[
        [ogrListele],
        [ogrListele,detayaList],
        [ogrKayit,ogrListele,detayaList,ogrGuncelle],
        [ogrKayit,ogrListele,ogrSil,detayaList,ogrGuncelle]
    ]
    mesajIcerik=[
        ["1. Öğrenci Listele"],
        ["1. Öğrenci Listele","2. Öğrenci Detay"],
        ["1. Öğrenci Kayıt","2. Öğrenci Listele","3. Öğrenci Detay","4. Öğrenci Güncelle"],
        ["1. Öğrenci Kayıt","2. Öğrenci Listele","3. Öğrenci Sil","4. Öğrenci Detay","5. Öğrenci Güncelle"]
    ]
    islem=rol[user[4]]

    mesaj="""
    Yapmak istediğini işlem Nedir?
    \t{}
    Çıkmak için q harfine basınız.
    """.format("\n \t".join(mesajIcerik[user[4]]))

    while loop:
        i=input(mesaj)
        if i.lower() == "q":
            loop=False
        else:
            if i.isdigit() and int(i)>0 and int(i)<=len(islem):
                islem[int(i)-1]()
            else:
                print("Yanlış Değer girdiniz")

    else:
        log(" Sistemden çıkış yaptı.")
        print("Sistemden çıkış yapıldı")
