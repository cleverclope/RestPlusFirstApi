# The os module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying 
# the current directory, etc. You first need to import the os module to interact with the underlying operating system.

# unit test is to detect as many bugs and inconsistencies in the infancy of the application development as possible. It ensures that bugs
#  and other problems we catch in the first stages of the development, can be fixed by the development team.

# A migration in Python uses the features of an ORM to provide tools to change our database. A migration system compares the current state of 
# our application's models to the existing state of the database. When we run the script, the operations run one after another, and the database is updated.

# The Flask-Script extension provides support for writing external scripts in Flask. This includes running a development server, a customised Python shell, 
# scripts to set up your database, cronjobs, and other command-line tasks that belong outside the web application itself.
import os  
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user
from app.main.model import blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run()


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()