# Restaurant Booking System

## Project Overview

The Restaurant Booking System allows users to book a table for a meal at a restaurant. It supports features such as booking tables, managing reservations, and viewing a menu. This system is built using **Python**, **Django**, **HTML**, **CSS**, **JavaScript**, and a **PostgreSQL** database (hosted on Heroku). It is designed to provide a seamless user experience while managing bookings efficiently.

## Features

### External User's Goal:
- Book one or more guests for a meal at a specific time and date.

### Site Owner's Goal:
- Accept online reservations for their restaurant.

### Key Features:
- **Date/Time-based bookings**
- **Avoid double bookings**
- **Multiple table occupancies**
- **Reservation cancellations**
- **Menu display**

## Technologies Used
- **Back-End**: Python, Django
- **Front-End**: HTML, CSS, JavaScript
- **Database**: PostgreSQL (hosted on Heroku)
- **Deployment**: Heroku

## Installation

### Prerequisites:
- Python 3.x
- Django
- PostgreSQL (for local testing)
- Heroku CLI (for deployment)

### Setup Instructions:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/restaurant-booking-system.git
    cd restaurant-booking-system
    ```

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Create a PostgreSQL database (or use Heroku for cloud database).
    - Add database configurations in `settings.py`.

5. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser to access admin panel:**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Visit the app at** `http://127.0.0.1:8000/` in your browser.

## Features Implementation

### Back-End
- **CRUD operations** for reservations (create, read, update, delete).
- **User authentication**: Role-based login and registration (admin and user).
- **Database models** for reservations, tables, users, etc.
- **Role-based access control**: Admins can manage reservations, users can make bookings.

### Front-End
- **Restaurant Page**: Displays available tables and allows users to make reservations.
- **Menu Page**: Dynamic menu loaded from the back-end.
- **Responsive design**: The site is mobile-friendly and accessible.

### Deployment

1. **Deploy to Heroku:**
    - Push code to Heroku using Git and the Heroku CLI.
    - Set up PostgreSQL on Heroku.
    - Deploy the app using the following commands:
        ```bash
        heroku create
        git push heroku master
        heroku run python manage.py migrate
        ```

2. **Heroku Configuration:**
    - Add the necessary environment variables (e.g., Django secret key, database configurations).
    - Use Heroku’s PostgreSQL add-on for production database.

## Testing

- Manual testing for all functionality (reservations, user authentication, etc.).
- Automated tests for core features are implemented.
- Front-end testing for responsiveness and accessibility.

## Documentation

### Database Schema
- **Reservation**: Stores information about each booking (time, number of guests, user).
- **User**: Stores user authentication information (username, email, password).
- **Table**: Stores information about tables (seating capacity, availability).

### User Stories
1. **Back-End User Stories**:
   - As a user, I want to register and log in so I can make a reservation.
   - As an admin, I want to view, manage, and cancel reservations.

2. **Front-End User Stories**:
   - As a user, I want to browse the menu and book a table.
   - As a user, I want to receive confirmation when my reservation is successful.

## Future Improvements
- Add admin interface for better management of reservations and user roles.
- Expand menu options with more dynamic content.
- Implement email notifications for reservation confirmations.

## Conclusion

The Restaurant Booking System provides an efficient and user-friendly way for customers to book tables at a restaurant. The system is fully integrated with a back-end powered by Django and is deployed on Heroku, ensuring a reliable and scalable solution for restaurant owners and customers alike.

