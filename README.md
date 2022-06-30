# Project 3: Cake Sera Sera
## A full stack Django application by Richard Afrane-Kesey, Chris Ailey and Marc Usher

**Deployed App on Heroku:** [Cake Sera Sera](https://cakeprojectapp.herokuapp.com/)

## Introduction
For this Django full stack application project, the team decided to create a website that would allow budding bakers to add their versions of their favourite cakes to a database and see others' recipes too. Visitors to the site would also be able to browse the full database, but without the option to add cakes or recipes.

The idea was to crowdsource variations of well known and lesser known cakes from a community of enthusiastic home bakers, also allowing for people to share variations of the cakes that use different ingredients or cater to different dietary requirements. If the cake doesn't yet exist, a user can add it to the database.

## Technologies Used
* Python
* Django
* PostgreSQL & pgAdmin
* Bulma CSS Library and additional custom CSS
* Front-end Javascript & jQuery
* Heroku (for deployment)


## Approach
[Project Trello Board](https://trello.com/invite/b/cm2jmZuT/d458fa353c6048c1ef123e2b9457e1d0/ga-project-3)

![Website Flow Chart](https://trello.com/1/cards/62b5e598273de413c9f1ee90/attachments/62b5e5be95c2cb41f3c9c91b/previews/62b5e5c195c2cb41f3c9ca48/download/Cake_Recipe_Site_Flowchart_v01.jpg)

## Application Architecture
### ERD
![Project ERD](https://trello.com/1/cards/62b5e53532359505ca19185d/attachments/62b5e58d6e82706751d1e593/previews/62b5e58d6e82706751d1e5da/download/Cake_Project_ERD.jpg)

### USER STORIES
* As a visitor, I want to be able to browse the cakes to see which ones I want to make.
* As a visitor, I want to be able to see the details of a cake to find out how to make it.
* As a visitor, I want to be able to sign up and log in as a registered user, so I can access the full user functionality of the site.
* As a registered user, I want to be able to add a new cake to the database so I can share it with others.
* As a registered user, I want to add my own recipes to existing cakes so others can see how I made it.
* As a registered user, I want to be able to edit/delete the cakes and recipes that I've added so they can stay current.

### WIREFRAMES
[Full Wireframes on Figma](https://www.figma.com/file/TZoFGaVXjTqfhnrhjKanf3/Project-3---Have-your-cake-and-eat-it?node-id=0%3A1)
* Home Page - For Visitors
![Home Page - For Visitors](https://trello.com/1/cards/62bda022f57beb1bff75fca8/attachments/62bda06657db3e2b8341324e/previews/62bda06657db3e2b83413290/download/image.png)
* Home Page - For Users
![Home Page - For Users](https://trello.com/1/cards/62bda022f57beb1bff75fca8/attachments/62bda03e59802f1b550a3d44/previews/62bda03f59802f1b550a3d8b/download/image.png)
* Cake Index
![Cake Index](https://trello.com/1/cards/62bda022f57beb1bff75fca8/attachments/62bda08682bd755b6b00051a/previews/62bda08682bd755b6b000531/download/image.png)
* Cake Detail
![Cake Detail](https://trello.com/1/cards/62bda022f57beb1bff75fca8/attachments/62bda0adb4dca44688de4856/previews/62bda0aeb4dca44688de489e/download/image.png)
* Cake Detail - Modal
![Cake Detail - Modal](https://trello.com/1/cards/62bda022f57beb1bff75fca8/attachments/62bda0d892f37e1cb1d4a79b/previews/62bda0d992f37e1cb1d4a80f/download/image.png)

## Major Hurdles Overcome
* Pagination on the Cake Index page but particularly of the recipes on the Cake Detail page
* Successful redirects back to relevant cake details page from recipe edit/recipe delete
* Hiding Recipe Add form on the Cake Detail page as a modal to allow correct database entry of Cake ID as a Foreign Key
* Linked Bulma notification classes with Django message classes in settings.py
* Delving into Django documentation and finding it easy to navigate for additional functionality (particularly around pagination and authentication)
* Adding success/error notifications with class-based views, particularly login/logout for authentication

## The road not yet walked - What we'd like to have added
* Dropdown menu under 'view all cakes' that would take you to a filtered index view by flavour
* Recipe cards on the individual cake pages to have a 'full details' button for a modal would pop up with the full recipe information
* Additional authentication features - password reset using email and verification email upon registration. All seemed reasonably straightforward to implement in Django but we didn't have the time to hit this stretch goal.