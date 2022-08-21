# General Assembly Project 3 - Cake Sera Sera

## Table of Contents
* Introduction
    * Brief
    * Project Overview
    * Team Members & Timeframe
    * Technologies Used
* Approach Taken
    * Project Planning
    * User Stories
    * ERD
    * Wireframes
* Build Process (featured code)
* Final Product
* Conclusions
    * Wins & Challenges
    * Bugs
    * Future Improvements
    * Key Learnings

## Introduction

### Brief

* **Work in a group of three to build a full-stack web application from scratch** using the Django framework 
* **Use Django, Python, HTML, CSS, JavaScript and an SQL database (PostgreSQL)** to build the application with MVT architecture.
* **Create the application using at least 2 related models**, one of which should be a user.
* **Include all major CRUD functions** for at least one of your models.
* **Add authentication AND authorization** (page protection) to restrict access to appropriate users, including:
    * User must be able to sign up or login.
    * Signed in user must be able to change password and logout.
    * Change password and logout must only be available to logged in users.
* **Give feedback to the user after each action**, and after form submissions with success/failure.
* **Layout and style your front-end with clean & well-formatted CSS**, with or without a framework. Put effort into your design!

### Project Overview - Cake Sera Sera

For this full-stack application, the team decided to create a website that would allow budding bakers to register and add their versions of their favourite cakes to a database and see others' recipes too. Visitors to the site would also be able to browse the full database, but without the option to add cakes or recipes.

The idea was to crowdsource variations of well known and lesser known cakes from a community of enthusiastic home bakers, also allowing for registered users to share variations of the cakes that use different ingredients or cater to different dietary requirements. If the cake doesn't yet exist, a user can add it to the database.

![Cake Sera Sera screenshot](/main_app/static/images/readme/appscreenshot-01.png)

### Deployed App

