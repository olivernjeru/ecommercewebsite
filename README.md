# Ecommerce Website

<h3>Technologies Used: </h3>
<p>Python, Django, Vue.js, JavaScript, Bulma, HTML & CSS</p>

<h3>New Stuff Learned</h3>
<p></p>
<p>Django folder is a python web framework that
contains django environment pre-loaded files with a few additions to help customize with my application
contains uploaded media used to display the merchandise on sell
in the products part of the site, the admin can perform CRUD functionalities
we have models file in both order and products to define attributes to be used together with the field sizes and constraints
we have serializers for both folders to convert the data sets declared earlier in the models into native python datatypes that can be easily rendered into JavaScript frameworks, aka the js framework vue i used
we have views files for both folders to process payments made via stripe for the order folder and to load products and category for the products in the product file</p>
<p>Vue folder is a JavaScript framework that
contains bulma that i used instead of bootstrap for quick styling with css involving less line css
has components folder that has vue files that render cart item, order summary and product box in the front end side that the user interacts with
has router folder that helps in rendering whatever view that is associated with the browsers url history so we cant load stuff like cart without having a user logging in first
has a store folder that handles adding and removing items to and from the cart respectively
has views that render cart, category, checkout, home, login, myaccount, product, search, signup and success information dynamically
has app file that loads the animation when opening the app or moving from one step to the next</p>

