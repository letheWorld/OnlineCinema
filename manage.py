import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from App import create_app

env = os.environ.get('FLASK_ENV', 'develop')

app = create_app(env)

manege = Manager(app=app)
manege.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manege.run()
