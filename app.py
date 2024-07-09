from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def read_csv(filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(filename, data):
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

def update_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_csv('data/users.csv')
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('hotels'))
        flash('Invalid credentials')
    return render_template('login.html')

@app.route('/review/<hotel_id>', methods=['GET', 'POST'])
def review(hotel_id):
    if request.method == 'POST':
        rating = request.form['rating']
        review_text = request.form['review']
        review = {'hotel_id': hotel_id, 'username': session['username'], 'rating': rating, 'review': review_text}
        write_csv('data/reviews.csv', review)
        return redirect(url_for('hotel_detail', hotel_id=hotel_id))
    hotel = next(hotel for hotel in read_csv('data/hotels.csv') if hotel['id'] == hotel_id)
    return render_template('review.html', hotel_name=hotel['name'], hotel_id=hotel_id)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        if not email:
            flash('Email is required')
            return redirect(url_for('signup'))
        if not username or not password:
            flash('Username and Password are required')
            return redirect(url_for('signup'))
        users = read_csv('data/users.csv')
        if any(user['username'] == username for user in users):
            flash('Username already exists')
            return redirect(url_for('signup'))
        user = {'username': username, 'email': email, 'password': password, 'wishlist': ''}
        write_csv('data/users.csv', user)
        session['username'] = username
        return redirect(url_for('hotels'))
    return render_template('signup.html')

@app.route('/hotels', methods=['GET', 'POST'])
def hotels():
    hotels = read_csv('data/hotels.csv')
    if request.method == 'POST':
        filters = {
            'location': request.form.get('location'),
            'price_min': request.form.get('price_min'),
            'price_max': request.form.get('price_max'),
            'amenities': request.form.getlist('amenities')
        }
        hotels = filter_hotels(hotels, filters)
    return render_template('hotels.html', hotels=hotels)

def filter_hotels(hotels, filters):
    filtered_hotels = []
    for hotel in hotels:
        if filters['location'] and filters['location'].lower() not in hotel['location'].lower():
            continue
        if filters['price_min'] and float(hotel['price']) < float(filters['price_min']):
            continue
        if filters['price_max'] and float(hotel['price']) > float(filters['price_max']):
            continue
        if filters['amenities'] and not all(amenity in hotel['amenities'].split(',') for amenity in filters['amenities']):
            continue
        filtered_hotels.append(hotel)
    return filtered_hotels

@app.route('/hotel/<hotel_id>')
def hotel_detail(hotel_id):
    hotel = next(hotel for hotel in read_csv('data/hotels.csv') if hotel['id'] == hotel_id)
    reviews = read_csv('data/reviews.csv')
    hotel_reviews = [review for review in reviews if review['hotel_id'] == hotel_id]
    return render_template('hotel_detail.html', hotel=hotel, reviews=hotel_reviews)

@app.route('/book/<hotel_id>', methods=['GET', 'POST'])
def book(hotel_id):
    if request.method == 'POST':
        user = session['username']
        check_in_date = request.form['check_in_date']
        check_out_date = request.form['check_out_date']
        reservation = {'user': user, 'hotel_id': hotel_id, 'check_in_date': check_in_date, 'check_out_date': check_out_date}
        write_csv('data/reservations.csv', reservation)
        hotel = next(hotel for hotel in read_csv('data/hotels.csv') if hotel['id'] == hotel_id)
        return redirect(url_for('confirm_booking', hotel_name=hotel['name']))
    hotel = next(hotel for hotel in read_csv('data/hotels.csv') if hotel['id'] == hotel_id)
    return render_template('book.html', hotel=hotel)

@app.route('/confirm_booking')
def confirm_booking():
    hotel_name = request.args.get('hotel_name')
    return render_template('confirm_booking.html', hotel_name=hotel_name)

@app.route('/profile')
def profile():
    user = session.get('username')
    if not user:
        return redirect(url_for('login'))
    reservations = [res for res in read_csv('data/reservations.csv') if res['user'] == user]
    hotels = {hotel['id']: hotel for hotel in read_csv('data/hotels.csv')}
    return render_template('profile.html', reservations=reservations, hotels=hotels)

@app.route('/wishlist')
def wishlist():
    user = session.get('username')
    if not user:
        return redirect(url_for('login'))
    users = read_csv('data/users.csv')
    wishlist = next(user for user in users if user['username'] == session['username'])['wishlist'].split(',')
    hotels = {hotel['id']: hotel for hotel in read_csv('data/hotels.csv')}
    wishlist_hotels = [hotels[hotel_id] for hotel_id in wishlist if hotel_id in hotels]
    return render_template('wishlist.html', wishlist_hotels=wishlist_hotels)

@app.route('/add_to_wishlist/<hotel_id>')
def add_to_wishlist(hotel_id):
    user = session.get('username')
    if not user:
        return redirect(url_for('login'))
    users = read_csv('data/users.csv')
    for usr in users:
        if usr['username'] == user:
            wishlist = usr['wishlist'].split(',')
            if hotel_id not in wishlist:
                wishlist.append(hotel_id)
                usr['wishlist'] = ','.join(wishlist)
    update_csv('data/users.csv', users)
    return redirect(url_for('wishlist'))

if __name__ == '__main__':
    app.run(debug=True)
