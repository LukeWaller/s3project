# For The Crown Clothing Website

## Overview

### What is this Website for?
 
This a shopping website for users that are interested in buying clothing and viewing fashion blog posts.I made this site for my final stream three prjoect.The site demonstrates the use of Django,Data tables and html/css/javascript. 
 
### What does it do?
 
This website uses Front-end and Backend technologies. The site allows users to easily purchase fashion items from the For The Crown brand.Not only can users purchase items they can easily scroll through blog posts to keep up to date with whats happening in the company aswell as the fashion industry.The website uses django to allow the site owner/web designer to easily add blog posts, products and update the about page without any coding knowledge right from the administration page.
 
### How does it work
 
The websites core uses the **Django** Framework run by **Python**. Django connects all the pages through urls and allows for seemless functionality with its views and models. The shop uses **Stripe** to allow users to easily purchase items right from the products page.I have used an **Sqlite** database for Djangos database tables. The styling of the website is done with **Bootstrap** and my own **CSS**.I have also used **Javascript** logic for adittional features.The Site uses **Github** version controll to keep track of any changes and the final working version has been diployed to **Heroku**

 
## Features
 
### Implemented Features
    - Website Core (Django/Python)
        - Simple and effective about page (Flat Pages)
        - Shop
            -Payments (stripe)
            - Styling (Bootstrap/Css)
        - Blog Page
        - User authentication 

    - Mobile responsive features (Css)
 
## Tech Used

### Some of the tech used includes:

- [Django](https://www.djangoproject.com/)
    - I used the Django framework for quick and stable development.

- [bootstrap](https://getbootstrap.com/)
    - I used Bootstrap for styling of the site

-[Stripe](https://stripe.com/gb)
    - I used Stripe to handle the payments on the site.

- [Disqus](https://django-disqus.readthedocs.io/en/latest/)
    - I used django-disqus to integrate comments into my blog app.



## Testing
- All testing has been done throughout the duration of the project using chrome and firefox.The mobile responsive features tested by resizing the browser windows in both chrome and firefox
 
## Contributing

- w3schools has been a good refrence site to refresh different codes and methods.

- My tutor has been a great help and inspiration for this project.

### How to get the Site working
1. Clone this repository by running the `git clone <project's Github URL>` command.
2. Setup a virtual environment by running 'virtualenv env'.(dont forget to activate 'env\Scripts\activate'.)
3. Next install all the dependencies in the requirements.txt file.
5. Next Run  `python manage.py makemigrations` and `python manage.py migrate`commands.
6. Next Run `python manage.py runserver` then you will be able to view the project on localhost:8000.