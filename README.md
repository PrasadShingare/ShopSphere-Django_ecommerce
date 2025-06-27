# Ecommerce Django Project

A robust and simple Django-based web application that allows users to register, log in, and manage products with full Create, Read, Update, and Delete (CRUD) functionality. It features a modern, responsive user interface built with Tailwind CSS.

---

## Features

* **User Authentication**:
    * User Registration & Login
    * Secure user authentication powered by Django's built-in system
* **Modern User Interface**:
    * Sleek and responsive design using Tailwind CSS
    * Consistent dark theme across pages
* **Comprehensive Product Management (CRUD)**:
    * **Add New Products**: Form for adding new products with image upload capabilities.
    * **View Product Catalog**: Display of all products in a table with item numbers, prices, stock, and action links.
    * **View Product Details**: Dedicated page for detailed information on each product.
    * **Edit Existing Products**: Form for updating product details and images.
    * **Delete Products**: Secure deletion with a confirmation modal.

---

## Technologies Used

* **Backend**:
    * Django 5.2.3
    * Python 3.12
* **Database**:
    * SQLite (default Django DB)
* **Frontend**:
    * Tailwind CSS (for styling)
    * Django Widget Tweaks (recommended for applying Tailwind classes to Django forms)

---

## Folder Structure

```
ecommerce/
├── ecommerce/           # Project configuration
├── shop/                # Main app
│   ├── migrations/
│   ├── templates/
│   │   └── shop/
│   │       ├── base.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── products.html
│   │       ├── product_detail.html
│   │       └── product_form.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
├── .gitignore           # Git ignore file
├── db.sqlite3
├── manage.py
└── requirements.txt     # Project dependencies
```

## Setup Instructions

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/PrasadShingare/ShopSphere-Django_ecommerce.git
    cd ecommerce
    ```
2.  **Create a virtual environment** (optional but highly recommended):
    ```bash
    python -m venv env
    # On Windows:
    env\Scripts\activate
    # On macOS/Linux:
    source env/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run migrations**:
    ```bash
    python manage.py makemigrations shop
    python manage.py migrate
    ```
5.  **Create superuser** (optional, for admin panel access):
    ```bash
    python manage.py createsuperuser
    ```
6.  **Start the development server**:
    ```bash
    python manage.py runserver 8001
    ```
7.  **Visit the application** in your browser:
    `http://127.0.0.1:8001/`

---

## Notes

* Ensure `MEDIA_URL` and `MEDIA_ROOT` are configured in `ecommerce/settings.py` for image uploads to function correctly.
* The Django admin panel is accessible at `/admin/`.
* Product creation and management forms are only available to logged-in users.

---

## License

This project is for educational purposes. Feel free to modify and build upon it.
