# Lexical Dictionary

* This app consumes the [Oxford API](https://developer.oxforddictionaries.com)
* To make use of it, type a word in the search field and hit `enter`/ click the `search` button.

# Setting up
* The **`APP_KEY`** and **`APP_ID`** environment variables are used to provide the values for **api_key** and **app_id** values respectively. These two can be obtained once you sign up as a user at [Oxford API](https://developer.oxforddictionaries.com).

> Migrations are not necessary since this app does not store any data in the database.

# Known Issues
* Responses from the API don't necessarily have the same structure. As a result, key errors can be encountered while trying to access non existent keys e.g. while getting the definition for the word `apiculture`.