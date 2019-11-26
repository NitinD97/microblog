# microblog
Created a Blogging website, that allows the users to post their thoughts, read others posts and follow them, to keep updated with their posts. The app also has translation feature that allows the users to translate a post into their native language, if the translation is available for a particular post.

## Technologies
- Flask
- SQLAlchemy
- Elasticsearch
- PostgreSQL
- flask-babel
- Jinja2
- Bootstrap
- Mail
- AzureTextTranslation

## Commands
You should have venv installed in your `python3.6`
> python3.6 -m pip install venv

Install `venv` 
> python3.6 -m venv venv

Activate venv
> source venv/bin/activate

Install all the module into venv using:
> pip install -r requirements.txt

export the following variables
> FLASK_APP = /path/to/microblog.py

> FLASK_ENV = development

> FLASK_DEBUG = 1

run the commands:
> flask db init

> flask db migrate

> flask db upgrade


