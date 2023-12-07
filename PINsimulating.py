password_bank={'sam':8682,'smith jr.':98038,'kerala':9804}
for u in range (0,5):
    name=input('user name: ')
    if name in password_bank.keys():
        for i in range (0,3):
            pin=input('enter pin: ')
            if int(pin) in password_bank.values():
                print('correct pin! app accessed')
                break
            else:
                print('wrong pin! '+str(2-i)+' attempts left.')
        break
    else:
        print('incorrect user name! '+str(4-u)+' Attempts left')
