from flask import Flask,request,render_template,redirect,url_for,flash
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST']= "localhost"
app.config['MYSQL_DB']= "patient"
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= "abc123"
app.config['MYSQL_CURSORCLASS']="DictCursor"
app.secret_key="myapp"
conn = MySQL(app)

@app.route('/')
def front():
    return render_template("front.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/signup1', methods = ['POST', 'GET'])
def signup1():
    if request.method  == 'POST':
        user_name1 = request.form['username']
        password1 = request.form['password']
        email = request.form['email']
        con=conn.connection.cursor()
        sql = "insert into signup(username,password,email) values  (%s,%s,%s)"
        result=con.execute(sql,(user_name1,password1,email))
        con.connection.commit()
        con.close()
        return  redirect(url_for('login'))
        
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/book')
def book():
    return render_template("book.html")

@app.route('/book1', methods = ['POST', 'GET'])
def book1():
    if request.method  == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        tel = request.form['tel']
        gender = request.form['gender']
        age = request.form['age']
        bloodGroup = request.form['bloodGroup']
        con=conn.connection.cursor()
        sql = "insert into book(firstName,lastName,email,tel,gender,age,bloodGroup) values  (%s,%s,%s,%s,%s,%s,%s)"
        result=con.execute(sql,(firstName,lastName,email,tel,gender,age,bloodGroup))
        con.connection.commit()
        con.close()
        return  redirect(url_for('confirmation'))
        
    return render_template('book.html')

@app.route('/confirmation')
def confirmation():
    return render_template("confirmation.html")

@app.route('/login1', methods = ['POST', 'GET'])
def login1():
    if request.method  == 'POST' or 'GET':
        user_name1 = request.form['username']
        email = request.form['email']
        password1 = request.form['password']
        con=conn.connection.cursor()
        sql = "select * from signup WHERE username= %s and password=%s and email=%s"
        result=con.execute(sql,(user_name1,password1,email))
        if result:
            con.connection.commit()
            con.close()
            return redirect(url_for('index'))
        else:
            return "Invalid Username or Password"

'''@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login1', methods = ['POST', 'GET'])
def login1():
    if request.method  == 'POST' or 'GET':
        user_name1 = request.form['user_name']
        password1 = request.form['password']
        con=conn.connection.cursor()
        sql = "select * from signup WHERE username= %s and  password=%s"
        result=con.execute(sql,(user_name1,password1))
        if result:
            con.connection.commit()
            con.close()
            return redirect(url_for('about'))
        else:
            return "Invalid Username or Password"
        
@app.route('/about')
def about():
    return render_template("about.html")
               
                
    return render_template("login.html") 

@app.route('/signup1', methods = ['POST', 'GET'])
def signup1():
    if request.method  == 'POST':
        user_name1 = request.form['user_name']
        password1 = request.form['password']
        con=conn.connection.cursor()
        sql = "insert into signup(username,password) values  (%s,%s)"
        result=con.execute(sql,(user_name1,password1))
        con.connection.commit()
        con.close()
        return  redirect(url_for('login'))
        
    return render_template('signup.html')'''





if __name__ == "__main__":
    app.run(debug=True)