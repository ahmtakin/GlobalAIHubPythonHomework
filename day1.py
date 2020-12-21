first=input("string bir ifade giriniz: ")#input fonksiyonu default olarak ifadeleri str kabul ettiği için
print("{} ifadesi {} türü bir ifadedir.".format(first,type(first)))#koşullu ifade de kullanmamak için böyle bir yol tercih ettim.
second=int(input("integer bir ifade giriniz: "))
print("{} ifadesi {} türü bir ifadedir.".format(second,type(second)))
third=int(input("integer bir ifade giriniz: "))
print(f"{third} ifadesi {type(third)} türü bir ifadedir.")
fourth=float(input("float türü bir ifade giriniz: "))
print(f"{fourth} ifadesi {type(fourth)} türü bir ifadedir.")
fifth=list(map(str,input("birden fazla ifade girebilirsiniz: ").split()))#bunu önceden biraz bilgim olduğu için kullanmayı tercih ettim.
print("{}ifadesi {} türü bir ifadedir.".format(fifth,type(fifth)))