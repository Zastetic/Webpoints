# What is this project?
It's a web server made in python with flask and sqlalchemy. Made for a school project.
In there you can create multiple classes and assing pontuation to it. In the admin panel you can add specifics amount of points or do it manually.

In the main page you can see the project's rules, and the updated ranking.

# How to run it
The code is tested with Python 3.13. Any other version above this will work properly.
The first time you run the project, The database will be created. To recriate it, just erase the database, and it'll be created again, but reseted.

All the following instructions was made in git bash.

```bash

# Clone the repository
git clone https://github.com/Zastetic/Webpoints.git

# Move to the folder's project
cd Webpoints

# Create the virtual environment and install dependences
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt

# Run the server
python app.py


