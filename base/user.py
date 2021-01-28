from cx_Oracle import *
import cx_Oracle

def userAdd():
    print('')
    print('-' * 22)
    print('-' * 3 + '사용자등록 페이지' + '-' * 3)
    print('-' * 22)

    id = input('아이디?')
    while True:
        if id == '':
            id = input('아이디?')
        else:break
    name = input('이름?')
    while True:
        if name == '':
            name = input('이름?')
        else:break
    return (id,name)

def user_insert(data):
    conn = cx_Oracle.connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute(' insert into member(ID,Name) values(:1,:2) ',data)
    cur.close()
    conn.commit()
    conn.close()
    print('-' * 22)
    print('등록완료!')
    input(''' '엔터'하세요.''')

def changename():
    print('')
    print('-' * 22)
    print('-' * 3 + '이름변경 페이지' + '-' * 5)
    print('-' * 22)
    id = input('아이디는?')
    newname = input('바꿀 이름은?')
    return (newname,id)

def userupdate(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('update member set name= :1 where id = :2',data)
    cur.close()
    conn.commit()
    conn.close()
    print('-' * 22)
    print('업데이트!')
    print('')
    input(''' '엔터'하세요.''')

def deleteid():
    print('')
    print('-' * 22)
    print('-' * 3 + '아이디삭제 페이지' + '-' * 3)
    print('-' * 22)
    id = input('아이디는?')
    return (id,)

def userdelete(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('delete from member where id = :1', data)
    cur.close()
    conn.commit()
    conn.close()
    print('-' * 22)
    print('삭제완료!')
    print('')
    input(''' '엔터'하세요.''')

def subMenufir():
    while True:
        print('')
        print('-' * 22)
        print('-' * 3 + '사용자관리 페이지' + '-' * 3)
        print('-' * 22)
        print('1.사용자등록')
        print('2.유저명변경')
        print('3.사용자삭제')
        print('q.메인페이지')
        print('-' * 22)
        no = input('번호?')
        if no == '1':
            a = userAdd()
            user_insert(a)
        elif no == '2':
            xy = input('정말 변경?(y)')
            if xy == 'y' or xy == 'Y':
                b = changename()
                userupdate(b)
        elif no == '3':
            xy=input('정말 삭제?(y)')
            if xy == 'y' or xy == 'Y':
                c = deleteid()
                userdelete(c)
        elif no == 'q':
            break