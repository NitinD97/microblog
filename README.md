# microblog (https://microblog-nd.herokuapp.com/)
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
> Install elasticsearch on your system.

> You should have venv installed in your `python3.6` 
```
python3.6 -m pip install venv
```

> Install `venv` 
```
python3.6 -m venv venv
```

> Activate venv
```
source venv/bin/activate
```

> Install all the module into venv using:
```
pip install -r requirements.txt
```

> set the following environment variables
```
FLASK_APP=/path/to/microblog.py
FLASK_ENV=development
FLASK_DEBUG=1
```

> run the commands:
```
flask db init
flask db migrate
flask db upgrade
```

> Create a `.env` file that contains the following variables:
```
SECRET_KEY=appSecretKey
MAIL_SERVER=localhost
MAIL_PORT=8025
MS_TRANSLATOR_KEY=key_of_translator_service
ELASTICSEARCH_URL=http://localhost:9200 or the port in your system
```

> finally run the command:
```
flask run
```



