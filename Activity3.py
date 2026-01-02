math = int(input("What did you get on your math exam?"))
english = int(input("What did you get on your english exam?"))
SS = int(input("What did you get on your SS exam?"))
science = int(input("What did you get on your science exam?"))
PE = int(input("What did you get on your PE exam?"))

total = math + english + SS + science + PE
print("Your total marks are", total) 

avg = total // 5
print(avg)

if 91<avg<100:
    print("A1")
elif 81<avg<91:
    print("A2")
elif 71<avg<81:
    print("B1")
elif 61<avg<71:
    print("B2")
elif 51<avg<61:
    print("C1")
elif 41<avg<51:
    print("C2")
elif 31<avg<41:
    print("D")
elif 21<avg<31:
    print("E1")
elif 0<avg<21:
    print("E2")
else:
    print("Invalid input")