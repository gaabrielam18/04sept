# 
num_int = int(input("Input a number: "))    # Do not change this line
# Fill in the missing code

max_int = num_int 
# Lesum tölu frá notendanum ef hún er stærri en 0 þá gerum við þetta:
# num_int á að vera stærri en 0 síðan er ég að búa til nyja breytu en 
# ef hún er stærri en max talan þá gef ég  max tölunni nýtt gildi sem á 
# að vera num_int (talan sem notandinn slær inn) 
# annars prentum við stærstu tölu sem við höfum séð áður 
while num_int > 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)
    