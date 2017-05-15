from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

from instance.config import app_config


db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    from app.models import PullList

    @app.route('/pulllists/', methods=['POST', 'GET'])
    def pulllists():
        if request.method == "POST":
            name = request.form['name']
            if name:
                pulllist = PullList(name=name)
                pulllist.save()
                response = jsonify({
                    'id': pulllist.id,
                    'name': pulllist.name,
                    'date_created': pulllist.date_created,
                    'date_modified': pulllist.date_modified
                })
                response.status_code = 201
        elif request.method == "GET":
            pulllists = PullList.get_all()
            results = []

            for pulllist in pulllists:
                obj = {
                    'id': pulllist.id,
                    'name': pulllist.name,
                    'date_created': pulllist.date_created,
                    'date_modified': pulllist.date_modified
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
        else:
            response = jsonify({"errors": [{
                "title":  "Method Not Allowed",
                "detail": "{} method not allowed. Only the GET and POST method are allowed".format(request.method)}]
            })
            response.status_code = 405

        return response

    return app
