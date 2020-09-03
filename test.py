

def enterGrades(cutoffAgrade=85):
    name = input('Enter name: ')
    
    gotAgrade = False
    while not gotAgrade:
        Score = int(input('Please enter your score from your test:'))

        if Score > 100:
            print("Invalid, please try again")
        elif Score >= 85:
            print("A, Good Job %s" %(name))
            gotAgrade = True
        elif Score >= 70:
            print('B, Do a little better next time %s' %name)
        elif Score >= 55:
            print('C, You need to pay more attention or your going to do test again')
        elif Score >= 0:
            print('Failed, See Teacher after school %s' %name)
        else:
            print('Invalid')

enterGrades()
