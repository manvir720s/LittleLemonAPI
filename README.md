# Restuarant Menu, Ordering and Management API

This API built for the **LittleLemon Restuarant** is a Django-based API designed to manage various aspects of a restaurant's operations, including menus, orders, carts, order delivery, and user management. This API is built with the assumption that all users are authenticated, and it categorizes them into two distinct groups: **Managers** and **Delivery Crew**. Any user not belonging to these groups is considered a **Customer**.

## Purpose

The primary purpose of the LittleLemon API is to provide a robust backend system for the restaurant's operations, allowing for the creation, retrieval, updating, and deletion of various resources. These resources include menus, orders, shopping carts, order deliveries, and user accounts. Additionally, it manages user authentication and distinguishes between Managers, Delivery Crew, and Customers.

## Libraries Used

The project relies on the following libraries to achieve its functionality:

### Django Rest Framework

- **Purpose**: Django Rest Framework (DRF) is used to build reliable and secure API endpoints for the LittleLemon API. It offers essential tools for creating RESTful APIs, including user authentication, access control, and API views. DRF also provides endpoint throttling to control the rate at which users can make requests, ensuring fair usage.

### Djoser

- **Purpose**: Djoser is used to handle user management operations via API endpoints. It simplifies user-related actions like registration, login, password reset, and profile management. Djoser provides a set of URLs for user operations, making it easier to implement these functionalities.

- `/users/`: Endpoint for listing and creating user accounts.
- `/users/me`: Endpoint for retrieving and updating the authenticated user's profile.
- `/users/resend_activation/`: Endpoint for resending activation emails.
- `/users/set_password/`: Endpoint for setting a new user password.
- `/users/reset_password/`: Endpoint for initiating a password reset.
- `/users/reset_password_confirm/`: Endpoint for confirming a password reset request.
- `/users/set_username/`: Endpoint for setting a new username.
- `/users/reset_username/`: Endpoint for initiating a username reset.
- `/users/reset_username_confirm/`: Endpoint for confirming a username reset request.
- `/token/login/`: Endpoint for user login.
- `/token/logout/`: Endpoint for user logout.

### User Groups

The LittleLemon API classifies users into two main groups:

1. **Managers**: Users with administrative privileges, responsible for managing the restaurant's menu, orders, deliveries, and user accounts.
2. **Delivery Crew**: Users responsible for order deliveries and related tasks.
3.  **Customers**: Users who place items in carts and place orders.


## API Endpoints

The LittleLemon API offers various endpoints to interact with the system. Below is a list of key endpoints categorized by functionality:
## Menu Endpoints
![menu-items endpoint](https://github.com/manvir720s/LittleLemonAPI/assets/70035337/a3e6eecc-5ab9-42f0-925f-f5502fe55e50)

## Orders Endpoints
![order management](https://github.com/manvir720s/LittleLemonAPI/assets/70035337/209f3e3f-d3a6-4b76-8b78-9d1b132aab31)

## Cart Endpoints
![cart endpoints](https://github.com/manvir720s/LittleLemonAPI/assets/70035337/8ef8d1a6-5bee-4a3d-bff3-8d5c5e032ece)

## User Management Endpoints
![user group management](https://github.com/manvir720s/LittleLemonAPI/assets/70035337/dd6f62f9-fe5f-4924-96bf-1f37080d4b4d)

## Usage

To start using the LittleLemon API, you must have the necessary authentication credentials and permissions. Please refer to the API documentation for detailed information on how to interact with each endpoint and the required authentication headers.


## Acknowledgments

The starter code for this project was provided by Meta as part of the Full Stack Certification program


## Contribution

If you wish to contribute to the LittleLemon API project, please follow the contribution guidelines outlined in the project's repository.

Thank you for using the LittleLemon API. We hope this project enhances your restaurant's operational efficiency and provides a seamless experience for both managers and customers.
