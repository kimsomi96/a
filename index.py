from flask import Flask, render_template
import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="user1", db="pythonproj", charset="utf8")
cur = db.cursor() # 쿼리문의 결과를 가져옴

sql = "SELECT * from p_table"
cur.execute(sql)

data_list = cur.fetchall()



app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html', data_list=data_list) # 렌더하고싶은 파일명 입력

if __name__ == '__main__':
    app.run()
