import pickle
import datetime

#FAYLNI TO'LIQLIGACHA O'QISH
# with open('test.txt') as fayl:
#     pi = fayl.read()
# print(pi)
# fayl.close()

#faylni qatorma qator o'qish
# with open('test.txt') as fayl:
#     talabalar = fayl.readlines()
#     print(talabalar)
# talaba = [talaba.rstrip('\n') for talaba in talabalar]
# print(talaba)

# talabas = []
# for  talaba in talabalar:
#     talabas.append(talaba.rstrip('\n'))    
# print(talabas)
# fayl.close()

# with open('Alimurod.txt', 'w') as fayl:
#     for i in range(10):
#         fayl.write('Alimurod\n')

# with open('Hello world.txt', 'w') as fayl:
#     text = "Hello World!"
#     a=[]
#     for i in text:
#         a.append(i)
#         for j in a:
#             print(j, end="")
#             fayl.write(j)
#         fayl.write("\n")
#         print("\n")

# with open('Alimurod.txt', 'a') as fayl:
#     fayl.write("Akbarov\n")
#     fayl.write("2004.09.26\n")



data = {
    'ichimliklar' : {
        "kola" : {
            'miqdori' : 50,
            'price' : 1500,
            'date' : datetime.datetime.now().strftime("%x")
        },
        "pepsi" : {
            'miqdori' : 50,
            'price' : 1500,
            'date' : datetime.datetime.now().strftime("%x")
        },
        "fanta" : {
            'miqdori' : 50,
            'price' : 1500,
            'date' : datetime.datetime.now().strftime("%x")
        },
        "flesh" : {
            'miqdori' : 50,
            'price' : 1500,
            'date' : datetime.datetime.now().strftime("%x")
        }
    }
}

# print(data)
print(data.get('ichimliklar').keys())
print(len(data.get('ichimliklar').keys()))

# with open("database.txt", 'wb') as fayl:
#     pickle.dump(data, fayl) 

# with open("database.txt", 'rb') as fayl:
#     data2 = pickle.load(fayl)

# print(data2)

















# fayl.close()