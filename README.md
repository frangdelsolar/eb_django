# EasyBroker Technical Test

by Francisco Javier González del Solar

## How to run this project

1. Clone repository in a folder of your preference running the command.

   ```
   git clone https://github.com/frangdelsolar/eb_django.git
   ```

2. Open your terminal in the same folder and run the following command to install the required dependencies.

   ```
   pip install -r requirements.txt
   ```

3. If you are running locally, create a '.env' file in your root directory with the EasyBroker Authorization token. Otherwise, set an environment varible like this.

   ```
   EB_TOKEN=RightTokenForEasyBrokerAPI
   ```

4. Run the following command to navigate the project:

   ```
   python manage.py runserver
   ```

#### How to run the tests

1. In your root directory, run the tests of the project:

   ```
   python manage.py test -v 3
   ```

## NOTES

This is a Django project to consume the EasyBrokerAPI as a part of a technical test. The basic goal is to create a Property List page that consumes data from the api and displays upto fifteen properties. Also there should be functional pagination to retrieve bunchs of data at a time. In addition, a basic Detail View was created to test redirections and a different data call from the api.

For styling, it is being used the Bootstrap framework with some basic customization.

There is some basic testing for the api call as well as the list view. Although, there is not much coverage.
