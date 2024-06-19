# Python program for simple Calculator
operator=input("Choose operator (+,-,*,/):")
num=input("Enter numbers seperate with :").split(',')
print(num)
total=0
if operator=="+":
    for element in num:
        total+=int(element)
elif operator=="-":
    total=int(num[0])-int(num[1])
    for i in range(2,len(num)):
        total = total- int(num[i])
elif operator=="*":
    total=1
    for element in num:
        total*=int(element)
elif operator=="/":
    # 1 2 3 4 5
    total=int(num[0])/int(num[1])
    for i in range(2,len(num)):
        total = total/ int(num[i])
print(f"Answer for {operator} is : {total}")


# OUTPUT

# Choose operator (+,-,*,/):+
# Enter numbers seperate with ',:1,2,3,4,5
# ['1', '2', '3', '4', '5']
# Answer for + is : 15

# Choose operator (+,-,*,/):-
# Enter numbers seperate with ',:1,2,3,4,5
# ['1', '2', '3', '4', '5']
# Answer for - is : -13

# Choose operator (+,-,*,/):*
# Enter numbers seperate with ',:1,2,3,4,5
# ['1', '2', '3', '4', '5']
# Answer for * is : 120

# Choose operator (+,-,*,/):/
# Enter numbers seperate with ',:1,2,3,4,5
# ['1', '2', '3', '4', '5']
# Answer for / is : 0.008333333333333333
