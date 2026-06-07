from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Feedback('{self.name}', '{self.subject}')"

with app.app_context():
    db.create_all()

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title='Главная')

@app.route('/about')
def about():
    return render_template('about.html', title='О нас')

@app.route('/services')
def services():
    return render_template('services.html', title='Услуги')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Пользователь с таким email уже существует!', 'danger')
            return redirect(url_for('register'))

        new_user = User(
            username=username,
            email=email,
            password=password
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Регистрация прошла успешно!', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            flash('Произошла ошибка при регистрации!', 'danger')

    return render_template('register.html', title='Регистрация')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        new_feedback = Feedback(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        try:
            db.session.add(new_feedback)
            db.session.commit()
            flash('Ваше сообщение успешно отправлено!', 'success')
            return redirect(url_for('contact'))
        except:
            db.session.rollback()
            flash('Произошла ошибка при отправке сообщения!', 'danger')

    return render_template('contact.html', title='Контакты')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
