# Exam Center Management System

A beginner-friendly Django CRUD application developed to understand Django Forms, ModelForm, database handling, and the complete flow of a Django application.

This project is the second Django learning project after the Staff Management System. The main focus of this project was to improve the application structure by using Django Forms instead of manually creating HTML forms.

## Project Overview
The Exam Center Management System helps manage exam center information.

The application supports basic CRUD operations:
- Add Exam Center
- View Exam Centers
- Update Exam Center Details
- Delete Exam Center Records

The main objective of this project was to understand how Django Forms connect frontend forms with backend models and databases.

## Technologies Used

Backend:

- Python
- Django
- Django Forms
- PostgreSQL

Frontend:

- HTML
- CSS
- Bootstrap

Development Tools:
- VS Code
- Git
- GitHub

## Django Concepts Learned

During this project, I learned and practiced:
- Django project and app structure
- MVT (Model View Template) architecture
- Django Models
- Database migration
- Django ORM
- URL routing
- Views and request handling
- Django Forms
- ModelForm
- Template inheritance
- CRUD operations
- PostgreSQL database connection

## Application Flow

The basic flow of the application:

User
↓
HTML Template
↓
Django URL
↓
View Function
↓
Django Form
↓
Model
↓
PostgreSQL Database

## Project Features

### Add Exam Center

Users can add new exam center details using Django Forms.

The form automatically handles:

- Field generation
- Data validation
- Saving data into database

### View Exam Centers

Displays all available exam centers in a table format.

Users can:
- View complete details
- Edit records
- Delete records

### Update Exam Center

Existing exam center data is loaded into Django Form.
Users can modify information and update the database.

### Delete Exam Center

Allows removing unwanted exam center records from the database.

## Model Structure

The Exam Center model contains:

- Center Name
- Center Code
- Address
- City
- State
- Pincode
- Contact Number
- Email
- Capacity
- Created Date
- Updated Date

Django automatically generates:
- Primary Key ID
- Created timestamp
- Updated timestamp

## Django Forms Implementation

Instead of manually creating HTML input fields, this project uses Django ModelForm.

Example:

class Meta:

    model = ExamCenter

    fields = "__all__"

Benefits of Django Forms:
- Automatic form generation
- Built-in validation
- Cleaner code
- Better connection between Model and Template

## Template Structure

templates/
└── exam_center/
├── base.html
├── home.html
├── add_exam_center.html
├── view_exam_center.html
└── update_exam_center.html

## Template Inheritance

This project uses Django template inheritance.

Common elements like:
- Page structure
- Bootstrap CSS
- Common layout

are handled using:
base.html
Other pages extend the base template:

{% extends "exam_center/base.html" %}
This reduces duplicate HTML code and makes the project easier to maintain.

## Database

This project uses PostgreSQL.

Database communication is handled through Django ORM.

Examples:

Fetching all exam centers:
ExamCenter.objects.all()

Getting a single record:
ExamCenter.objects.get(id=id)

Deleting a record:
object.delete()

## Frontend Development and Styling

The frontend layout and Bootstrap styling of this project were developed with the assistance of AI using ChatGPT.

AI assistance was used for:

- Creating clean HTML structure
- Improving Bootstrap layouts
- Organizing page design
- Improving navigation structure
- Making forms user-friendly
- Maintaining consistent styling across pages

The main purpose of using AI assistance was to improve frontend presentation while understanding how Django templates connect with backend logic.

## Learning Improvement From Previous Project

Compared with the previous Staff Management System, this project introduced:

- Django Forms instead of manual HTML forms
- ModelForm integration
- Better template organization
- Template inheritance using base.html
- Cleaner CRUD implementation

## Future Improvements

Possible future enhancements:

- User authentication
- Admin and staff roles
- Google Maps integration for exam center location
- Latitude and longitude storage
- Search functionality
- Pagination
- Image upload
- Deployment on cloud platform

## Author

Keshav

Learning Django by building practical projects.