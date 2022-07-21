


def solve(str):
    for i in range(6):
        flag = True
        guess = input("what is your guess? ")
        if len(guess) !=len(str):
            print(f"its a {len(str)} letter word brother its not {len(guess)}")
            flag = False
        while not flag:
            guess = input('Enter another guess! ')
            if len(guess) == len(str):
                flag = True
        for j in range(len(str)):
            if j == 0:
                if str == guess:
                    print(f'you guessed the correct word in {i+1} guesses, congrats!')
                    return
            if guess[j] == str[j]:
                print(guess[j], end='')
            elif guess[j] in str and guess.count(guess[j]) <= str.count(guess[j]):
                print(guess[j].upper(), end='')
            else:
                print('_', end='')
        print('')

import random
yordlelist = ['about', 'above','abuse','actor','acute','admit','adopt','adult','after','again','agent','agree','ahead','alarm',
'album','alert','alike','alive','allow','alone','along','alter','among','anger','Angle','angry','apart','apple','apply','arena',
'argue','arise','array','aside','asset','audio','audit','avoid','award','aware','badly','baker','bases','basic','basis','beach',
'began','begin','begun','being','below','bench','billy','birth','black','blame','blind','block','blood','board','boost','booth',
'bound','brain','brand','bread','breed','brief','bring','broad','broke','brown','build','built','buyer','cable','calif','carry',
'catch','cause','chain','chair','chart','chase','cheap','check','chest','chief','child','china','chose','civil','claim','class',
'clean','clear','click','clock','close','coach','coast','could','count','court','cover','craft','crash','cream','crime','cross',
'crowd','crown','curve','cycle','daily','dance','dated','dealt','death','debut','delay','depth','doing','doubt','dozen','draft',
'drama','drawn','dream','dress','drill','drink','drive','drove','dying','eager','early','earth','eight','elite','empty','enemy',
'enjoy','enter','entry','equal','error','event','every','exact','exist','extra','faith','false','fault','fiber','field','fifth',
'fifty','fight','final','first','fixed','flash','fleet','floor','fluid','focus','force','forth','forty','forum','found','frame',
'frank','fraud','fresh','front','fruit','fully','funny','giant','given','glass','globe','going','grace','grade','grand','grant',
'grass','great','green','gross','group','grown','guard','guess','guest','guide','happy','harry','heart','heavy','hence','henry',
'horse','hotel','house','human','ideal','image','index','inner','input','issue','japan','jimmy','joint','jones','judge',]
number = random.randint(1, len(yordlelist))

solve(yordlelist[number])