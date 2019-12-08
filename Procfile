web: flask db migrate; flask db upgrade; flask translate compile; gunicorn microblog:app
worker: rq worker microblog-tasks
