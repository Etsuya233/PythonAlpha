print('欢迎来到MekOs')
print('请输入 v 来了解此软件，输入 o 为已阅。')
reader = input('请输入: ')
if reader == 'v':
    print('Yes')
elif reader == 'o':
    print('Angry！')
else:
    print('请输入正确的字符!')
    qwq = True
    while qwq:
        xyb = input('Please: ')
        if xyb == 'v':
            print('Yes')
            qwq = False
        elif xyb == 'o':
            print('Angry!')
            qwq = False
        else:
            print('请输入正确的字符！')

un = input('请输入用户名: ')
if un == 'Etsuya':
    print('Yes')
elif un != 'Etsuya':
    qwqwq = True
    while qwqwq:
        un = input('请输入用户名: ')
        if un == 'Etsuya':
            qwqwq = False
        elif un != 'Etsuya':
            print('请重新输入用户名！')

pw = input('请输入密码: ')
if pw == "fnndp":
    print('Yes')
elif pw != "fnndp":
    qqwq = True
    while qqwq:
        pw = input('请输入密码: ')
        if pw == 'fnndp':
            qqwq = False
        elif pw != 'fnndp':
            print('请重新输入用户名!')
            
#其实还可以写得更简单的 我这时为什么那么傻写那么长

print('已完成！')
print('Etsuya!')
