def printText(userInput):
    """This project spells out integers between 0 and 1000 """
    unitsMapping = {'0':'',
                    '1':' One',
                    '2':' Two',
                    '3':' Three',
                    '4':' Four',
                    '5':' Five',
                    '6':' Six',
                    '7':' Seven',
                    '8':' Eight',
                    '9': 'Nine'
                    }
    
    tensMapping = {'0':'',
                   '2':' Twenty',
                   '3':' Thirty',
                   '4':' Forty',
                   '5':' Fifty',
                   '6':' Sixty',
                   '7':' Seventy',
                   '8':' Eighty',
                   '9':' Ninety'
                   }
    
    teensMapping = {'10':' Ten',
                    '11':' Eleven',
                    '12':' Twelve',
                    '13':' Thirteen',
                    '14':' Fourteen',
                    '15':' Fifteen',
                    '16':' Sixteen',
                    '17':' Seventeen',
                    '18':'Eighteen',
                    '19':' Nineteen'
                    }
    
    numLength = len(userInput)
    numText = ''

    units = userInput[numLength - 1] if numLength >= 1 else '0'

    tens = userInput[numLength - 2] if numLength >= 2 else '0'

    hundreds = userInput[numLength - 3] if numLength >= 3 else '0'

    if (hundreds != '0'):
        numText = numText + unitsMapping[hundreds] + ' Hundred'

    if (int(userInput) > 99 and int(userInput)%100 != 0):
        numText = numText + ' and'

    if (tens == '1'):
        numText = numText + teensMapping[tens+units]

    elif (tens ==  '0'):
        numText = numText + unitsMapping[units]
    else:
        numText = numText + tensMapping[tens] + unitsMapping[units]

    return numText

if __name__ == "__main__":
    userInput = input('Enter an integer smaller than 1000: ')
    
    while True:
        try:
            userNum = int(userInput)
            if userNum > 999:
                userInput = input ('Number is too big. Enter an integer smaller than 1000: ')
            else:
                break
        except ValueError:
            userInput = input('Youd did not enter an integer. Enter an integer smaller than 1000: ')
    
    print(printText(userInput).strip())
