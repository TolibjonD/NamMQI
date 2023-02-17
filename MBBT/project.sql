CREATE DATABASE clinics;
CREATE TABLE doctors(
    id PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    phone VARCHAR(255),
    address VARCHAR(255)
);

CREATE TABLE clinics(
    id PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    destination VARCHAR(255),
    doctors INT,
    sections INT   
);