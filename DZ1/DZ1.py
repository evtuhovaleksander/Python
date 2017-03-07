#На входе есть список команд. Его вы задаете сами любым удобным способом.
#Далее вы случайным образом (модуль random) разбиваете команды по парам и формируете сетку
#плей-офф - думаю все знают, как проводятся такие турниры (1/8-я, 1/4-я, полуфиналы и финал).
#Далее проводите матчи - счет определяется случайным образом. По окончании турнира нужно иметь возможность
#запросить и посмотреть как выступила в турнире та или иная команда - с кем на какой стадии играла, счет матча.
#Если что-то непонятно по условию - спросите и я уточню.
import random


def play_match(a,b,ia,ib):
    print('now playing '+a+'  vs  '+b)
    z=random.randrange(0,10)
    x=random.randrange(0,10)
    print('match results '+str(z)+'x'+str(x))
    if(z>x):
        return[ia,(ia,ib,z,x)]
    else:
        return [ib,(ia,ib,z,x)]




team_mas=['t0','t1','t2','t3','t4','t5','t6','t7']
i=""
#for i in range(0,7):
#    i=input('Input team'+str(i)+' name \n')
#    team_mas.append(i)

print('Finished team inputing\n')

print('Printing team info\n')
for i in team_mas:
    print(i+"\n")

print('Now making new order')

order=[]#[-1,-1,-1,-1,-1,-1,-1,-1]
i=0
while(i!=8):
    tmp=random.randrange(0,8)
    if not tmp in order:
        order.append(tmp)
        print(order)
        i+=1


print('print new order')
for i in order:
    print(i)


print('Now Matching')

matches=[]
new_order=[]

print('1/8 final matches')
for i in range(0,7,2):
    tmp=play_match(team_mas[order[i]],team_mas[order[i+1]],order[i],order[i+1])
    new_order.append(tmp[0])
    matches.append(tmp[1])

print('1/4 final matches')
for i in range(0,3,2):
    tmp=play_match(team_mas[order[i]],team_mas[order[i+1]],order[i],order[i+1])
    new_order.append(tmp[0])
    matches.append(tmp[1])

print('1/2 final matches')
for i in range(0,1,2):
    tmp=play_match(team_mas[order[i]],team_mas[order[i+1]],order[i],order[i+1])
    new_order.append(tmp[0])
    matches.append(tmp[1])



inp=""
while(inp!="out"):
    inp=input('input index of comand')
    x=int(inp)
    for i in matches:
        if(i[0]==x or i[1]==x):
            print('There was a match')
            print(team_mas[i[0]]+'  vs  '+team_mas[i[0]])
print(new_order)
print(matches)
