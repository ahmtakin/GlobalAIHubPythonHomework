import random as rnd #not belirleme için random modülünü kullandım
students=["Ahmet Akın","Ömer Cengiz","Mert Çobanov","Elif Yiğit","Kutay Akalın"] #öğrencileri listeye tanımladım
name=input("Please enter your name: ") 
mistake=0 #girişteki hataları saymayı sağlayan değişken
crscnt=0 #
courses=[] #girilen dersleri içinde tutan liste
grades=[x for x in range(0,101)] #not aralığını belirleyen liste
exams={"midterm":rnd.choice(grades),"final":rnd.choice(grades),"project":rnd.choice(grades)} #notlandırma
tkngrd=list(exams.values()) #sözlükteki not değerlerini toplayan liste
average=((tkngrd[0]*3)/10)+((tkngrd[1]*5)/10)+((tkngrd[2]*2)/10) #ortalamayı tutan değişken
def course(courses, lesson):#girilen dersleri listeye ekleme fonksiyonu
    while len(lesson.strip(" "))==0: #boşluk girilmesini engelleyen döngü
        lesson=input("Please enter a course: ") #boşluk girilirse yeni input alınır
    courses.append(lesson.strip(" ")) #girilen ders adlarının sonlarını boşluksuz hale getiren kısım

while not name in students: #girilen adın öğrenciler arasında olmadığı durumda çalışan döngü
    if mistake<=1: 
        name=input("Your name is not True. Please try again: ")
        mistake+=1
        if mistake==2 and not name in students: #üç hata durumunda çalışan kısım
            print("Please try again later...")
            break

if name in students:  
    print("Hello {}".format(name)) #selamlama kısmı
    while len(courses)<5: #beş ders girilmesini sağlayan kısım
        lesson=input("Please enter a course: ")
        course(courses,lesson)
    coursesnum= enumerate(courses,1) #girilen dersleri yazdıracak değişken
    print(list(coursesnum)) 
    
    chosenlessons=[int(i) for i in input("Please enter the row number of courses you want to take(You must choose at least 3 courses and you can choose maximum 5 courses): ").split()] #girilen derslerin sıra numarasına göre ders seçtiren kısım
    
    while True:
        while not 3<=len(chosenlessons)<=5: #istenen sayıda ders girilmesini sağlayan kısım
            chosenlessons=[int(i) for i in input("Please try again. Please enter the row number of courses you want to take(You must choose at least 3 courses and you can choose maximum 5 courses): ").split()]    
        try:
            for j in range(len(chosenlessons)):
                chosenlessons[j]=courses[chosenlessons[j]-1] #seçilen dersleri listeye atan kısım
            print(list(enumerate(chosenlessons,1))) #seçilen dersleri yazdıran kısım
            break
        except (ValueError,IndexError): #hata ayıklama aracı index hataları ve integer girilmemesi durumlarında çalışıyor.
            chosenlessons=[int(i) for i in input("Undefined lesson.Please try again. please enter the row number of courses you want to take(You must choose at least 3 courses and you can choose maximum 5 courses): ").split()]
    
    while True:
        try:
            examtake= int(input("Please pick a lesson that you want to learn your grades(Please enter the row number of the course.): ")) #istenen dersin notlarını getirmek için input alan kısım
            print("Your grades for ",chosenlessons[examtake-1]," course are: ",exams) #notları yazdırma kısmı
            break
        except (ValueError, IndexError): #hata ayıklama aracı index hataları ve integer girilmemesi durumlarında çalışıyor.
            print("ERROR!! Please just enter row numbers and be careful about existence of that row number!")
    
    print(f"Your average grade at {chosenlessons[examtake-1]} course is: {average:.2f}") #formatlanmış ortalamayı bastıran kısım
    
    if average>=90: #geçip kalma ortalamalarını belirleyen bloklar
        print("Your passing grade is AA.")
    elif 90>average>=70:
        print("Your passing grade is BB.")
    elif 70>average>=50:
        print("Your passing grade is CC.")
    elif 50>average>=30:
        print("Your passing grade is DD.")
    else:
        print("Your grade is FF. You have failed this course.")