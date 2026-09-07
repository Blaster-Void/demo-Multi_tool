import socket
import time ,datetime
import calendar
from requests import get
colors={'green':'\x1b[32m',
        'red':'\x1b[31m',
        'grey':'\x1b[30m',
        'yelow':'\x1b[33m',
        'pepor':'\x1b[35m',
        'blue':'\x1b[34m',
        'lightblue':'\x1b[36m',
        'defalt':'\x1b[0m',
        }
hostname=socket.gethostname()
while True:
    User_input=input(f'\n(S/s)Show Local ip\n(C/c)Calendar\n{colors['red']}(Q/q)Quit{colors['defalt']}\n{colors['pepor']}{hostname}:{colors['defalt']}')


    if User_input.lower()=='s':

        User_input=input(f'(L/l)Local ip\n(P/p)Public ip\n{colors['pepor']}{hostname}:{colors['defalt']}')

        if User_input.lower()=='l':
            print(f'{hostname} local ip:{colors['yelow']}{socket.gethostbyname(hostname)}{colors['defalt']}')

        elif User_input.lower()=='p':
            print('a')
            print(f'{colors['grey']}Internet most connected... Please wait a moment.{colors['defalt']}',end='\r',flush=True)
            time.sleep(0.3)
            ip = get('https://api.ipify.org').content.decode('utf8')
            print(f'{hostname} public ip:{colors['yelow']}{ip}                         {colors['defalt']}')

    elif User_input.lower()=='c':

        date=datetime.datetime.now()
        year=date.year
        month=date.month
        day=date.day
        weekday=datetime.datetime(year=year,month=month,day=day).strftime('%A')
        rangeofm=calendar.monthrange(year=year,month=month)
        rangeofm=rangeofm[-1]
        monthname=date.strftime('%b')

        


        print(f'{colors["yelow"]}{monthname}{colors["defalt"]}')
        print(f'{weekday}')

        days=[i for i in range(1,rangeofm+1)]
        for i in days:
            if day==i:
                if i%7==0:
                    print(f"{colors['red']}{i:2} {colors['defalt']}",end='\n')
                    continue
                else:
                    print(f"{colors['red']}{i:2} {colors['defalt']}",end='')
                    continue
                
            if i%7==0:
                print(f'{i:2}')
            else:
                print(f'{i:2} ',end='')

        print(f'\n\n{year} {month} {day}')

    elif User_input.lower()=='q':
        exit()
