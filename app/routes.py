# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
import datetime

main = Blueprint('main', __name__)

# Фіксовані дані для входу
VALID_USERNAME = "user"
VALID_PASSWORD = "password"

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['username'] = username
            flash('Ви успішно увійшли!', 'success')
            return redirect(url_for('main.profile'))
        else:
            flash('Невірне ім\'я користувача або пароль', 'danger')
            return redirect(url_for('main.login'))
    return render_template('login.html')

@main.route('/profile')
def profile():
    if 'username' not in session:
        flash('Спершу увійдіть в систему', 'danger')
        return redirect(url_for('main.login'))
    
    username = session['username']
    cookies = request.cookies
    return render_template('profile.html', username=username, cookies=cookies)

@main.route('/logout')
def logout():
    session.pop('username', None)
    flash('Ви вийшли з системи', 'info')
    return redirect(url_for('main.login'))

@main.route('/add_cookie', methods=['POST'])
def add_cookie():
    if 'username' not in session:
        flash('Спершу увійдіть в систему', 'danger')
        return redirect(url_for('main.login'))
    
    key = request.form.get('key')
    value = request.form.get('value')
    max_age = int(request.form.get('max_age'))
    
    if key and value and max_age:
        resp = make_response(redirect(url_for('main.profile')))
        resp.set_cookie(key, value, max_age=max_age)
        flash(f'Кукі {key} додано', 'success')
        return resp
    else:
        flash('Будь ласка, введіть усі поля для додавання кукі', 'danger')
        return redirect(url_for('main.profile'))

@main.route('/delete_cookie/<key>')
def delete_cookie(key):
    if 'username' not in session:
        flash('Спершу увійдіть в систему', 'danger')
        return redirect(url_for('main.login'))
    
    resp = make_response(redirect(url_for('main.profile')))
    resp.set_cookie(key, '', expires=0)
    flash(f'Кукі {key} видалено', 'info')
    return resp

@main.route('/delete_all_cookies')
def delete_all_cookies():
    if 'username' not in session:
        flash('Спершу увійдіть в систему', 'danger')
        return redirect(url_for('main.login'))
    
    resp = make_response(redirect(url_for('main.profile')))
    for key in request.cookies.keys():
        resp.set_cookie(key, '', expires=0)
    flash('Усі кукі видалено', 'info')
    return resp
