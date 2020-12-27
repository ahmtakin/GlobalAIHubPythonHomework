name=input("Please enter your name: ")
print("Welcome {}".format(name))
word=input("please enter a word: ") #tahmin edilmesi istenen kelime girilir
print("_ "*(len(word))) #kullanıcıya ipucu olması açısından kelime uzunluğu verilir.

myword=set(word) #harfleri kontrol etmek adına oluşturulmuş küme
newset=set() #girilen doğru harfler için açılan küme

a=[] #hata sayılarını içinde tutacak liste
myguess=["_ "for j in range(len(word))] #kelimeyi oluşturacağımız liste

def guess(letters): #tahmin etme işlemini sağlayan fonksiyon
    if not letters in myword:
        a.append("x")#hataları listeye atıyor. değişken olarak tanımladığımda değişken her seferinde tekrar sıfır olduğu için bu yöntemi seçtim.
        hanging(len(a)) #asma işlemi
    else:
        newset.add(letters)#doğru olan harfleri kümeye atama
        for i in range(len(word)):
            if letters==word[i]: #kelimeyi oluşturduğumuz listeye girilen tahminlerin atıldığı blok.
                myguess[i]=letters
def monitor(liste):#listemizi sıralı olarak yazdırmamızı sağlayan fonksiyon
    for i in liste:
        print(i,end="")
def hanging(a): #asma fonksiyonu
    if a==1:
        print("\n|\n|\n|\n|")
    elif a==2:
        print("\n|-----|\n|\n|\n|")
    elif a==3:
        print("\n|-----|\n|     O\n|\n|")
    elif a==4:
        print("\n|-----|\n|     O\n|     |\n|")
    elif a==5:
        print("\n|-----|\n|     O\n|    /|\n|")
    elif a==6:
        print("\n|-----|\n|     O\n|    /|""\\""\n|")
    elif a==7:
        print("\n|-----|\n|     O\n|    /|""\\""\n|    /")
    elif a==8:
        print("\n|-----|  GAME OVER\n|     O The answer was:\n|    /|"f"\\      {word}""\n|    /"" \\")

while len(a)<8: #hanging fonksiyonu asma işlemini sekiz adımda gerçekleştiriyor.
    letter=input("\nPlease enter a letter: ") #kullanıcıdan tahmin harf isteme kısmı
    guess(letter)
    monitor(myguess)
    if len(a)==8: #hata sınırına ulaşınca fonksiyonu kapatan blok
        break
    if len(newset)==len(myword): #tahmin doğru olunca fonksiyonu kapatan blok
        print("\nyou won!")
        break