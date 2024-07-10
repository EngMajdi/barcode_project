from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import qrcode
from PIL import Image
import os
from flask import session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(150), nullable=False)
    barcode = db.Column(db.String(150), unique=True)
    unique_number = db.Column(db.Integer, unique=True)

    def __repr__(self):
        return f'<User {self.email}>'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('تم تسجيل الدخول بنجاح!', 'success')
            session['user_id'] = user.id
            return redirect(url_for('success', user_id=user.id))
        else:
            flash('البريد الإلكتروني أو كلمة المرور غير صحيحة.')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        
        # Check if the email already exists
        if User.query.filter_by(email=email).first():
            flash('Email already exists. Please use a different email.')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        unique_number = User.query.count() + 1
        user = User(name=name, email=email, phone=phone, password=hashed_password, unique_number=unique_number)
        
        # Generate a barcode
        barcode_path = f'static/barcodes/{email}.png'
        img = qrcode.make(f"{email}-{unique_number}")
        img.save(barcode_path)
        user.barcode = barcode_path

        try:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('success', user_id=user.id))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating user: {e}')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/success/<int:user_id>')
def success(user_id):
    user = User.query.get(user_id)
    return render_template('success.html', user=user)

if __name__ == '__main__':
    if not os.path.exists('users.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
