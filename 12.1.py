#определите при каком наименьшем значении s программа выведет число 64
#s = int(input())
#n = 1
#while s <30:
#    s = s + 4
#    n = n * 2
#print(n)

#решение
for i in range(1, 100):
    s = i            #s будет равнятся числам от 1 до 100 по очереди
    n = 1
    while s < 30:
        s+=4
        n*=2
    if n==64:         #проверка при каком значении n = 64
        print(n, i)