[Visit Cake Sera Sera](https://cakeprojectapp.herokuapp.com/ )

### Team Members

[Chris Ailey](https://github.com/C-T-Ailey) (Team Lead)
[Marc Usher](https://github.com/MarcUsher)
[Richard Afrane-Kesey](https://github.com/richard70UKGithub)

### Timeframe

1 week



### Technologies Used

* Python
* Django
* PostgreSQL & pgAdmin 4
* HTML5
* CSS3 and Bulma CSS Framework
* JavaScript & jQuery
* Git & GitHub
* Figma (for mockups)
* Visual Paradigm (for ERD)
* Trello (for planning)
* Heroku (for deployment)


## Approach

### Project Planning

Our first step in the planning process was to map the routes and CRUD operations through the application in the below flow chart.

This gave the team a clear idea of the site flow, and allowed us to start discussing ERDs and an overview of how we might split the project out.

![Cake Sera Sera site map](/main_app/static/images/readme/sitemap-01.png)

We used Trello to keep all our planning resources together and also keep our User Stories clearly visible to the whole team throughout the build.

We agreed we would also start and end each day with a short stand-up in order to assign tasks for the day ahead and review progress, with regular check-ins throughout each day in order to push and pull updates and make sure none of us was struggling with any blockers on our individual tasks.

In the event one of us ran up against a difficult issue, we would go back to pair programming until the issue was resolved; this ensured that obstacles would be overcome as quickly as possible and everyone could proceed onto the next task, rather than leaving one teammate to struggle while the others pressed on with their own development.

This flow repeated until completion - we would look at which pieces of the project remained incomplete, decide amongst ourselves which we felt most comfortable to attempt, and assisted each other in completing them whenever necessary.

![Project Trello](/main_app/static/images/readme/trello-01.png)

### User Stories

Once we had a clear idea of the website flow, we created our key user stories in order to make sure we hadn’t overlooked any activity that a visitor or user of the site would want or expect to do.

* As a visitor, I want to be able to browse the cakes to see which ones I want to make.
* As a visitor, I want to be able to see the details of a cake to find out how to make it.
* As a visitor, I want to be able to sign up and log in as a registered user, so I can access the full user functionality of the site.
* As a registered user, I want to be able to add a new cake to the database so I can share it with others.
* As a registered user, I want to add my own recipes to existing cakes so others can see how I made it.
* As a registered user, I want to be able to edit/delete the cakes and recipes that I've added so they can stay current.

### ERD

We then created our full ERD, refining the rough ideas we’d had when creating the site flow chart and pinning down exactly what each model would include and how each model would be related. 

We wanted each cake to have multiple recipes to accommodate variations from different users, with each user able to add as many cakes and recipes as they wanted. Each cake and recipe would also include a referenced user ID so that we could easily limit the Edit and Delete functionality to the user who had created the record.

![Entity Relationship Diagram](/main_app/static/images/readme/erd.png)

### Wireframes

For the first two days of the build we focused on functionality over styling, using the Materialize CSS Framework for quick basic styling. 

Once our key functionality was up and running, we then spent time creating wireframes of how we wanted the site to look, so the whole team would be working towards the same design and we’d have consistency across our pages and elements.

We also decided we would use the Bulma CSS Framework for the final styling and design of the site, as after some research I found it seemed to integrate well with Django, particularly for styling forms.

**[Full Wireframes on Figma](https://www.figma.com/file/TZoFGaVXjTqfhnrhjKanf3/Project-3---Have-your-cake-and-eat-it?node-id=0%3A1)**

Home Page - For Visitors
![Wireframe - Home page for visitors](/main_app/static/images/readme/wireframes-01.png)

Home Page - For Users
![Wireframe - Home page for Users](/main_app/static/images/readme/wireframes-02.png)

Cake Index
![Wireframe - Cake Index](/main_app/static/images/readme/wireframes-03.png)

Cake Detail
![Wireframe - Cake Detail](/main_app/static/images/readme/wireframes-04.png)

Cake Detail - Modal
![Wireframe - Cake Detail Modal](/main_app/static/images/readme/wireframes-05.png)

## Build Process

### Day 1 - Planning and setup

We worked together as a team to plan the project on the first day as outlined above, and once we had agreed the scope of the project and what needed to be done we began with pair programming sessions to construct the bones of the app around our MVT architecture - the initial URL paths, the models we intended to use, and some placeholder templates.

Once the app was in a state where we could individually work on separate aspects of it, we assessed our flowchart, discussed which features we had the groundwork to implement, and assigned an area of the app to develop independently.

I chose to work on the authentication and authorisation of the website as I was keen to learn to do this in Django after having worked on it extensively in Express for my second General Assembly Project.

Using Django’s class-based views this was quite straightforward as I was happy to use the built in User model which suited our requirements very well. The main challenge was customising some of the built-in functionality associated with the User model’s class-based view, specifically around the success messages, and also by creating a signup form and view.

Below is the signup form functionality I created for signup in `forms.py`:

```
class NewUserForm(UserCreationForm):
 class Meta:
   model = User
   fields = ['username', 'email', 'password1', 'password2']
  def save(self, commit=True):
       user = super(NewUserForm, self).save(commit=False)
       user.email = self.cleaned_data['email']
       if commit:
         user.save()
       return user
```

I then imported this into `views.py`:
```
def signup(request):
   if request.method == 'POST':
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           messages.success(request, 'You successfully signed up and are now logged in.')
           return redirect('/')
       else:
           messages.error(request, "Invalid sign up - try again.")
  
   form = NewUserForm()
   return render(request, 'registration/signup.html', {'form': form})
```
And created the form in `signup.html`:
```
{% extends 'base.html' %}
{% load bulma_tags %}
 
{% block title %}
Sign Up
{% endblock %}
 
{% block content %}
 
 
<section class="section">
   <div class="container is-max-desktop">
       <div class="content box">
           <h1>Sign Up</h1>
 
           <form method="post" action="{% url 'signup' %}">
 
               {% csrf_token %}
               {{ form|bulma }}
 
               <br>
 
               <input type="submit" class="button is-primary is-light" value="Sign Up!">
 
           </form>
       </div>   
   </div>
</section>
{% endblock %}
```
All our forms on the site used the CSRF Token middleware in Django to protect against Cross Site Request Forgeries.

As mentioned above, I also customised the authorisation views in order to add custom success messages, mainly using Django’s built-in messages framework and Success Message Mixin

```
class PasswordChange(SuccessMessageMixin, PasswordChangeView):
   success_message = "Password changed successfully."
   success_url = '/'
 
class LoginView(SuccessMessageMixin, LoginView):
   def form_valid(self, form):
           messages.success(self.request, f"You have successfully logged in!")
           return super().form_valid(form)
 
class LogoutView(LoginRequiredMixin, SuccessMessageMixin, LogoutView):
   def dispatch(self, request, *args, **kwargs):
       if request.user.is_authenticated:
           messages.info(request, "You have successfully logged out.")
       return super().dispatch(request, *args, **kwargs)
```

The below snippet shows the code I added to our `base.html` to which would display any messages generated by the application.
```
{% if messages %}
       <br>
       {% for message in messages %}
       <div {% if message.tags %} class="notification {{ message.tags }}"{% endif %} style="margin: auto;">
           <button class="delete" onclick="this.parentElement.style.display='none'" ></button>
           {{ message }}
       </div>
       {% endfor %}
   {% endif %}
```

This snippet is from the final application, where I went on to link the messages framework with notification styling from the Bulma CSS framework to dynamically update the colour of all our pop-up messages (see Day 4 - Final styling for more information on this).

### Day 2 - Authorisation & Add Recipe

I continued to work on adding custom success messaging to the rest of our existing CRUD functionality around Cakes and Recipes in the same way as I had done for our Authentication views.

I also picked up on the work Chris and Richard had done on adding a Recipe to an existing Cake in our database. They had been running into problems in getting the Recipe to automatically take the relevant Cake’s ID, as originally the ‘Add Recipe’ functionality would take you to a different URL which would no longer have the relevant Cake data to draw from.

I first moved the ‘Add Recipe’ functionality to sit on the relevant Cake Detail page, where it would be able to take the Cake ID from the data on the page. This worked and added the data correctly to our database, so I then decided to hide the ‘Add Recipe’ form in a modal, using the modal example from W3Schools.

Below is the Add Recipe view, including the Login Required decorator from Django which was added later.

```
@login_required
def add_recipe(request, pk):
   form = RecipeForm(request.POST)
   print(form)
   if form.is_valid():
       new_recipe = form.save(commit = False)
       new_recipe.cake_id = pk
       form.instance.created_by = request.user
       new_recipe.save()
       messages.success(request, f"Recipe successfully added.")
       return redirect('detail', pk = pk)
```

In the `cake_detail.html` I then hid the form behind a check that would only show to authenticated users, and only display the form as a modal when the user clicked the ‘Add Recipe’ button, and this would still be able to take the page’s relevant cake ID and pass it back to on submission of the form. The code snippet below is from the final app, when we had integrated the Bulma CSS Framework into the design. 

```
{% if user.is_authenticated %}
       <p>Get involved - add your favourite version of this cake here!</p>
       <a id="modal-button" class="button is-link is-light mt-3">Add Recipe for {{cake.name}}</a>
       <br>
       <div id="recipe-form" class="modal-recipe">
           <div class="modal-content content box">
               <h4>New Recipe</h4><span class="close">&times;</span>
               <form action="{% url 'add_recipe' cake.id %}" method="post">
                   {% csrf_token %}
                   {{ form|bulma }}
                   <input type="submit" class="button is-primary is-light" value="Add Recipe">
               </form>
           </div>
       </div>
       {% endif %}
```

I used the Bulma integration to style the all our form consistently, from Cake and Recipe CUD operations (including the modal) and all our authorisation forms, loading the relevant Bulma tags that could then be used to display the form with the following import in the relevant template files:
```
{% load bulma_tags %}
```

I also started to put more CUD functionality behind checks that would only display Edit and Delete buttons to the user who had created that cake or recipe. The snippet below is from `cake_detail.html`, to secure the Edit and Delete functionality.
```
{% if user.id == cake.created_by.id %}
    <hr>
    <a class="button is-primary is-light" href="{% url 'cakes_update' cake.id %}">Edit Cake</a>
    <a class="button is-danger is-light" href="{% url 'cakes_delete' cake.id %}">Delete Cake</a>
{% endif %}
```

### Day 3 - Final functionality and Bulma styling

By Day 3 we had completed nearly all of the technical requirements for the application, and so worked through the remaining functionality that was required by pair-programming.

The main issue still outstanding was an error that would occur when deleting a Recipe attached to a Cake - we could easily return the user to the Cake index, but wanted to instead send them back to the linked Cake. However, as Django uses a secondary Delete Confirmation page, this would then lose the relevant Cake ID from the page data.

After some research in Django’s documentation around URL utility functions, I was able to find a solution that worked:
```
class RecipeDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
   model = Recipe
   success_message = "Recipe successfully deleted."
   #success_url = reverse_lazy('detail', kwargs = {'pk': model.cake_id})
   def get_success_url(self):
       return reverse('detail', kwargs={'pk' : self.object.cake_id})
```

The final line allowed us to take the cake ID from the recipe being deleted and pass this as a primary key back to the Cake Detail view to display the relevant Cake.

We also decided to add a preset list of options that could be selected as Flavour types for our cakes, and attach a hexcode value to these which we could use to consistently style specific elements of the page depending on which cake flavour had been selected. The below snippet shows the final list of flavours and our Cake model which used these flavours.

```
FLAVOURS = (
   ('#f4f0d2', 'Plain Sponge'),
   ('#e8b26b', 'Caramel'),
   ('#d4a373', 'Chocolate'),
   ('#fff3c9', 'Cream Cheese'),
   ('#fad2e6', 'Fruit'),
   ('#d48c55', 'Spiced'),
   ('#fffeeb', 'Vanilla'),
   ('#f1b0ff', 'Experimental')
)
 
class Cake(models.Model):
   name = models.CharField(max_length=100)
   flavours = models.CharField(max_length=7, choices=FLAVOURS, default=FLAVOURS[0][0])
   description = models.TextField(max_length=250)
   imageurl = models.CharField(default=None, blank=True, max_length=300, null=True)
   created_by = models.ForeignKey(User, on_delete=models.CASCADE)
   def get_absolute_url(self):
       return reverse('detail', kwargs = {'pk': self.id})
```

Once our functionality was all completed, we then worked on fully integrating the Bulma CSS framework into our application and completing the design and styling. Some of the elements I worked on, such as forms, have already been discussed above, and only needed simple additional CSS to complete the styling.

My main task around Bulma integration on this day was to fully style our Cake Index page, allowing each cake in our database to display as a new Card element that could be clicked on to go to that Cake’s detail page.

It took some time to get my head around how Bulma’s layouts worked, with containers nested in sections and columns in containers, but after a lot of reading of their documentation and some trial and error I was able to get the cakes displaying in a nice Card format on the index page. Chris then worked on including pagination for the index page.

The below code snippet shows my loop to populate the page with a card of each Cake in our database, in the cake `index.html`. Here I have also used the hex code from the Cake’s flavour as the background colour for the card content:

```
<section class="section">
   <div class="container">
       <div class="container columns is-multiline">
           {% for cake in page_obj %}
           <div class="column is-half">
               <div class="card m-3">
                   <a href="{% url 'detail' cake.id %}" style="text-decoration: none; color: black">
                       <div class="card-image">
                           <figure class="image is-square">
                               <img src="{{ cake.imageurl }}" id="cakeImage"/>
                           </figure>
                       </div>
                  
                       <div class="card-content" style="background-color: {{ cake.flavours }}">
                           <h3 class="title is-3">
                               {{ cake.name }}
                           </h3>
                           <div class="content">
                           <p><b>Primary Flavour:</b>
                                   <br>{{ cake.get_flavours_display }}</p>
                               <p><b>Description:</b>
                                   <br>{{ cake.description }}</p>
                           </div>
                       </div>
                   </a>
               </div>
           </div>
           {% endfor %}
       </div>
```

I also added a Bulma full-width hero element to the top of the page that would have some impact on first viewing and differentiate it from the rest of the page, and would also show a prompt to visitors to sign up to the site so they could get involved.

```
<section class="hero is-warning is-light">
   <div class="container">
       <div class="hero-body">
           <p class="title">
           Our cake shelf
           </p>
           <p class="subtitle">
           Take a look at all the cakes added by our community of bakers, and the different recipes attached to each cake!
           </p>
           {% if user.is_authenticated %}
 
           {% else %}
           <p class="subtitle">Not a member yet?</p>
           <a href="{% url 'signup' %}"><button class="button is-link is-light">Sign up now!</button></a>
           {% endif %}
       </div>
   </div>
</section>
```

### Day 4 - Final styling

On the final build day we continued to work on design, styling and integrating Bulma across our shared elements for consistent design.

I finalised the pop-up success and error notifications, and linked the built-in message types in Django’s messages framework to Bulma classes that would then automatically display notifications in the colour we wanted, depending on which message type it was.

To do this across the application, I added the following code to our `settings.py` file which allowed me specify the Bulma classes that would apply to the different message types.

```
from django.contrib.messages import constants as messages
 
MESSAGE_TAGS = {
       messages.DEBUG: 'is-link is-light',
       messages.INFO: 'is-info is-light',
       messages.SUCCESS: 'is-primary is-light',
       messages.WARNING: 'is-warning is-light',
       messages.ERROR: 'is-danger is-light',
}
```

I updated the `base.html` to include these message tags as a class, and I also added a button allowing the user to close the notification.
```
{% if messages %}
    <br>
    {% for message in messages %}
    <div {% if message.tags %} class="notification {{ message.tags }}"{% endif %} style="margin: auto;">
        <button class="delete" onclick="this.parentElement.style.display='none'" ></button>
        {{ message }}
    </div>
    {% endfor %}
{% endif %}
```

I also worked with Richard to style the Cake Detail page so there would be consistency with our Cake index page. I added a similar hero element at the top, this time using the flavour hexcode as the background colour. I styled the Recipes to have similar card layouts to the Cakes on the Cake index, adding Bulma card footers to show the edit and delete links only if the authenticated user matches the user who created the record. 

Once all our styling was complete and our code merged and fully tested, Chris as our Team Lead deployed the app to Heroku, and we spent the remainder of our build time seeding the relevant data to our cloud database.

## Final Product

Homepage:
![Cake Sera Sera - Homepage part 1](/main_app/static/images/readme/appscreenshot-02a.png)
![Cake Sera Sera - Homepage part 2](/main_app/static/images/readme/appscreenshot-02b.png)

Cake Index:
![Cake Sera Sera - Cake Index part 1](/main_app/static/images/readme/appscreenshot-03a.png)
![Cake Sera Sera - Cake Index part 2](/main_app/static/images/readme/appscreenshot-03b.png)
![Cake Sera Sera - Cake Index part 3](/main_app/static/images/readme/appscreenshot-03c.png)


Cake Detail:
![Cake Sera Sera - Cake Detail part 1](/main_app/static/images/readme/appscreenshot-04a.png)
![Cake Sera Sera - Cake Detail part 2](/main_app/static/images/readme/appscreenshot-04b.png)
![Cake Sera Sera - Cake Detail part 3](/main_app/static/images/readme/appscreenshot-04c.png)

Signup page:
![Cake Sera Sera - Signup page](/main_app/static/images/readme/appscreenshot-05.png)

Login:
![Cake Sera Sera - Login page](/main_app/static/images/readme/appscreenshot-06.png)

Homepage for authenticated user:
![Cake Sera Sera - Homepage for authenticated user](/main_app/static/images/readme/appscreenshot-07.png)

Add Cake form:
![Cake Sera Sera - Add Cake form](/main_app/static/images/readme/appscreenshot-08.png)

Cake Detail page for logged in user:
![Cake Sera Sera - Cake Detail page for logged in user](/main_app/static/images/readme/appscreenshot-09.png)

Add Recipe modal:
![Cake Sera Sera - Add Recipe modal](/main_app/static/images/readme/appscreenshot-10.png)

Cake Detail for authenticated user who created the cake:
![Cake Sera Sera - Cake Detail for authenticated user who created the cake](/main_app/static/images/readme/appscreenshot-11.png)

Recipe list with recipe created by authenticated user:
![Cake Sera Sera - Recipe list with recipe created by authenticated user](/main_app/static/images/readme/appscreenshot-12.png)


## Conclusions

### Wins

* Meeting the technical requirements of the project by the start of the third day with good communication between the whole team.
* Generally delving into Django documentation and finding it easy to navigate for additional functionality (particularly around pagination, which was done by Chris, and authentication).
* Turning the Add Recipe form into a modal, so it was hidden from the user until needed but would still easily allow the correct database entry of the Cake ID as a Foreign Key
* Implementing the reverse() function to redirect back to the relevant Cake details page from recipe edit/recipe delete, which was a tricky problem to solve.
* Adding custom success/error notification messages to class-based views, particularly around authentication.
* Linking Bulma notification classes with the Django message framework.

### Challenges

* The biggest challenge of this project was using a new CSS Framework that none of the team was familiar with. The documentation for Bulma was very helpful, but as with all CSS frameworks to use it to its full potential it needed you to structure things in a specific way, and it took a while to get my head around the interactions between the various elements available and applying these to our application.
* Working in a team of 3 was also quite tricky, with all of us having different levels of comfort with Django and with CSS Frameworks, and dividing up the work equally so that everyone could contribute to the application.

### Bugs

* Success and error messages on the sign-up form display over the form itself rather than at the top of the page.
* Site is not entirely responsive as we were unable to implement a responsive navbar.
* Unfortunately, we initialised our Git folders in the wrong locations at the beginning of the process, so when it came time to host the app on Heroku we ran into one issue after another. The only solution to this issue was to each create a new repository for our project and migrate our files over with the correct structure - this means that the majority of our project's commit history was confined to now-obsolete repositories.

### Future Improvements 

* Add a dropdown filter on the Cake index page that would allow visitors and users to filter by flavour.
* Recipe details to display full information as a modal - we wanted to update the recipe cards on the Cake detail pages to include a ‘full details’ button which would open a modal when clicked showing the full details of that recipe - this would cut down on the size of the Recipe cards, which are quite long. We started working on integrating this using Bulma modals but didn’t have time to fully complete this.
* Additional authentication features - password reset using email and verification email upon registration. The documentation for this seemed straightforward to implement in Django, but in the end I didn't have the time to implement this stretch goal of the brief.

### Key Learnings

* As with Project 2, the importance of open and regular communication was key in this project, and a big takeaway for me. Working in a team of 3 was very different to working in a pair as the division of work became much more granular, but we were very focused with our project management and very open if any of us was struggling with a problem so that we could come together to help debug and find a solution as a group.
* The importance of good documentation! Django’s documentation was fantastic, so easy to explore and find how the built-in functionality could be adapted and extended depending on your needs. I really enjoyed working on this project and being able to push Django much further than we had in our lessons.