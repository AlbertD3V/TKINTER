def fixo(msg = 'oi', qqcoisa = 'topilhas, 1 real'):
    qqcoisa = qqcoisa.replace('a','4')
    qqcoisa = qqcoisa.replace('i', '1')
    qqcoisa = qqcoisa.replace('e','3')
    qqcoisa = qqcoisa.replace('o','0')
    msg = msg.replace('o', '0')
   
    print (msg, qqcoisa)

fixo()
