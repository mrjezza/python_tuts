#check tax condtions

country = input('What country are you shopping in? ')
state = input('what state are you in? ')
if country == 'au':
    if state in ('nsw', 'vic', 'act'):
        tax = 0.15
    elif state == qld:
        tax = 0.333
    else:
        tax = 0
    print ('your tax is ' + str(tax))
else:
    print('no tax for lucky you')

