PROJECT: Discuss Now! Website

FILES:
.
├── README.txt
├── auth
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── myvenv
├── requirements.txt
├── templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   ├── register.html
│   ├── static
│   │   └── base.css
│   ├── thread_detail.html
│   └── threads.html
└── website
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

DESCRIPTION:
The goal of this project is to implement the discussion website on django application.
In this webpage, the user can register with their email address and password.
Once the user logged in, they can create threads and leave comments on each threads, 
delete their thread/comment, or check their profiles.
Threads and comments can be deleted by only the owner of the thread/comment.

HOW TO RUN SERVER LOCALLY:
pip install all required packages. (Use requirements.txt)
Excute "python manage.py runserver" in the terminal.