# blog_project

This is a Simple Blog Project created using Django Web Framework.

## Features

* Create Blog.
* Sign In Using Username and Password.
* Add a New Post.
* Publish the New Post.
* Comment on the Post.
* Delete the Post


## Project Installation

To setup a local development environment:

Create a virtual environment in which to install Python pip packages. For any help regarding virtual environment installation,
you can check Django documentation.


Clone GitHub Project,

https://github.com/Kirti-Bhushan/blog_project.git

cd blog_project/myblogsite


Migrate Database,
```bash
python manage.py migrate
python manage.py makemigrations blogapp
python manage.py migrate
```

Run the web application locally,
```bash
python manage.py runserver # 127.0.0.1:8000
```

Create Superuser,
```bash
python manage.py createsuperuser
```


