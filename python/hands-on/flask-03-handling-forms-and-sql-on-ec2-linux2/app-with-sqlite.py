# Install flask_sqlalchemy to your bash/oper sys/instance. "pip install flask_sqlalchemy"
# Import Flask modules. 
# Create an object named app
# Configure sqlite database
# Execute the code below only once.
# Write sql code for initializing users table..
# Write a function named `find_emails` which find emails using keyword from the user table in the db,
# and returns result as tuples `(name, email)`.
# Write a function named `insert_email` which adds new email to users table the db.
# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
#using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')
#Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')
# Add a statement to run the Flask application which can be reached from any host on port 80.
    #app.run(host='0.0.0.0', port=80)