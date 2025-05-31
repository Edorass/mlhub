# populate_projects.py
import os
import django

# تنظیمات Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mlhub.settings")
django.setup()

from projects.models import MLproject

# حذف پروژه‌های قبلی برای تست مجدد
MLproject.objects.all().delete()

# لیست پروژه‌ها
projects = [
    {
        "title": "AI Resume Scanner",
        "description": "An application for reviewing resumes and scoring with machine learning algorithms.",
        "tech_stack": "Python, Django, OpenCV",
        "github_link": "https://github.com/user/resume-scanner",
    },
    {
        "title": "API Rate Limiter",
        "description": "Request rate limiter for API using Redis and Django.",
        "tech_stack": "Django REST, Redis",
        "github_link": "https://github.com/user/api-rate-limiter",
    },
    {
        "title": "Data Science Pipeline",
        "description": "A complete path for data processing from extraction to modeling, evaluation, and final deployment. Includes multiple steps and uses various libraries such as Pandas, Scikit-learn, and Flask to build an end-to-end system.",
        "tech_stack": "Pandas, Scikit-learn, Flask",
        "github_link": "https://github.com/user/data-pipeline",
    },
    {
        "title": "Satellite Image Classifier",
        "description": "Object classification in satellite images using deep neural networks.",
        "tech_stack": "Keras, TensorFlow",
        "github_link": "https://github.com/user/satellite-classifier",
    },
    {
        "title": "Broken Link Project",
        "description": "This project was added only to test displaying broken or empty links in the UI.",
        "tech_stack": "FastAPI",
        "github_link": "",
    },
]

# اضافه کردن به دیتابیس
for project in projects:
    MLproject.objects.create(**project)

print("✅ پروژه‌ها با موفقیت به دیتابیس اضافه شدند.")
