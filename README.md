# Ecommerce Website

![landing-page_shot](https://user-images.githubusercontent.com/51198797/210174879-9b206b4e-cda3-48f7-b200-9aaf3a5794cc.png)

* Built using Django and Vue
* Use Django Rest Framework to build an API in the Backend
* Use VueJS to build a separate frontend which will connect to the backend using axios

## Django Features
* The admin can perform CRUD functionalities

## VueJS Features
* Has components folder that has vue files that render cart item, order summary and product box in the front end side that the user interacts with
* Has router folder that helps in rendering whatever view that is associated with the browsers url history so we cant load stuff like cart without having a user logging in first
* Has a store folder that handles adding and removing items to and from the cart respectively
* Has views that render cart, category, checkout, home, login, myaccount, product, search, signup and success information dynamically

## Run the app
### VUE(FRONTEND)

* To run vue, cd into vue_frontend and run the command:
    ```
    npm run serve
    ```

### DJANGO(BACKEND)
* To run django, activate the environment first by enter the following in a separate comand line or terminal:
    ```
    oontztopiaenvironment/Scripts/activate
    ```
* After that enter the following command to run the django server:
    ```
    python manage.py runserver
    ```



