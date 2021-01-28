from base import *

try:
    def menu():
        while True:
            print('')
            print('-' * 22)
            print('-' * 3 + '주사위 게임 v0.1' + '-' * 4)
            print('-' * 22)
            print('1.사용자관리')
            print('2.게임시작')
            print('3.순위보기')
            print('q.종료하기')
            print('-' * 22)
            no = input('번호?')
            if no == '1':
                user.subMenufir()
            elif no == '2':
                start.submenuthr()
            elif no == '3':
                rank.subMenusec()
            elif no == 'q':
                print('')
                print('-' * 22)
                print('-' * 7 + '종료 하기' + '-' * 7)
                print('-' * 22)
                exit()
            else:
                no = input('번호?')
    menu()
except KeyboardInterrupt:

    exit(0)





