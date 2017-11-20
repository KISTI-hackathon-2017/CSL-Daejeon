import sys
orig_stdout = sys.stdout
f = open('IK10%%.txt', 'w')
sys.stdout = f

import pymysql
# MySQL Connection 연결
conn = pymysql.connect(host = '115.88.201.51', user = 'iotr',password='iotr123',db='kisti')
# Connection 으로부터 Cursor 객체 생성
curs = conn.cursor()
# SQL 문 실행
sql =  'SELECT * FROM sensorParser WHERE node_id = \'IK10%%\' AND date(timestamp)=\'YYYY-MM-DD\''
curs.execute(sql) # Cursor 객체의 execute() 메서드를 사용하여 SQL 문장을 DB 서버에 보낸다
# 데이터 Fetch
rows = curs.fetchall()
print(rows)

sys.stdout = orig_stdout
f.close()
