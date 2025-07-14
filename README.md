# TRAVEL-BOOKING-AGENCY
This is a comprehensive travel booking system designed to facilitate seamless travel arrangements across various modes of transport, including road, railway, waterways, and airways.


## Features
- **User Authentication**: Login for both users and administrators.
- **Booking Management**: Users can book travel by specifying location, destination, time, driver preferences, and urgency.
- **Bill Verification**: Calculate payment based on distance traveled.
- **Travel Log**: View past travel history.
- **Admin Panel**: Manage accounts, view records, insert/delete data, and generate reports.

## Technologies Used
- **Backend**: Python with MySQL for database operations.
- **Libraries**: `mysql.connector` for database connectivity, `tabulate` for displaying data in tabular format.
- **Database**: MySQL database named `travel_booking` with tables for accounts and customer bookings.

## Database Design
### Tables
1. **accounts**:
   - `Phone_number` (Primary Key)
   - `name`
   - `password`
2. **customer_bookings**:
   - `Phone_number`
   - `Your_location`
   - `Your_destination`
   - `Time`
   - `Driver` (gender preferences)
   - `Urgency` (yes/no)
   - `Date_booked`

## Installation
1. **Prerequisites**:
   - Python 3.x
   - MySQL Server
   - Install required libraries:
     ```
     pip install mysql-connector-python tabulate
     ```
2. **Database Setup**:
   - Create a MySQL database named `travel_booking`.
   - Execute the following SQL commands to create tables:
     ```sql
     CREATE TABLE accounts (
         Phone_number BIGINT PRIMARY KEY,
         name VARCHAR(100),
         password VARCHAR(100)
     );
     CREATE TABLE customer_bookings (
         Phone_number BIGINT,
         Your_location VARCHAR(100),
         Your_destination VARCHAR(100),
         Time VARCHAR(50),
         Driver VARCHAR(20),
         Urgency VARCHAR(10),
         Date_booked VARCHAR(50)
     );
     ```

## Usage
1. **Run the Program**:
   ```
   python travel_booking.py
   ```
2. User Login:

  Enter phone number and password to access user features like booking, bill verification, and travel log.
3. Admin Login:

  Use password Adminpass to access admin features like viewing, inserting, or deleting records.
