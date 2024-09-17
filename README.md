# 🍽️ MealHaven Backend API

MealHaven is a meal kit delivery platform that allows users to customize, plan, and order meals directly from an intuitive web interface. This backend API is responsible for managing user data, meal plans, ingredients, orders, and customization options, providing the necessary logic and database interactions for the platform.

## 📁 Project Structure

The backend is built using Python and is organized into two main sections: the `api` folder, which handles the routing and endpoints, and the `models` folder, which manages the data models and database interactions.

### Directory Overview:

```bash
.
├── api/                    # API routes and versioning
│   ├── __init__.py
│   └── v1/                 # Version 1 of the API
│       ├── app.py          # Main app initialization
│       └── views/          # Route handlers for various resources
│           ├── address.py
│           ├── customizationOptions.py
│           ├── ingredients.py
│           ├── meals.py
│           ├── orders.py
│           ├── plans.py
│           ├── pref.py
│           ├── status.py
│           └── users.py
│
├── models/                 # Database models
│   ├── Data/               # Database engine configuration
│   │   ├── db_engine.py    # Database connection and setup
│   ├── address.py
│   ├── customization.py
│   ├── ingredients.py
│   ├── mealIngredient.py
│   ├── mealPreference.py
│   ├── meals.py
│   ├── order_meal_cust.py
│   ├── order_preferences.py
│   ├── OrderMeals.py
│   ├── order.py
│   ├── plan.py
│   ├── Preference.py
│   └── user.py
```

## 🛠️ Technologies Used

- **Python**: The core language used to build the API.
- **Flask**: A lightweight web framework for building RESTful APIs.
- **SQLAlchemy**: For database modeling and ORM (Object Relational Mapping).
- **MySQL**: The relational database management system used for storing and managing data.
- **JSON**: The format used for exchanging data between the frontend and backend.

## 📂 API Endpoints

Below are the primary API endpoints available in **MealHaven**:

### Users
- **GET** `/users`: Retrieve a list of all users.
- **POST** `/users`: Create a new user.
- **GET** `/users/<id>`: Retrieve user details by user ID.

### Meals
- **GET** `/meals`: Retrieve a list of available meals.
- **POST** `/meals`: Create a new meal.
- **GET** `/meals/<id>`: Retrieve meal details by meal ID.

### Orders
- **GET** `/orders`: Retrieve all orders.
- **POST** `/orders`: Place a new order.
- **GET** `/orders/<id>`: Retrieve order details by order ID.

### Customization Options
- **GET** `/customization-options`: Retrieve all customization options.
- **POST** `/customization-options`: Create a new customization option.

### Address
- **GET** `/address`: Retrieve all saved addresses.
- **POST** `/address`: Save a new delivery address.

### Status
- **GET** `/status`: Check the status of the API.

## ⚙️ Models

The backend includes models representing key elements of the meal kit system. These models manage database interactions and data structures for users, meals, orders, preferences, and more:

- **User Model** (`user.py`): Manages user data including registration and authentication.
- **Meals Model** (`meals.py`): Handles meal data such as descriptions, ingredients, and nutritional info.
- **Order Model** (`order.py`): Manages order creation, tracking, and meal assignments.
- **Address Model** (`address.py`): Stores user delivery addresses.
- **Customization Model** (`customization.py`): Handles meal customization options, allowing users to tailor meals to their preferences.

## 🚀 Getting Started

To run the backend locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mealhaven-backend.git
```

### Install the necessary dependencies:
```bash
pip install -r requirements.txt
```

### Set up the database:
- Create a MySQL database for the project.
- Update `db_engine.py` with your database credentials.

### Run the development server:
```bash
flask run
```

