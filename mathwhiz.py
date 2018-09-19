from pwn import *
conn = remote('offsec-chalbroker.osiris.cyber.nyu.edu', 1236)
conn.recvuntil(':')
conn.sendline('ll3056')
conn.recvuntil('??')
nums = {'ZERO':0,'ONE':1,'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9}

while True:
    conn.recvline()
    equation = conn.recvline()
    print(equation)
    x = equation.split()
    print(x)
    param1 = x[0]
    operation = x[1]
    param2 = x[2]
    try:
        intVal = int(param1,0)
    except ValueError:
        lst = param1.split('-')
        itr = 0
        for num in lst:
            if (num in nums):
                lst[itr] = nums[num]
            else:
                continue
            itr += 1
        temp = map(str, lst)
        param1 = ''.join(temp)

    try:
        intVall = int(param2,0)
    except ValueError:
        lstt = param2.split('-')
        itrr = 0
        for numm in lstt:
            if (numm in nums):
                lstt[itrr] = nums[numm]
            else:
                continue
            itrr += 1
        tempp = map(str, lstt)
        param2 = ''.join(tempp)



    if (operation == '+'):
        result = str(int(param1,0)+int(param2,0))
        conn.sendline(result)


    elif (operation == '-'):
        result = str(int(param1,0)-int(param2,0))
        conn.sendline(result)


    elif (operation == '*'):
        result = str(int(param1,0)*int(param2,0))
        conn.sendline(result)
    
    else:
        break
f = conn.recvline()
print(f)
