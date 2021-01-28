import cx_Oracle
from base import rank
import random
# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# import main

def userUpdate(data):
    conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute(''' UPDATE result SET point = point+1 WHERE id = :1 ''', data)
    cur.close()
    conn.commit()
    conn.close()


def usersUpdate(data):
    conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''UPDATE result SET point = point+1 WHERE id = :1 ''', (data[0],))
    cur.execute('''UPDATE result SET point = point-1 WHERE id = :1 ''', (data[1],))
    cur.close()
    conn.commit()
    conn.close()

def computerGame():
    while True:
        user = random.randint(1, 6)
        comp = random.randint(1, 6)
        id = input('아이디?')
        cnt = rank.userexist((id,))
        if cnt <= 0:
            print(id+'정보가 없습니다.');
            print('-' * 22)
        else:
            print(id, ':', user)
            print('컴퓨터:', comp)
            if user > comp:
                userUpdate((id,))
                print('-' * 22, '\n' + id, '승!')
            elif user < comp:
                print('-' * 22, '\n' + '컴퓨터 승!')
            elif user == comp:
                print('-' * 22, '\n' + '무승부');
            break
    return (id,)

def usersGame():
    while True:
        fstid = input('유저1 아이디?')
        cnt = rank.userexist((fstid,))
        if cnt <= 0:
            print(fstid + '의 정보가 없습니다.');
            continue
        scdid = input('유저2 아이디?')
        cnt = rank.userexist((scdid,))
        if cnt <= 0:
            print(scdid + '의 정보가 없습니다.');
            continue
        fstuser = random.randint(1, 6)
        scduser = random.randint(1, 6)
        print('-' * 22)
        print(fstid, ':', fstuser)
        print(scdid, ':', scduser)
        if fstuser > scduser:
            usersUpdate((fstid, scdid))
            print('-' * 22, '\n' + fstid, '승!')
        elif fstuser < scduser:
            usersUpdate((scdid, fstid))
            print('-' * 22, '\n' + scdid, '승!')
        else:
            print('-' * 22, '\n' + '무승부');
        break
    return (fstid, scdid)

def submenuthr():
    while True:
        print('')
        print('-' * 22)
        print('-' * 3 + '주사위배틀 페이지' + '-' * 3)
        print('-' * 22)
        print('1.컴퓨터와배틀')
        print('2.유저들과배틀')
        print('q.메인페이지')
        print('-' * 22)
        no = input('번호?')

        if no =='q':
            print('메인으로')
            break

        while True:
            if no == '1':
                print('')
                print('-' * 22)
                print('-' * 5 + '컴퓨터와 배틀' + '-' * 5)
                print('-' * 22)
                data1 = computerGame()
                userUpdate(data1)
            elif no == '2':
                print('')
                print('-' * 22)
                print('-' * 5 + '유저들과 배틀' + '-' * 5)
                print('-' * 22)
                data2 = usersGame()
                usersUpdate(data2)
            print('')
            input(''' '엔터'하세요.''')
            print('')
            print('r.다시하기')
            print('q.게임페이지')
            reNo = input('번호?')
            if reNo == 'r':
                continue
            elif reNo == 'q':
                break
            else:
                print('다시 입력하세요.')


