from cx_Oracle import *
import cx_Oracle

def userexist(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select count(*) cnt from member where id = :1', data)
    cnt = tuple(cur)[0][0]
    cur.close()
    conn.close()
    return cnt

def checkAll():
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute(''' select sum(r.point)point, r.id, max(m.name)name from member m  join result r on (m.id=r.id) group by r.id order by point desc ''')
    for point, id, name in cur:
        print(id,name, point )

    cur.close()
    conn.close()

def checkMe(data):
    conn = connect('hr/hr@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('''select * from result where id = :1 ''',data)
    for id,point in cur:
        pass
    cur.close()
    conn.close()
    return id, point

def subMenusec():
    while True:
        print('')
        print('-' * 22)
        print('-' * 3 + '순위확인 페이지' + '-' * 5)
        print('-' * 22)
        print('1.전체랭킹확인')
        print('2.나의점수확인')
        print('q.메인페이지')
        print('-' * 22)
        no = input('번호?')
        if no == '1':
            print('')
            print('-' * 22)
            print('-' * 5 + '랭킹확인 페이지' + '-' * 3)
            print('-' * 22)
            checkAll()
            print('')
            input(''' '엔터'하세요.''')
        elif no == '2':
            print('-' * 22)
            print('-' * 5 + '점수확인 페이지' + '-' * 3)
            print('-' * 22)
            id = input('검색할 아이디?')
            cnt = userexist((id,))
            if cnt > 0:
                id, point = checkMe((id,))
                print('%s의 점수는 %d 입니다.' % (id, point))
                print('')
                input(''' '엔터'하세요.''')
            else:
                print('%s의 정보가 없습니다.'%id)
                print('')
                input(''' '엔터'하세요.''')
        elif no == 'q':
            break






