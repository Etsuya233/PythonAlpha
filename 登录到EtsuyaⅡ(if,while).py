print('欢迎来到MekOs')
print('输入c以查看关于，输入s以跳过。')

cs = True
while cs:
    css = input('请输入: ')
    if css == 'c':
        print('我喜欢你，拿滴克来。')
        cs = False
    elif css == 's':
        print('也要看！！！信不信我上了你！')
        cs = False
    else:
        print('请选择正确的选项！')

un = True
while un:
    unn = input('请输入用户名: ')
    if unn == 'Etsuya':
        print('用户名正确。')
        un = False
    elif unn != 'Etsuya':
        print('用户名错误！请重新输入！')
        
pw = True
while pw:
    pww = input('请输入密码: ')
    if pww == 'fnndp':
        print('密码正确，所以.....诶嘿嘿。')
        pw = False
    elif pww != 'fnndp':
        print('密码错误！请重新输入！')
        
#这次比之前的那次好多了qwq
