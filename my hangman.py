import random

name=input("enter your name")
print(name,"welcome to hangman game")
print("best of luck",name)
print("lets start the game")
word_list=["lan","jian","susma"]
chosen_word=random.choice(word_list)
word_lenght=len(chosen_word)

display=[]
for i in range(word_lenght):
    display=display+list("_")

lives=7
game_over=False
while not game_over:
    guess=input("enter a guess : ").lower()
    for i in range(word_lenght):
        letter=chosen_word[i]
        if letter==guess: 
            display[i]=letter

    if guess not in chosen_word:
            lives-=1
            if letter!=guess and lives==6:
                print("-------\n"
                      "|      \n"
                      "|      \n"
                      "|     \n"
                      "|\n"
                      "|\n"
                      "|\n")
                # break
            if letter!=guess and lives==5:    
                print("-------\n"
                      '|      |\n'
                      '|      \n'
                      "|     \n"
                      "|     \n"
                      '|\n'
                      '|\n')
                # break
            if letter!=guess and lives==4: 
                print("--------\n"
                      "|       |\n"
                      "|       0\n"
                      "|      \n"
                      "|\n"
                      "|\n"
                      "|\n")
                # break
            if letter!=guess and lives==3: 
                print("--------\n"
                      "|       |\n"
                      "|       0\n"
                      "|      /|\ \n"
                      "|\n"
                      "|\n"
                      "|\n")
                # break
            if letter!=guess and lives==2: 
                print("--------\n"
                      "|       |\n"
                      "|       0\n"
                      "|      /|\ \n"
                      "|       | \n"
                      "|\n"
                      "|\n")
            if letter!=guess and lives==1: 
                print("--------\n"
                      "|       |\n"
                      "|       0\n"
                      "|      /|\ \n"
                      "|       | \n"
                      "|      / \ \n"
                      "|\n"
                      "|\n")
                print("you lose")
                break
    print(display)  
    
    if "_" not in display:
        game_over=True
        print("you win")  



# a=[[12],[23],20,[3],[80],9,[7]]
# a1=[]
# i=0
# j=0
# while i<len(a):
#     if type(a[i])==int:
#         b=a[i]
#         a1.append(b)
#     else:
#         b=a[i][j]
#         a1.append(b)
#     i+=1
# print(a1)
# o/p=[12,23,3,80,9.7]



# dic1={"a":1,"b":2,"c":3}
# dic2={"d":4,"e":5,"f":6}
# a=[]
# b=[]
# c=[]
# d=[]
# e={}
# f={}
# for x in dic1:
#     a.append(x)
#     b.append(dic1[x])
# for y in dic2:
#     c.append(y)
#     d.append(dic2[y])  
# i=0
# while i<len(a):
#     j=0
#     while j<len(d):
#         e[a[i]]=d[j]
#         j+=1
#         i+=1
# l=0
# while l<len(c):
#     k=0
#     while k<len(b):
#         f[c[l]]=b[k]
#         k+=1
#         l+=1
# print(e)
# print(f)


# a=[1,2,3,4,5,6,7,8,9,0,1,2,9]
# b=[]
# i=0
# while i<len(a):
#     if i%4==0:
#         # a.append(20)
#         c=a[i]
#         b.append(c)
#         b.append(20)
#     i+=1
# print(b)


# a=int(input("enter "))
# b=int(input("enetr"))
# c=int(input("enetr"))
# if a>b and a>c:
#     print("a,oldest")
# elif a<b and a<c:
#     print("a,yougest")
# elif b>a and b>c:
#     print(b,"oldest")
# elif b<a and b<c:
#     print("b youngest")
# elif c>b and c>a:
#     print("c oldest")
# elif c<b and c<a:
#     print(c,"youngest")


# a=[[1,2,3],[4,5],[6,7,8]]
# i=0
# j=0
# s=0
# s1=0
# s2=0
# l=[]
# l1=[]
# l2=[]
# k=[]
# for i in a:
#     for j in i:
#         if j==i[0]:
#             s+=j
#         elif j==i[1]:
#             s1+=j
#         elif j==i[2]:
#             s2+=j
# l.append(s)
# l1.append(s1)
# l2.append(s2)
# k.append(l)
# k.append(l1)
# k.append(l2)
# print(k)



# a=[1,2,3,4,5,6,7,8,9,10]
# b=[]
# # c=int(input("enter the number"))
# i=0
# while i<len(a):
#     d=[a[i],a[i+1]]
#     # c=[a[i+1]]
#     b.append(d)
#     # b.append(c)
#     i+=2
# print(b)
