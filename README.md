# Django Milestone Project

This is my Milestone Project for Full Stack Development.

## Travis Continuous Integration Testing:

[![Build Status](https://travis-ci.org/jepainter/MilestoneProject4.svg?branch=master)](https://travis-ci.org/jepainter/MilestoneProject4)

# Milestone Project 4: Artifact Hunters Website

The deployed website can be accessed from here (Heroku): [Artifact Hunters](https://artifact-hunters.herokuapp.com/)

## Temporary note for the assessor (this section will be removed in future):

- The website has various user types that have different priviledges in terms of actions they can take.  For testing of the super user / administrative account please use the following log in information:
    - Email: ubradmin@yahoo.com
    - Password: qazwsxedc1234
- The information above is made available to the assessor to demonstrate the full functionality of the site, and will be changed once the assessment has been completed.
- Other account types (regular user) can be assessed by registering a new account.
- Visitor accounts need no registrations, and will demonstrate limited functionality of the site in line with previleges.

## Goal of the website

The website created is a responsive and interactive auction and commerce website giving the user the opportunity to view artifacts on sale, place and adjust bids, outright purchase artifacts, compile a review for an artifact that is owned by them, as well as contribute to the history of an artifact that is owned by them. The site also supports the processing of successful bid or purchases for payment and recording the order information. 

The website in predominatentely managed by the site owner through the admin panel as the superuser (CRUD of artifacts, categories, bid_events).


### Project Purpose:
The project purpose is to demonstrate Full Stack development of a website, including the accessing, manipulating (through CRUD operations) and displaying data retrieved from a relational database.
The website utilises a PostGres database together with Python code to access and manipulate the data.  Visualisation is done with HTML, CSS and JavaScript where required, utilizing the Django framework.

## Limitations:

- Screening for controversial content is not caterred for, however site owner has access to delete any content, regardless of contributor.

## UX

This website provides the relevant functionality to satisfy the requirements, in detail (guided by user stories/requirements):
- Provide the opportunity to view categories, artifacts, history and reviews without having to register with or login to the site.
- Provide the opportunity to register for or login to the site, in order to take part in bidding or purchasing of artifacts, as well as contribute to reviews or histories of artifacts if it is owned by the user.
- Provide the opportunity for the site owner to create, update and delete categories as needed for the site, through the admin panel.

### User Stories:
- As a person interested in rare artifacts, I want to view wat is available for bidding or purchase, read history and reviews of the artifacts.
- As a member of the site, I want to be able to take part in bidding and or outright purchase artifacts from the catalogue.
- As a member of the site, I want to be able to add to the history of artifacts or add reviews of artifacts that I do own.
- As a member of the site, I want to be able to update my details, or reset my password if I have forgotten it.
- As the site owner, I want to be able to create, edit or delete categories of artifacts on the site.
- As the site owner, I want to be able to manage histories of artifacts, deleting them if necessary (if content not suitable).
- As the site owner, I want to be able to set bid events, so that the user can partake in bidding.
- As the site owner, I want to process succesful bids and purchases by providing the user an opportunity to fill in payment details and complete a sale.

### Wireframes:
Wireframes for the initial development of the site and database structure can be found here:
- [Mobile](#)
- [Desktop](#)
- [Database](#)

### Design considerations:
It was decided to style the website with a simple and warm feel:
- Complementing yet contrasting colours.
- Multi page layout, with visibility of certain pages only available to logged in users (bid management section, edit profile, etc.).
- Simple and logical navigation.
- Intuitive user input requirements for quick and easy information capturing.
- Feedback regarding success of input to keep user informed of progress/changes.

The design utilises the Bootstrap grid system, containers and components responsive to different screen sizes and devices, styled with the Bootswatch Sandstone theme. 

This site is limited to the use of HMTL, CSS, JavaScript, Python, Django and PostGres. 

## Features

### Existing Features
- Feature 1 - Navigation: Simple navigation of the site that jumps to the selected section on the site (at top of each page).
- Feature 2 - Categories: Ability to view artifacts in catalogue in a specific category, and select a specific artifact for detailed info (review, history, etc)
- Feature 3 - Artifacts: Ability to view all artifacts in catalogue, grouped according to in stock/out of stock.
- Feature 4 - Bidding: Ability to bid on a artifact (if registered and logged in). Bidding allows user to amend or remove a bid.
- Feature 5 - My Bids: Ability to to manage all bids from a central location, and process if successful(pay and archive) or unsuccessful (archive).
- Feature 6 - Purchase: Ability to outright purchase an artifact which is stored in the cart.
- Feature 7 - Payment: Ability to fill in details regarding a artifact in the cart (either outright purchase or successful bid), in order to close sale.
- Feature 8 - Add Review: Ability to add review for a specific artifact, if logged into the site and owner of the artifact.
- Feature 9 - Add History: Ability to add hisotry events for an artifact, if logged into the site and owner of the artifact. Superuser will be able to add history events for the artifact as well.
- Feature 10 - Register User: Ability to register as a new user for increased functionality (only if logged in).
- Feature 11 - Log In: Ability to log in as user, for increased functionality.
- Feature 12 - Profile/User Management:  Ability to view and update own profile (regular user and super user).
- Feature 13 - Password Reset: Ability to reset password securely if user forgets password.
- Feature 14 - Social Media: Links to social media platforms.

### Features Left to Implement
- Feature A - Email order to purchaser on succesful conclusion of sale.
- Feature B - Improved search functionality to allow searches based on categories, dates added, alphabetical order etc.
- Feature C - Storage of greater number of images for specific artifact, in order to display more aspects of a specific artifact.
- Feature D - Pagination for better display as catalogue grows.

## Technologies Used

The following languages, frameworks, libraries, IDE, repositories and tools were used for the creation of this website:

- [HTML](https://en.wikipedia.org/wiki/HTML)
    - This project utilises the **HTML** language and sematic elements for basic layout and function.   

- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - This project is styled using **CSS** where required for classes and specific elements. 

- [Bootstrap](https://getbootstrap.com/)
    - This project utilizes the **Bootstrap** grid system and components (incorporated through the Bootstrap CDN), to create the layout and responsive design of the page.

- [Bootwatch](https://bootswatch.com/sandstone/)
    - This project relies on the Bootswatch Sandstone theme for styling of the site and Bootstrap grid system and components.

- [FontAwesome](https://fontawesome.com/)
    - This project utilises **FontAwesome CDN** for icons utilised on the website. 

- [jQuery](https://jquery.com/)
    - This project utilises **jQuery** for the responsive navbar.

- [Popper.js](https://popper.js.org/)
    - The project uses **Popper.js**  for the responsive navbar.

- [AWS Cloud9](https://www.awseducate.com)
    - This project was created using **AWS Cloud9** IDE for development, as well as committing of progress to GitHub and Heroku. 

- [Travis CI](https://travis-ci.org)
    - This project uses **Travis Continuous Integration Testing  Cloud9** for build testing.

- [AWS S3](https://aws.amazon.com/)
    - This project uses **Amazon Web Services S3** for hosting of static and media files.

- [AWS IAM](https://aws.amazon.com/)
    - This project uses **Amazon Web Services IAM ** for access management between the hosted app and S3.

- [Heroku](https://www.heroku.com/)
    - This project uses **Heroku** for hosting and running of the application.

- [GitHub](https://github.com)
    - This project uses **GitHub** for hosting of project repository. 

- [FreeLogoDesign](https://www.freelogodesign.org/)
    - Used **FreeLogoDesign.org** to generate a logos for the site.

- [Favicon](https://www.favicon-generator.org/)
    - Used **Favicon-generator.org** to generate at favicon for the site from a logo designed.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - This project was tested using the **W3C CSS Validation Service** for checking conformity and validity of css content. 

- [Autoprefixer CSS Online](https://autoprefixer.github.io/)
    - Used **Autoprefixer CSS Online** tool to update/confirm prefixes for style.css code.

- [AutoPEP8](https://pypi.org/project/autopep8/)
    - Used **AutoPep8** to auto format Python code to conform to PEP8 standards.  Some deviation have been allowed for sake of readibility.

## Testing

Testing for this site was performed as follows:

### Code Validation:
The index.html file was not passed through the W3C HTML Validation site, due to the use of the Flask Framwork, many errors and warnings raised.
The style.css file was tested using the W3C CSS Validation site, with no errors reported.
The style.css file was run through the Autoprefixer CSS Online tool.

The site was tested on Google Chrome (desktop and mobile through dev tools), Opera (desktop only), Edge (desktop only) and Safari (mobile only iPhone6) for functionality.  Verified working well.

This site was also tested manually in line with the user stories and general functionality.  Testing is detailed in the testing matrix - [Testing Matrix](#).

## Deployment

This project is deployed on Heroku and GitHub and is accessible as follows:
- Website: [Heroku](https://artifact-hunters.herokuapp.com/)
- Repository: [GitHub](https://github.com/jepainter/MilestoneProject4)

For this project I used the AWS Cloud9 IDE platform [AWS Cloud9](https://www.awseducate.com) via the AWS Educate portal.
The platform allowed me to commit my pages (and changes) to Git, following which it was pushed through to the [GitHub repository](https://github.com/jepainter/MilestoneProject4).

Deployment of the website from to Heroku can accomplished through the following method: 
1. Log into the Heroku website. 
2. Install the Heroku CLI in the IDE terminal.
3. Log into Heroku from the IDE terminal using $ heroku login.
4. Clone the repository by typing ```heroku git:clone -a ultimate-book-review``` and then ```cd ultimate-book-review``` into your IDE terminal.
5. Changes and updates to code can be made in the IDE.
6. To deploy changes to Heroku type ```git add <your filename>```, followed by ```git commit -m "messaage regarding changes"``` and lastly ```git push heroku master``` into the IDE terminal.

This website can also be locally deployed by following the method outlined below:
1. Use the following link to access the project repository: [GitHub](https://github.com/jepainter/MilestoneProject3).
2. Click on the **Clone or Download** button, under the repository name.
3. Copy the clone URL for the repository, found in the **Clone with HTTPS** section. 
4. Open **Git Bash** in your local IDE environment.
5. Select the location to where the cloned directory must be made.
6. Input ```git clone``` together with the copied clone URL into Git Bash and press Enter.

The deployed version on **Heroku** is the same as the development version.

## Credits

### Content
- Artifact and category pictures have been sources from [Pixabay](https://pixabay.com/) and Google image searches, and used purely for educational purposes.
- Artifact details (history) have in part been obtained from [Wikipedia](https://www.wikipedia.org/) and is used purely for educational purposes.
- Wallpaper background obtained from [Pixabay](https://pixabay.com/) and is used purely for educational purposes.

### Code
- Code have been adapted from [Code Institute's](https://codeinstitute.net/) course material.
- Implementation of certain code have been adapted from the [Django Documentation](https://docs.djangoproject.com/en/3.0/)

### Acknowledgements
- I would like to thank my mentor, Dick Vlaanderen, for input provided during the development of the site.
