import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
from app import models


config_name = os.getenv('ENV_CONFIG')
app = create_app(config_name)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
