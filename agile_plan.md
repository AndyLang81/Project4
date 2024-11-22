# Restaurant Booking System - Agile Project Plan

## Overview

This is the Agile plan for delivering a **Restaurant Booking System** by **December 2nd**. The plan focuses on back-end development and deployment first, followed by front-end features such as the restaurant page and menu.

The plan follows a **sprint-based** approach to ensure continuous progress and timely delivery.

## Sprint 1: **Back-End Development & Deployment** (Nov 22 - Nov 28)

**Goal**: Focus on building the back-end functionality and deploy the system on Heroku.

### Day 1-3 (Nov 22 - Nov 24): **Back-End Setup & Database Design**
- **Set up Django project** and basic environment.
- **Create database schema** (models for reservations, users, tables).
- Implement back-end CRUD operations for reservations.
- Set up **PostgreSQL/MySQL** for local testing.

### Day 4-5 (Nov 25 - Nov 26): **User Authentication & Role-Based Access**
- Implement **user authentication** (login, registration).
- Apply **role-based access control** for users and admins.
- **Test back-end locally** to ensure reservation creation and data management work.

### Day 6-7 (Nov 27 - Nov 28): **Deployment to Heroku**
- Deploy the app on **Heroku** with PostgreSQL or MySQL.
- Set up the database and environment variables on Heroku.
- Test back-end features to ensure smooth operation in the cloud.

---

## Sprint 2: **Front-End Development & Integration** (Nov 29 - Dec 2)

**Goal**: Implement the front-end components, including restaurant page, menu, and reservation form.

### Day 8-9 (Nov 29 - Nov 30): **Front-End Design & Basic Menu Page**
- Design and implement the **restaurant page** layout (HTML/CSS).
- Make the page **mobile-responsive** and accessible.
- Implement a **dynamic menu** using Django templates, displaying menu items pulled from the back-end.

### Day 10 (Dec 1): **Reservation Form & Integration**
- Implement the **reservation form** allowing users to book tables.
- Ensure form data (date, time, number of guests) is correctly captured and stored in the database.
- Test the **reservation flow** from front-end to back-end and ensure users receive feedback (confirmation, error messages).

### Day 11 (Dec 2): **Final Testing & Documentation**
- Conduct final testing of both back-end and front-end features.
- Test the reservation system for edge cases (double booking, invalid inputs).
- Finalize and clean up the **README** with documentation of the project.
- **Submit the project** with the final deployed version on Heroku.

---

## User Stories Breakdown

### Back-End User Stories:
- **User Story 1**: As a user, I want to register, log in, and make a reservation for a table.
- **User Story 2**: As an admin, I want to view, manage, and cancel reservations.

### Front-End User Stories:
- **User Story 1**: As a user, I want to browse the restaurant menu and book a table at a given time.
- **User Story 2**: As a user, I want to see a confirmation when my reservation is successfully made.

---

## Task Breakdown and Prioritization

### Must-Have Features (Core for Delivery):
- Back-end CRUD functionality for reservations.
- User registration, login, and role-based access.
- Front-end restaurant page and menu.
- Reservation form with confirmation and error handling.
- Deployment to Heroku.

### Should-Have Features (To Be Delivered by End of Sprint 2):
- Admin interface for managing reservations.
- Responsive and accessible front-end design.

---

## Final Deliverables

1. **Fully functional back-end** with reservations and user management.
2. **Deployed version on Heroku** with active database.
3. **Front-end interface** with restaurant page, menu, and reservation form.
4. **User authentication** with role-based access control.
5. **Testing & Documentation** in the README, including database schema and setup instructions.
