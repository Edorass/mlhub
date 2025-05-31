# MLHub – Machine Learning Project Showcase

MLHub is a Django-based web application that allows users to upload, view, edit, and manage machine learning project portfolios. It features a user-friendly interface with image upload previews, Bootstrap styling, and full CRUD support for project entries.

## 🚀 Features

- 🔐 User registration and login system
- 📝 Upload and manage ML project entries
- 📷 Image upload with preview and validation
- ✏️ Edit or delete existing projects
- 💡 Bootstrap 5-based responsive UI
- ✅ CSRF protection and form validation feedback

## 🛠️ Tech Stack

- **Backend:** Python 3.11, Django 5.2
- **Frontend:** HTML, CSS, Bootstrap 5
- **Database:** SQLite (default, easy to switch to PostgreSQL or others)

## 📸 Screenshots

> Add screenshots to the `/screenshots` folder if you'd like to showcase your UI.

![Home Page](screenshots/home.png)
![Add Project Form](screenshots/form.png)

## 📦 Installation

Clone the repository and set up the project locally:

```bash
git clone https://github.com/your-username/mlhub.git
cd mlhub

Create and activate a virtual environment:
python -m venv venv
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate

Install the dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser:
python manage.py createsuperuser

Start the development server:
python manage.py runserver

Now visit: http://127.0.0.1:8000

Project Structure

mlhub/
├── projects/            # The main project app with models, forms, views
│   ├── templates/       # Templates related to projects
│   └── ...              
├── templates/           # Generic templates like base.html
├── media/               # User uploaded images
├── manage.py
└── venv/                # Python virtual environment (does not have to be inside git)


🙋‍♂️ Contributing
Feel free to fork the repository and submit pull requests for new features, improvements, or bug fixes.

Made with 💻 and ☕ by Dariush Ajorloo




