from datetime import date
from urllib import request
from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = {
  "Billy Bob": "Boston Celtics",
  "Joe Mama": "Phoenix Suns",
  "Juandale Pringle": "Milwaukee Bucks",
  "LeBron James" : "Los Angeles Lakers",
  "Bobby Shmurda": "Golden State Warriors"
}



@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    now = datetime.now()
 

    currentDate = now.strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', currentDate=currentDate)


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']

    # Write your to code here to check whether number is even or odd and render result.html page

    if number is None or number=='':
        result_string = "No number provided...bruh :("
    else:
        try:
        # converting to integer
            int_number = int(number)
            even_or_odd = "Even" if int_number % 2 == 0 else "Odd"
            result_string = number + " is " + even_or_odd + "."
        except ValueError:
            result_string = "Provided input is not an integer!"

        
    return render_template('result.html', result_string=result_string)



@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    studentOrg = request.form['Organization']

    # Append this value to studentOrganisationDetails
    studentOrganisationDetails[studentName] = studentOrg
    # Display studentDetails.html with all students and organisations
    return render_template('StudentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
