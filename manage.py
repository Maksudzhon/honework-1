# Users={
#     "Jhon":{
#         "email":"John0213@gmail.com",
#         "password":"qaz123plm",
#         "age":"21"
#     },
#     "Steve":{
#         "email":"Steve0213@gmail.com",
#         "password":"qaz1234plm",
#         "age":"34"
#     },
#     "Tom":{
#         "email":"Tom987@gmail.com",
#         "password":"qaz1234plm",
#         "age":"18"
#     }
# }

# email=input("Email kiriting >>> ")
# parol=input("Parol kiriting >>> ")

# if email == "John0213@gmail.com" and parol == "qaz123plm":
#     print("You're Log In!")
# else:
#     print("You aren't Log In")
#     restart=input("Do you want to add your email? >>> ")
#     if restart == "Xa" or "xa" or "Ha" or "ha":
#         new = input("Email kiriting >>> ")
#         book = input("Parol kiriting >>> ")
#     elif new == "Steve0213@gmail.com" and book == "qaz1234plm":
#         print("You're Log In!")
#     else:
#         print("False")

# Names=["Mike", "Anna", "Michael", "Tom"]

# son=1
# for item in Users:
#     print(f"{son}-Foydalanuvchi emaili: {Users[item]["email"]}   paroli:{Users[item]["parol"]}   yoshi:{Users[item]["age"]}")
#     son +=1 


# parol = input("Parolni Kiriting >>> ")

# mystery_parol = ""

# for i in parol:
#     i = "*"
    
#     mystery_parol += i
    
# print(mystery_parol)



# while True:
#     search = input("Username >>> ")
#     confirm = input("Password >>> ")
#     confirm2 = ""
#     ask1 = input("Would you like hide this password? (yes/no) >>> ")
#     if search in Users and confirm == Users[search]['password'] and ask1=='yes':
#         for i in confirm:
#             i = "*"
#             confirm2 +=i
#             print(f"Username:{search}\nEmail:{Users[search]['email']}\nPassword:{confirm2}\nAge:{Users[search]['age']}")
#     elif ask1=='no':
#         print(f"Username:{search}\nEmail:{Users[search]['email']}\nPassword:{Users[search]['password']}\nAge:{Users[search]['age']}")
#     else:
#         ask = input("User not found! Are you want to add a new User? (yes/no) >>> ")
#         if ask == 'yes':
#             email=input("Email >>> ")
#             password=input("password >>> ")
#             age=input("Age >>> ")
#             Users[search] = {
#                 "email":email,
#                 "password":password,
#                 "age":age
#             }
#             print(f"Username:{search}\nEmail:{Users[search]['email']}\nPassword:{Users[search]['password']}\nAge:{Users[search]['age']}")
#         else:
#             print(f"Username:{search}\nEmail:{Users[search]['email']}\nPassword:{Users[search]['password']}\nAge:{Users[search]['age']}")





# ismlar = input("Ism kiriting >>> ").split()
# number = 1
# for ism in sorted(ismlar):
#     print(f"{number}) {ism.title()}")
#     number += 1
# def salomdunyo(son1, son2 , amal):
    
#     if amal == "+":
#         print(son1 + son2)
#     elif amal == "-":
#         print(son1 - son2)
#     elif amal == "*":
#         print(son1 * son2)
#     elif amal == "/":
#         print(son1 / son2)
#     else:
#         print("ergkhjelfkdsjagljihulygjtfrdesdtfyugiop[oiuytrewqadesrdtfgyhj")


# salomdunyo(input("Amalni kiriting >>> "))
books={
    "Sherlock Holmes":{
        "Author":"Abdullajon Shoqosimov",
        "Price":"67$",
        "Description":"Sherlock Holmes short story collections in order. The Adventure of Sherlock Holmes",
        "Year":"2003 yil"
    },
    "Sid Kageno":{
        "Author":"Abdullajon Shoqosimov",
        "Price":"489$",
        "Description":"Sid Kageno short story collections in order. The Adventure of Sidn Kageno",
        "Year":"2003 yil"
    },
    "William Moriarti":{
        "Author":"Abdullajon Shoqosimov",
        "Price":"167$",
        "Description":"William Moriarti short story collections in order. The Adventure of William Moriarti",
        "Year":"2003 yil"
    }
}

def bookshop():
    while True:
        book_search=input("Kitob nomini yoki kitobga oid ma'lumot kiriting >>> ")
        if book_search == "Sherlock Holmes":
            print(books["Sherlock Holmes"])
        elif book_search == "Sid Kageno":
            print(books["Sid Kageno"])
        elif book_search == "William Moriarti":
            print(books["William Moriarti"])
        else:
            new_book=input("Bu kitob topilmadi , Yangi kitob qushasizmi ? ha/yuq  >>> ")
            if new_book == "ha":
                Author=input("Author >>> ")
                Price=input("Price >>> ")
                Description=input("Description >>> ")
                Year=input(" Yili >>> ")
                books[book_search] = {
                    "Author":Author,
                    "Price":Price,
                    "Description":Description,
                    "Year":Year
                }
                print(f"Bookname:{book_search}\nAuthor:{books[book_search]['Author']}\nPrice:{books[book_search]['Price']}\nDescription:{books[book_search]['Description']}\nYear:{books[book_search]['Year']}")
            else:
                break
                
bookshop()
