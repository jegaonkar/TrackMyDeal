### Gas Utility Service

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Credentials](#credentials)

## Overview
The Gas Utility Service is a web application designed to streamline service requests, account management, and tracking. Users can submit service requests, track their status, and manage their accounts efficiently.

## Prerequisites
Before you begin, ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.10 or above)
- [Django](https://www.djangoproject.com/download/) (latest)

## Installation
Follow these steps to set up the project:

1. **Install the required packages**:
   ```bash
   pip install django
   ```

2. **Clone the repository**:
   ```bash
   git clone https://github.com/jegaonkar/trackmydeal
   ```

3. **Navigate to the project directory**:
   ```bash
   cd trackmydeal
   ```

4. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   ```
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application
To start the development server, run:
```bash
python manage.py runserver
```
You can access the application by navigating to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage
- Users can register and log in to submit service requests.
- The application provides a tracking feature to monitor the status of submitted requests.
- Admins can manage users and service requests through the admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

## Credentials
### Admin
- **Username:**
  ```bash
  adminuser
  ```
- **Password:**
  ```bash
  admin1234
  ```
    
