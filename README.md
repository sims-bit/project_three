|Reciply

Contents

Project Introduction
UX Design 
Features
Data Model
Technologies Used
Testing
Deployment
Security Features
Version Control
Credits

1. Project Introduction

    Live site - [|Reciply](https://twe-app-1641f237327d.herokuapp.com/)

    Repository - [Github](https://github.com/sims-bit/project_three.git)

The site is for home cooks of all skill levels who want to create delicious, approachable meals for their families and friends. This includes busy parents looking for quick weeknight solutions, cooking enthusiasts eager to try new recipes and techniques, and beginners who need clear, step-by-step guidance. The audience values practical cooking tips, a space to ask for advice and guidance, and recipes that bring people together around the dinner table.

2. UX Design

User Stories
Information Architecture
Wireframes
    Wireframes were created in Balsamiq, the wireframes were used to get a general jist of what the site may look like when finished.

<details>
    <summary>Landing Page</summary>
    <br>
    <img src="readme_media/landing_page_wireframe.jpg" alt="">
    </details>

<details>
    <summary>Post Page</summary>
    <br>
    <img src="readme_media/individual_post_wireframe.png" alt="">
    </details>

<details>
    <summary>Registration</summary>
    <br>
    <img src="readme_media/registration_wireframe.png" alt="">
    </details>

<br>
<strong>Design Decisions and Reasoning</strong>
<br>

- Minimal design
- The design uses a clean, card-based layout with generous white space that creates visual breathing room.
- The navigation is minimal and unobtrusive at the top. Recipe titles are given appropriate emphasis while author tags and timestamps provide secondary information in a subtle manner.
- The design employs a neutral color palette with pops of teal/turquoise in the author tags, creating visual consistency. The typography appears clean and readable, supporting the content-first approach.


<br>
<strong>Accessibility Considerations</strong>

<br>
<strong>Responsive Design Features</strong>
<br>
- Responsive design prioritizing mobile devices with adaptive templates
- Collapsible navigation menu optimized for mobile interfaces
- Intuitive, accessible interface designed for optimal readability

<br>
3. Features

    - Homepage
    - Navigation Bar
    - Fixed Footer
    - Individual blog post page
    - Register page
    - Login page
    - Django Admin page

<strong>CRUD Functionality</strong>

- Registered users to the site have the ability to create, view, edit and delete comments on Posts. 
- Admin can approve or delete comments and create blog posts.

<strong>User Authentication and Authorization</strong>
- User account creation and authentication system with sign-in/sign-out capabilities. 
- Comment posting requires user authentication, and comment moderation is handled by administrators through the Django Admin interface.


<strong>User Interaction Features</strong>

- Registered users can add comments to any post.
- New comments await superuser moderation before going live.
- A comment input form appears on every individual post page.

Navigation Structure

Future Feature Roadmap

    Profile Pages for Users
    Enable users to search blog posts through the navbar

4. Data Model



<details>
    <summary><strong>Entity Relationship Diagram</strong></summary>
    <br>
    <img src="readme_media/erd_diagram.jpg" alt="">
    </details>
<br>
The diagram illustrates the following relationships: 
- One Author/ User can have many posts. One - Many
- One Post can have many comments. One - Many

Cloudinary is used to store all user uploaded images. Two models were created for this project: Post and Comment. I have included Djangos default user model within the diagram for clarity.


5. Technologies Used

<strong>Languages Used:</strong>

    HTML5
    CSS3
    JavaScript
    Python
    Django Templating Language

<strong>Frameworks and Libraries:</strong>

    Django
    Django Allauth
    Django Crispy Forms
    Bootstrap
    Cloudinary
    Gunicorn
    Psycopg2
    Summernote
    dj_database_url


<strong>Software and Web Applications used:</strong>

    Heroku
    Heroku PostgreSQL
    SQLite3

    HTML Validator
    W3 CSS Validator
    JSHint
    PEP8 Online
    Lighthouse
    Balsamiq 

Version control:

    Git & GitHub


6. Testing

<details>
    <summary><strong>HTML Validation</strong></summary>
    <br>
    <img src="" alt="">
    </details>

<br>
<details>
    <summary><strong>CSS Validation</strong></summary>
    <br>
    <img src="" alt="">
    </details>

<br>
<details>
    <summary><strong>HTML Validation</strong></summary>
    <br>
    <img src="" alt="">
    </details>


<br>
<strong>Manual Testing Procedures</strong>


| Test Description | Outcome | Status |
|---  | --- | --- |
|Registration Required Fields | Verifies that all mandatory form fields(username, email, password) must be completed before account creation | Pass |
|Successful Registration |Confirms that valid user data creates a new accountand redirects appropriately | Tests that password and confirmation passwordfields must match during signup |
|Password Confirmation | Tests that password and confirmation password fieldsmust match during signup| Pass |
|Sucessful Login| Validates that registered users can access their accountswith correct credentials | Pass |
|Login Status Check| Verifies that the system correctly identifies andmaintains user authentication state | Pass |
|User Registration |  General test of the complete registration workflow fromform submission to account activation | Pass |
|Invalid Login Attempt | Ensures proper error handling when incorrectusername/password combinations are entered | Pass |
|Log Out Functionality| Confirms users can properly terminate their sessionsand return to logged-out state | Pass |
|Post Display | Tests that blog posts or content items render correctly forusers | Pass |
|Creating New Post | Validates that authenticated users can successfullycreate and publish new content | Pass |
| | | |
| | | |
| | | |
| | | |


    Cross-Browser Compatibility
    Mobile Responsiveness
    
User Testing Results
Known Bugs and Fixes
Outstanding Issues

7. Deployment

    The prerequisites

<strong>Database Setup</strong>
    - Navigate to PostgreSQL from Code Institute
    - Enter in your student email address and click submit
    - Wait whilst your database is created
    - Your database is sucessfully created, you will receive an email with the database link

<strong>Heroku Deployment</strong>

- Log into Heroku and create a new app with a unique name. This will be added to the allowed hosts in the project settings.
- Following on, within the setting tab of your app:
- Locate the 'Reveal Config Vars', in which we shall be adding a new Config Var called DISABLE_COLLECTSTATIC, assign it the value of 1 and then save it via clicking add. This will be removed when relasing for production.
- Add a new Config Var called SECRET_KEY and assign it a value - any random string of letters, digits and symbols. (You can use an online generator for this) Click add to save.
- Add a new Config Var called DATABASE_URL and paste in the value of your Code institute PostgreSQL database,click Add to save.
- In the top layer of your directory create a file env.py, this file needs to be then added to the .gitignore file as this is where the DATABASE_URL and SECRET_KEY variable will be stored.
- The settings.py should be updated to use the DATABASE_URL and SECRET_KEY environment variable values:

        import os
        import dj_database_url
        if os.path.isfile('env.py'):
        import env

    Replace secret key placeholder with: 

        SECRET_KEY = os.environ.get('SECRET_KEY')

- Create a Procfile within the top level of your directory
- Within the Procfile add: 

        web: gunicorn project_name.wsgi


- Save all files and Make Migrations: python3 manage.py migrate
- Deploy the branch, when finished click on Open App to visit the live site. 


<br>
<strong>Connect your Github Repo to the Heroku App</strong>

    - Navigate to your deploy tab within your Heroku App
    - Select Github as the deployment method, and if prompted confirm that you want to connect to Github. Enter and search for the name of your chosen repository and click on Connect to link them. 
    - Return to the deploy tab of the app each time you push changes to Github. Scroll to the bottom and Manually deploy the app by clicking on 'Deploy Branch'. 


Local Development Setup
Environment Variables


Differences Between Development and Production Environments

8. Security Features

Authentication Implementation
Data Protection Measures
Environment Variables Usage
Defensive Programming Techniques
Input Validation

9. Version Control

10. Credits

    Code Institute: Walkthrough modules, resources and materials in Full Stack Frameworks.
  [Code Institute](https://codeinstitute.net/global/)

    Unsplash https://unsplash.com/@brookelark


