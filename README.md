# ✈️ TRAVEL-BOOKING-AGENCY

A comprehensive travel booking system for seamless arrangements across **road**, **railway**, **waterways**, and **airways**.

---

## 🚀 Features

- 🔒 **User Authentication**: Secure login for users and administrators.
- 🗺️ **Booking Management**: Book travel by specifying location, destination, time, driver preferences, and urgency.
- 💸 **Bill Verification**: Calculate payment based on distance traveled.
- 📖 **Travel Log**: View your past travel history.
- 🛠️ **Admin Panel**: Manage accounts, view records, insert/delete data, and generate reports.

---

## 🛠 Technologies Used

- **Backend**: Python
- **Database**: MySQL
- **Libraries**: 
  - `mysql.connector` (database connectivity)
  - `tabulate` (display data in tables)

---

## 🗃️ Database Design

### **accounts**
| Field         | Type         | Description         |
|---------------|--------------|--------------------|
| Phone_number  | BIGINT (PK)  | User’s phone number|
| name          | VARCHAR(100) | User’s name        |
| password      | VARCHAR(100) | User’s password    |

### **customer_bookings**
| Field           | Type          | Description          |
|-----------------|---------------|----------------------|
| Phone_number    | BIGINT        | User’s phone number  |
| Your_location   | VARCHAR(100)  | Start location       |
| Your_destination| VARCHAR(100)  | Destination          |
| Time            | VARCHAR(50)   | Time of booking      |
| Driver          | VARCHAR(20)   | Gender preference    |
| Urgency         | VARCHAR(10)   | Urgency (yes/no)     |
| Date_booked     | VARCHAR(50)   | Booking date         |

---

## ⚡ Installation

### **Prerequisites**
- Python 3.x
- MySQL Server

### **Install Required Libraries**
```bash
pip install mysql-connector-python tabulate
```

# DATABASE SETUP
CREATE DATABASE travel_booking;

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

# 🚦 Usage

1. Run the program
```bash
python travel_booking.py
```
2.**User Login** : Enter phone number and password to access booking, billing, and travel log features.

3.**Admin Login** : Use password Adminpass for admin features: view, insert, or delete records.


# Authors
ANSH BIRE
