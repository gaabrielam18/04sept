n = int(input("Enter the length of the sequence: ")) # Do not change this line

num_1 = 1
num_2 = 2
num_3 = 3

print(num_1)
print(num_2)
print(num_3)

for i in range(0,n-3):
    sum_n = num_1 + num_2 + num_3
    num_1 = num_2
    num_2 = num_3
    num_3 = sum_n

    print(sum_n)
