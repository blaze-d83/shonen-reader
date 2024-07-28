# Shonen Reader

Shonen Reader is a Django-based web application designed for manga enthusiasts. It allows users to browse, read, and interact with manga chapters. The platform features a dedicated admin interface for managing content and viewing statistics.

## Features

- **User Interface**: Browse and read manga chapters, like and comment on your favorites.
- **Admin Dashboard**: Manage manga content, view detailed statistics, and use a rich text editor for content creation.
- **Authentication**: Seamless login and profile-based redirection.
- **Media Management**: Easy upload and management of manga covers and chapters.

## Technologies

- Django
- SQLite
- HTML/CSS/JavaScript

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/shonen-reader.git
    cd shonen-reader
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access the application:**
    - User Interface: `http://127.0.0.1:8000/`
    - Admin Dashboard: `http://127.0.0.1:8000/admin/`

## Usage

- **Users** can browse, read, like, and comment on manga chapters.
- **Admins** can manage manga content, view statistics, and use the rich text editor for content creation.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License.

