.PHONY: clean system-packages python-packages install tests run all

clean:
   find . -type f -name '*.pyc' -delete
   find . -type f -name '*.log' -delete

system-packages:
   sudo apt install python-pip -y

python-packages:
   pip install -r requirements.txt

install: system-packages python-packages

tests:
   python manage.py test

run:
   python manage.py run

all: clean install tests run

# Here are the options of the make file.
# make install : installs both system-packages and python-packages
# make clean : cleans up the app
# make tests : runs the all the tests
# make run : starts the application
# make all : performs clean-up,installation , run tests , and starts the app.