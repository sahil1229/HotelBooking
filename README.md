
# Hotel Booking App

## Visuals
<img width="1512" alt="Screenshot 2024-07-09 at 2 23 58 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/abd67624-24f6-45a8-8e6e-3e6baf61bdac">
<img width="1512" alt="Screenshot 2024-07-09 at 2 24 20 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/dcff36a4-a9bb-442d-94b3-638805c1b0bf">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 00 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/1896e539-6839-4ba6-a415-d031548a6126">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 12 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/070130c9-e6b6-46d5-bfd3-859130c4a8f4">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 25 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/ff0d0266-8a39-4ff1-bf36-65ab8d1a6030">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 43 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/2c6f4361-5f68-4820-b3bd-ea042eefd4b2">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 50 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/8f954726-954e-49b3-9cfa-f517de1719e6">
<img width="1512" alt="Screenshot 2024-07-09 at 2 25 59 PM" src="https://github.com/sahil1229/HotelBooking/assets/143722174/fd8459d0-13e3-4e1c-83b4-4b8c93b64a9e">

## Overview

Welcome to the Hotel Booking App! This web application allows users to find, book, and review hotels, as well as manage their wishlist and view their booking history. Built with Flask, this app is designed to provide a seamless hotel booking experience with features for users to explore hotels, make reservations, and submit reviews.

## Features

- **Hotel Listings**: Browse a list of hotels with details like price, location, amenities, and special offers.
- **Hotel Details**: View detailed information about a specific hotel, including a description, amenities, and reviews.
- **Booking System**: Reserve a room at a hotel with options for check-in and check-out dates.
- **Wishlist Management**: Add hotels to your wishlist for future reference.
- **User Profiles**: View your booking history and manage your wishlist.
- **Review System**: Write and submit reviews for hotels.
- **Filter Options**: Apply filters based on location, price range, and amenities to find the perfect hotel.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **Database**: CSV files for data storage (users, hotels, reservations, reviews)

## Installation

To get started with the Hotel Booking App, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/sahil1229/HotelBooking.git
cd HotelBooking
```

### 2. Set Up a Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Data Files

Download the following CSV files and place them in the `data` directory:

- [hotels.csv](https://example.com/hotels.csv)
- [users.csv](https://example.com/users.csv)
- [reservations.csv](https://example.com/reservations.csv)

### 5. Run the Application

Start the Flask development server:

```bash
python app.py
```

Open your web browser and navigate to `http://127.0.0.1:5000` to access the app.

## Usage

### Access the Application

1. **Home Page**: The landing page with a welcome message.
2. **Login**: Sign in with your username and password.
3. **Sign Up**: Register a new account with a username, email, and password.
4. **Hotels**: View a list of available hotels and filter based on location, price, and amenities.
5. **Hotel Details**: View details of a specific hotel, book a room, or add the hotel to your wishlist.
6. **Book a Room**: Choose check-in and check-out dates to make a reservation.
7. **Wishlist**: Manage your list of favorite hotels.
8. **Profile**: View your booking history and manage your wishlist.

### Example Requests

- **View Hotel Details**: `GET /hotel/<hotel_id>`
- **Book a Room**: `POST /book/<hotel_id>`
- **Add to Wishlist**: `GET /add_to_wishlist/<hotel_id>`

## Folder Structure

```
/hotel-booking-app
    /static
        /styles.css       # CSS styles for the application
        /script.js        # JavaScript file for front-end functionalities
    /templates
        /welcome.html     # Home page template
        /login.html       # Login page template
        /signup.html      # Sign-up page template
        /hotels.html      # Hotels listing page template
        /hotel_detail.html# Hotel details page template
        /book.html        # Booking page template
        /confirm_booking.html # Booking confirmation page template
        /profile.html     # User profile page template
        /wishlist.html    # Wishlist page template
        /review.html      # Review submission page template
    /data
        /hotels.csv       # CSV file with hotel data
        /users.csv        # CSV file with user data
        /reservations.csv # CSV file with reservation data
        /reviews.csv      # CSV file with review data
    app.py                # Main Flask application file
    requirements.txt      # Python package dependencies
    README.md             # This README file
```


Please follow the coding guidelines and ensure your code is well-tested.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
