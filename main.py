from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector

class ContentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    link = StringField('Link', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)

app.config['SECRET_KEY'] = 'aloha' 


mydb =mysql.connector.connect(host='localhost', 
                              user ='root', 
                              password ='',
                              database = 'resources')


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/boas', methods=['GET'])
def boas():
    return render_template('boas.html')


@app.route('/science', methods=['GET', 'POST'])
def science():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO science (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM science WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM science;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('science'))

    return render_template('science.html', form=form, resources=resources)


@app.route('/math', methods=['GET', 'POST'])
def math():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO math (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM science WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM math;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('math'))

    return render_template('math.html', form=form, resources=resources)


@app.route('/statistic', methods=['GET', 'POST'])
def statistic():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO statistic (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM statistic WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM statistic;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('statistic'))

    return render_template('statistic.html', form=form, resources=resources)


@app.route('/econometrics', methods=['GET', 'POST'])
def econometrics():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO econometrics (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM econometrics WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM econometrics;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('econometrics'))

    return render_template('econometrics.html', form=form, resources=resources)


@app.route('/coding', methods=['GET', 'POST'])
def coding():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO coding (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM coding WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM coding;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('coding'))

    return render_template('coding.html', form=form, resources=resources)


@app.route('/eda', methods=['GET', 'POST'])
def eda():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO eda (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM eda WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM eda;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('eda'))

    return render_template('eda.html', form=form, resources=resources)


@app.route('/ml', methods=['GET', 'POST'])
def ml():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO ml (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM ml WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM ml;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('ml'))

    return render_template('ml.html', form=form, resources=resources)


@app.route('/dl', methods=['GET', 'POST'])
def dl():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO dl (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM dl WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM dl;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('dl'))

    return render_template('dl.html', form=form, resources=resources)


@app.route('/mlop', methods=['GET', 'POST'])
def mlop():
    form = ContentForm()

    if form.validate_on_submit():
        # Handle form submission for ContentForm
        my_cursor = mydb.cursor()
        sql = f"INSERT INTO mlop (title, description, link) VALUES ('{form.title.data}','{form.description.data}','{form.link.data}')"
        my_cursor.execute(sql)
        mydb.commit()

        # Fetch resources based on the search query if available
    query = request.form.get('query')
    if query:
        my_cursor = mydb.cursor()
        sql = f"SELECT title, description, link FROM mlop WHERE description LIKE '%{query}%' OR description LIKE '%{query}%'"
        my_cursor.execute(sql)
        resources = my_cursor.fetchall()
    else:
        my_cursor = mydb.cursor()
        my_cursor.execute("SELECT title, description, link FROM mlop;")
        resources = my_cursor.fetchall()
    
    cursor_list = []  # Initialize cursor_list as a list

    for resource in resources:
        title = resource[0]
        description = resource[1]
        link = resource[2]
        cursor_list.extend([title, description, link])
        print(cursor_list)
    
    if form.validate_on_submit():
            return redirect(url_for('mlop'))

    return render_template('mlop.html', form=form, resources=resources)


if __name__ == '__main__':
    app.run(debug=True)
