import pwn

r = pwn.remote('jh2i.com', 50031)
turnToShop = 1
while True:
    try:
        print('--------------------------------------------------------------------------------')
        msg = r.recv().decode()
        print(msg)
        msg = msg.split()
        gold = msg[msg.index('Gold:') + 1]
        level = msg[msg.index('level:') + 1]
        # print(msg)
        print('Gold : ', gold)
        print('Level : ', level)
        # browse the shop
        if level == '0':
            if turnToShop == 1:
                print('Browsing the shop...')
                turnToShop = 0
                r.sendline('6')
            else:
                print('Buying sword...')
                turnToShop = 1
                r.sendline('1')
        elif level == '1':
            if int(gold) < 1000:
                print('Going on a journey...')
                r.sendline('5')
            else:
                # level up to 3
                if turnToShop == 1:
                    print('Browsing the shop...')
                    turnToShop = 0
                    r.sendline('6')
                else:
                    print('Buying bow...')
                    turnToShop = 1
                    r.sendline('2')
        elif level == '3':
            if int(gold) < 2000:
                print('Plundering the pirates...')
                r.sendline('4')
            else:
                # level up to 5
                if turnToShop == 1:
                    print('Browsing the shop...')
                    turnToShop = 0
                    r.sendline('6')
                else:
                    print('Buying axe...')
                    turnToShop = 1
                    r.sendline('3')
        elif level == '5':
            if int(gold) < 10000:
                print('Raiding the cyclops...')
                r.sendline('3')
            else:
                # level up to 7
                if turnToShop == 1:
                    print('Browsing the shop...')
                    turnToShop = 0
                    r.sendline('6')
                else:
                    print('Buying axe...')
                    turnToShop = 1
                    r.sendline('4')
        elif level == '7':
            if int(gold) < 100000:
                print('Fighting a dragon...')
                r.sendline('2')
            else:
                # level up to 10
                if turnToShop == 1:
                    print('Browsing the shop...')
                    turnToShop = 0
                    r.sendline('6')
                else:
                    print('Buying tank...')
                    turnToShop = 1
                    r.sendline('5')
        elif level == '10':
            print('Defeating the gnomes...')
            r.sendline('1')
            break
        else:
            print('OOPS!')
            break
    except:
        print('End of transmission.')
        break
